
from .views import DefaultView
from django.urls import path

urlpatterns = [
    path('', DefaultView.as_view(), name='home'),
]
