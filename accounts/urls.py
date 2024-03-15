from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.SignupVie.as_view(),name='signup')
]
