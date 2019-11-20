from django.urls import path
from . import views

app_name = 'ghosting'

urlpatterns = [
    path('', views.home)
]