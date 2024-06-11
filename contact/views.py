from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import *


# Create your views here.
class ContactCreateView(CreateView):
    model = Contact
    template_name = 'contact.html'
    fields = ['name', 'email', 'subject', 'message']
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.instance.save()
        return redirect(reverse_lazy('contact'))

        