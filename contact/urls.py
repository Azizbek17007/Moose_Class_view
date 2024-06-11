from django.urls import path

from contact.views import about_page

urlpatterns = [
path('contact/', about_page, name='about')
]