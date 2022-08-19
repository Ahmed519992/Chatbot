# yomamabot/yomamabot/urls.py
from django.urls import path, include
from django.urls import re_path as url
from django.contrib import admin
urlpatterns =[
    path(r'admin/', admin.site.urls),
    path(r'fb_yomamabot/', include('fb_yomamabot.urls')),
]