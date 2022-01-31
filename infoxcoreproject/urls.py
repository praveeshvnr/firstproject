"""infoxcoreproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import re_path, include
from django.urls import path
from .import views
from coreapp import views as view
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

#--------marketing--------------
import taskapp
#--------------------------------

urlpatterns = [
    re_path(r'^$', views.hr,name='hr'),
    re_path(r'^coreapp/',include('coreapp.urls')),
    re_path(r'^admin/', admin.site.urls),
    # path("<str:username>",view.qrshow,name="qrshow"),
    #path("<str:username>", view.intqrshow, name="intqrshow"),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    #-----------------marketing-----------------
    re_path(r'^index2', views.index2, name='index2'),
    re_path(r'^taskapp/',include('taskapp.urls')),
    #------------------------------------------------
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
