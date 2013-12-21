from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import Context
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ArchiveIndexView, DetailView, CreateView, DeleteView 
# from xhtml2pdf import pisa             # import python module
from accounts.models import User, Trainee

def index(request):
    name = User(firstname ="Armad", lastname ="Ellis")
    list = User.objects.all().order_by('firstname')
    
    
    
