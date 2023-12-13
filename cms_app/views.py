from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy

from django.db.models import Count
from django.utils import timezone
from django.http import JsonResponse

from cms_app.models import *
from cms_app.forms import (
    ContactForm,
    CashTransactionForm,
    InventoryForm,
    InventoryBalanceForm,
)

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
    template_name = "plan.html"
    context_object_name = "plans"


class LogInView(TemplateView):
    template_name = "log_in.html"


class SignInView(TemplateView):
    template_name = "sign_in.html"


class AttendanceListView(ListView):
    model = Attendance
    template_name = "attendance_list.html"  # Provide the template name where you'll display the attendance data
    context_object_name = "attendance_list"  # Specify the variable name to use in the template for the queryset

    def get_queryset(self):
        return Attendance.objects.all()





class CashTransactionListView(ListView):
    model = CashTransaction
    template_name = "cashtransaction_list.html"
    
    def get_queryser(self):
        return CashTransaction.objects.all()



# class CashTransactionCreateView(View):
#     template_name = "cashtransaction_form.html"

#     def get(self, request):
#         return render(request, self.template_name)

#     def post(self, request):
#         form = CashTransactionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(
#                 request, "Successfully submitted your query. We will transactions you soon "
#             )
#             return redirect("cashtransaction_form")
#         else:
#             messages.error(request, "Cannot transactions error. ")
#             return render(
#                 request,
#                 self.template_name,
#                 {"form": form},
#             )



class CashTransactionCreateView(CreateView):
    model = CashTransaction
    form_class = CashTransactionForm
    template_name = 'cashtransaction_form.html'  # Specify the template you want to use
    success_url = reverse_lazy('success_url_name')  # Specify the success URL after the form is submitted

    def form_valid(self, form):
        # You can customize the behavior after the form is successfully validated and saved.
        # For example, you can add additional logic or set additional fields before saving.
        return super().form_valid(form)




class InventoryListView(ListView):
    model = Inventory
    template_name = "inventory_list.html"
    
    def get_queryset(self):
        return Inventory.objects.all()


class InventoryCreateView(CreateView):
    model = Inventory
    form_class = InventoryForm
    template_name = "inventory_form.html"
    success_url = "/success/"  # Redirect to success page after form submission


class InventoryBalanceListView(ListView):
    model = InventoryBalance
    template_name = "inventorybalance_list.html"
    
    def get_queryset(self):
        return InventoryBalance.objects.all()


class InventoryBalanceCreateView(CreateView):
    model = InventoryBalance
    form_class = InventoryBalanceForm
    template_name = "inventorybalance_form.html"
    success_url = "/success/"  # Redirect to success page after form submission
