from django.urls import path

from config import settings
from contact.views import *

urlpatterns = [
    path('contact/', ContactCreateView.as_view() , name='contact')
]

