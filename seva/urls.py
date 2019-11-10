"""seva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from convsort import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('company/<str:nam>', views.company, name='company'),
    path('admin/', views.admin, name='admin'),
    path('form/', views.form, name='form'),
    path('student_result/<str:nam>', views.student_result, name='student_result'),
    path('upload/', views.upload, name='upload'),
    path('registration/', views.register, name='register'),
    path('',views.login,name=" "),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('allcompanies/',views.allcompanies,name="allcompanies"),
    path('allstudents/',views.allstudents,name="allstudents"),
    path('info/',views.info,name="info"),
    path('admin_students/',views.admin_students,name="admin_students"),
    path('admincompanies/',views.admincompanies,name="admincompanies"),
    
   
]
handler404 = views.error_404

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
