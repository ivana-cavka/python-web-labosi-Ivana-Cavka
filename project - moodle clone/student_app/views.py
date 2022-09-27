import datetime
import os
from django.shortcuts import render
from project_task.settings import MEDIA_ROOT
from student_app.forms import DocumentForm, UserForm
from student_app.models import Document, RolesEnum, Student_Document, CustomUser
from django.contrib.auth import login, logout
from django.http import *
from django.shortcuts import redirect
from django.core.paginator import Paginator
from student_app.validate import CustomBackend
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password
from student_app.decorators import admin_auth_required, profesor_auth_required, student_auth_required

def login_view(request):
    #logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        print(password)
        user = CustomBackend.authenticate_user(username, password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                user_object = CustomUser.objects.get(username=username)
                role = user_object.role
                id = user_object.id
                return redirect(role, id=id)
        return render(request, 'login_page.html', {"message" : 'neispravni podaci, molimo pokušajte ponovno'})
    return render(request, 'login_page.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@student_auth_required
def student_view(request, id):
    st_id = request.user.id
    student = CustomUser.objects.get(pk=st_id)
    relations = Student_Document.objects.filter(student_id_id=st_id)
    professors = CustomUser.objects.filter(role='profesor')
    #filtriranje
    filtering_method = request.GET.get('select_filtering')
    filter_by_prof = CustomUser.objects.filter(username=filtering_method).first()
    documents = []
    for r in relations:
        document = Document.objects.get(pk=r.document_id_id)
        if filter_by_prof is None:
            documents.append(document)
        elif filter_by_prof is not None:
            if document.creator_id == filter_by_prof.id:
                documents.append(document)
    #sortiranje
    sorting_method = request.GET.get('select_sorting')
    if sorting_method == 'v1':
        documents.sort(key=lambda x: x.title.upper())
    elif sorting_method == 'v2':
        documents.sort(key=lambda x: x.created, reverse=True)
    elif sorting_method == 'v3':
        documents.sort(key=lambda x: x.created)
    #paginacija
    paginator = Paginator(documents, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'student_page.html', {"student_data" : student, "document_data" : page_obj, "profesor_data" : professors})

@profesor_auth_required
def professor_view(request, id):
    pf_id = request.user.id
    profesor = CustomUser.objects.get(pk=pf_id)
    #Pregled dokumenata je sortiran po datumu kreacije
    documents = Document.objects.filter(creator_id=pf_id).order_by('created')
    #paginacija
    paginator = Paginator(documents, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'professor_page.html', {"profesor_data" : profesor, "document_data" : page_obj})

@profesor_auth_required
def add_document(request):
    pf_id = request.user.id
    if request.method == 'GET':
        form = DocumentForm()
        return render(request, 'add_document.html', {"form" : form, "profesor_data" : pf_id})
    elif request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            new_doc = form.save(commit=False)
            new_doc.created = datetime.datetime.now() 
            new_doc.creator_id = pf_id
            #dodavanje dokumenta s file systemom 
            request_file = request.FILES['document'] if 'document' in request.FILES else None
            print(request_file)
            if request_file:
                fs = FileSystemStorage()
                file = fs.save(request_file.name, request_file)
                fileurl = fs.url(file)
                new_doc.path = fileurl
            new_doc.save()
            form.save_m2m()
        return redirect(RolesEnum.Profesor, id=pf_id)

@profesor_auth_required
def update_document(request, id):
    pf_id = request.user.id
    existing_document = Document.objects.get(pk=id)
    if request.method == 'GET':
        form = DocumentForm(instance=existing_document)
        return render(request, 'update_document.html', {"form" : form, "profesor_data" : pf_id})
    elif request.method == 'POST':
        form = DocumentForm(request.POST, instance=existing_document)
        if form.is_valid():
            #dodavanje dokumenta s file systemom 
            request_file = request.FILES['document'] if 'document' in request.FILES else None
            if request_file:
                fs = FileSystemStorage()
                file = fs.save(request_file.name, request_file)
                fileurl = fs.url(file)
                #brisanje starog dokumenta
                old_file_path = existing_document.path
                old_file_name = old_file_path.rsplit('/', 2)
                os.remove(os.path.join(MEDIA_ROOT, old_file_name[2].replace("%20"," ")))
                existing_document.path = fileurl
            form.save()
        return redirect(RolesEnum.Profesor, id=pf_id)

@profesor_auth_required
def delete_document(request, id):
    pf_id = request.user.id
    doc = Document.objects.get(pk=id)
    file_name=doc.path.rsplit('/', 2)
    os.remove(os.path.join(MEDIA_ROOT, file_name[2].replace("%20"," ")))
    doc.delete()
    return redirect(RolesEnum.Profesor, id=pf_id)

@profesor_auth_required
def share_document(request, id):
    pf_id = request.user.id
    document = Document.objects.get(pk=id)
    all_students = CustomUser.objects.filter(role='student')
    #pretraga studenata s kojima je dokument već podijeljen
    shared_students_relations = Student_Document.objects.filter(document_id_id=id)
    shared_students = []
    for relation in shared_students_relations:
        shared_students.append(CustomUser.objects.get(pk=relation.student_id_id))
    print("SHARED: ", shared_students)
    if request.method == 'GET':
        return render(request, 'sharing_page.html', {"students_data" : all_students, "students_already_shared" : shared_students, "document_data" : document, "profesor_data" : pf_id})
    elif request.method == 'POST':
        #pretraga studenata koji su označeni
        checked_students_usernames = list(request.POST.getlist('student_checkbox'))
        print(checked_students_usernames)
        checked_students = []
        for username in checked_students_usernames:
            checked_students.append(CustomUser.objects.filter(username=username).first())
        print("CHECKED: ", checked_students)
        #provjera da nisu oba prazni
        if shared_students != [] and checked_students != []:
            for student in shared_students:
                #oni koji više nisu označeni se brišu
                if student not in checked_students:
                    old_relation = Student_Document.objects.filter(document_id_id=id, student_id_id=student.id).first()
                    old_relation.delete()
            for student in checked_students:
                #novooznačeni se spremaju
                if student not in shared_students:
                    new_relation = Student_Document(document_id_id=id, student_id_id=student.id)
                    new_relation.save()
        #ako nije bilo već označenih, svi se spremaju
        elif shared_students == []:
            for student in checked_students:
                new_relation = Student_Document(document_id_id=id, student_id_id=student.id)
                new_relation.save()
        return redirect(RolesEnum.Profesor, id=pf_id)

@profesor_auth_required
def stop_sharing_document(request, id):
    pf_id = request.user.id
    shared_students_relations = Student_Document.objects.filter(document_id_id=id)
    for relation in shared_students_relations:
        relation.delete()
    return redirect(RolesEnum.Profesor, id=pf_id)

@admin_auth_required
def admin_view(request, id):
    ad_id = request.user.id
    admin = CustomUser.objects.get(pk=ad_id)
    #sortiranih po kriteriju student/profesor => filtriranih?
    filtering_method = request.GET.get('select_filtering')
    if filtering_method is None:
        users = CustomUser.objects.all()
    else:
        users = CustomUser.objects.filter(role=filtering_method)
    #paginacija
    paginator = Paginator(users, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin_page.html', {"admin_data" : admin, "user_data" : page_obj})

@admin_auth_required
def new_user(request):
    ad_id = request.user.id
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'add_user.html', {"form" : form, "admin_data" : ad_id})
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.date_joined = datetime.datetime.now() 
            input_password = new_user.password
            new_user.password = make_password(input_password,salt=None, hasher='default')
            new_user.save()
            form.save_m2m()
        return redirect(RolesEnum.Admin, id=ad_id)

@admin_auth_required
def update_user(request, id):
    ad_id = request.user.id
    existing_user = CustomUser.objects.get(pk=id)
    if request.method == 'GET':
        form = UserForm(instance=existing_user)
        return render(request, 'update_user.html', {"form" : form, "admin_data" : ad_id})
    elif request.method == 'POST':
        form = UserForm(request.POST, instance=existing_user)
        if form.is_valid():
            input_password = existing_user.password
            existing_user.password = make_password(input_password,salt=None, hasher='default')
            form.save()
        return redirect(RolesEnum.Admin, id=ad_id)

@admin_auth_required
def delete_user(request, id):
    ad_id = request.user.id
    user = CustomUser.objects.get(pk=id)
    user.delete()
    return redirect(RolesEnum.Admin, id=ad_id)

@admin_auth_required
def manage_students(request):
    students = CustomUser.objects.filter(role='student')
    relations = {}
    for st in students:
        relations_by_student = Student_Document.objects.filter(student_id_id=st.id).count()
        relations[st.id]=relations_by_student
    return render(request, 'admin_manage_students.html', {"students" : students, "relations" : relations})
  
@admin_auth_required
def documents_per_student(request, id):
    student = CustomUser.objects.get(pk=id)
    relations = Student_Document.objects.filter(student_id_id=id)
    profesori = CustomUser.objects.filter(role='profesor')
    documents = []
    for rel in relations:
        documents.append(Document.objects.get(pk=rel.document_id_id))
    return render(request, 'admin_show_documents.html', {"student" : student, "documents" : documents, "profesori" : profesori})