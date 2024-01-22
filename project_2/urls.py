"""project_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from project_2 import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('try/', views.try1),
    path('', views.homepage,name="home"),
    path('web/', views.web,name="web"),
    path('c_language/', views.c_language,name="c_language"),
    path('java/', views.java,name="java"),
    path('login/', views.login,name="login"),
    path('signup/', views.signup,name="signup"),
    path('get_method/', views.get_method,name="get"),
    path('post_method/', views.post_method,name="post"),
    path('output1/', views.output1,name="output1"),
    path('calc/', views.calculator,name="calc"),
    path('avg/', views.subjectavg,name="subjectavg"),
    path('model_demo/', views.model_demo,name="model_demo"),
    path('detailpage/<slug>', views.detailpage,name="detailpage"),
    path('paging/', views.paging,name="paging"),
    path('save_data/', views.save_data,name="save_data"),
    path('send_mail/', views.sendingmail,name="send_mail")
]


if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)