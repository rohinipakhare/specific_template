from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView
from app.models import *


class school_list(ListView):
    model=School
    context_object_name='schools'
    #queryset=School.objects.filter(id=1)
    
    template_name='app/school_list.html'


class school_detail(DetailView):
    model=School
    context_object_name='sclobject'