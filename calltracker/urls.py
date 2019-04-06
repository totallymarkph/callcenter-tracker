from django.urls import path
from . import views

urlpatterns = [
    path('', views.calltracker_homepage, name='calltracker_homepage'),
]