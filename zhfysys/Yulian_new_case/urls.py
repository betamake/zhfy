from django.contrib import admin
from django.urls import path,include
from django.views.static import serve
from django.conf.urls import url
import sys
import os
sys.path.append(os.path.realpath('.'))
from zhfysys import settings
from . import views
urlpatterns = [
    path('base_massage/', views.get_base_massage),
    path('t_msys/', views.get_ms_t_msys),
    path('upload/', views.upload),
    url('media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT})
]