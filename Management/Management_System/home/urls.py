from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('success/', views.success, name='success'),
]
