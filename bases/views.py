from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin,\
     PermissionRequiredMixin
from django.views import generic


# Create your views here.
class Home(generic.TemplateView):
    template_name = 'bases/home.html'
    
