from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from app.models import *


class school_list(ListView):
    model=School
    context_object_name='schools'
