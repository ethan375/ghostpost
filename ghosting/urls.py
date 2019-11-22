from django.urls import path
from . import views

app_name = 'ghosting'

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.new_post, name='new_post'),
    path('vote/up/<int:id>/', views.up_vote),
    path('vote/down/<int:id>/', views.down_vote),
    path('sort/boasts/', views.boasts, name='boasts'),
    path('sort/roasts/', views.roasts, name='roasts'),
    path('sort/votes/', views.votes, name="votes")
]