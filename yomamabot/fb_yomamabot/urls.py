from django.urls import include, path
from django.urls import re_path as url
from .views import YoMamaBotView
urlpatterns = [
                  path('botget', YoMamaBotView.as_view())
               ]