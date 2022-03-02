from django.urls import path
from . import views

app_name = 'OOEngine'

urlpatterns = [
    path('',views.home_view, name='home'),
]