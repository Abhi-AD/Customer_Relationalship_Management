from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.



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
    

    