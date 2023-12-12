from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages

from django.db.models import Count
from django.utils import timezone
from django.http import JsonResponse

from cms_app.models import *
from cms_app.forms import ContactForm
# create the view


class SubscriptionDetailView(TemplateView):
    template_name = "plan.html"




class ContactView(View):
    template_name = "contact.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Successfully submitted your query. We will contact you soon "
            )
            return redirect("contact")
        else:
            messages.error(request, "Cannot submit your data. ")
            return render(
                request,
                self.template_name,
                {"form": form},
            )













class HomeView(TemplateView):
    template_name = "index.html"














class AddMember(TemplateView):
    template_name = "add_member.html"


class Plan(ListView):
    model = Plan_Subscription
    template_name = 'plan.html'
    context_object_name = 'plans'












class LogInView(TemplateView):
    template_name = "log_in.html"


class SignInView(TemplateView):
    template_name = "sign_in.html"
