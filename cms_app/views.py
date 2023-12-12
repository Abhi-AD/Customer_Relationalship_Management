from django.shortcuts import render
from django.views.generic import TemplateView,View
from django.contrib.auth.mixins import LoginRequiredMixin

from cms_app.models import *
# Create your views here.

class SubscriptionDetailView(TemplateView):
    template_name = 'plan.html'

class HomeView(TemplateView):
    template_name = "index.html"
    
    
class AddMember(TemplateView):
    template_name = "add_member.html"
    
class Plan(TemplateView):
    template_name = "plan.html"
    

class LogInView(TemplateView):
    template_name = "log_in.html"
    
    
class SignInView(TemplateView):
    template_name = "sign_in.html"
    
