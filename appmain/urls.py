from django.urls import path

from appmain.views import index

urlpatterns = [
    path('', index),
]
