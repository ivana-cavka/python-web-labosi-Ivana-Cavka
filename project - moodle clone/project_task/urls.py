"""project_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from student_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('administrator/<int:id>/', views.admin_view, name='administrator'),
    path('student/<int:id>/', views.student_view, name='student'),
    path('profesor/<int:id>/', views.professor_view, name='profesor'),
    path('new_document/', views.add_document),
    path('delete_document/<int:id>/', views.delete_document),
    path('update_document/<int:id>/', views.update_document),
    path('share/<int:id>/', views.share_document),
    path('stop_sharing/<int:id>/', views.stop_sharing_document),
    path('new_user/', views.new_user),
    path('delete_user/<int:id>/', views.delete_user),
    path('update_user/<int:id>/', views.update_user),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('manage_students/', views.manage_students),
    path('doc_per_st/<int:id>/', views.documents_per_student),
]
  
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)