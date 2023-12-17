from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View, ListView, CreateView
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse,reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.views import View
from django.contrib import messages
from django.db.models import Sum

from django.db.models import Count
from django.utils import timezone

from cms_app.models import *
from cms_app.forms import (
    ContactForm,
    CashTransactionForm,
    InventoryForm,
    InventoryBalanceForm,
    RegistrationForm,
)

# create the view


class SubscriptionDetailView(TemplateView):
    template_name = "plan.html"


class HomeView(TemplateView):
    template_name = "index.html"


class SignInView(TemplateView):
    template_name = "sign_in.html"





# list view
class Plan(ListView):
    model = Plan_Subscription
    template_name = "plan.html"
    context_object_name = "plans"

class AttendanceListView(ListView):
    model = Attendance
    template_name = "attendance_list.html"
    context_object_name = "attendance_list"

    def get_queryset(self):
        return Attendance.objects.all()

class CashTransactionListView(ListView):
    model = CashTransaction
    template_name = "cashtransaction_list.html"

    def get_queryset(self):
        return CashTransaction.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cash_in_transactions = CashTransaction.objects.filter(transaction_type='CASH_IN')
        cash_out_transactions = CashTransaction.objects.filter(transaction_type='CASH_OUT')
        cash_in_sum = cash_in_transactions.aggregate(Sum('amount'))['amount__sum'] or 0
        cash_out_sum = cash_out_transactions.aggregate(Sum('amount'))['amount__sum'] or 0
        cash_difference = cash_in_sum - cash_out_sum

        context.update({
            'cash_in_transactions': cash_in_transactions,
            'cash_out_transactions': cash_out_transactions,
            'cash_in_sum': cash_in_sum,
            'cash_out_sum': cash_out_sum,
            'cash_difference': cash_difference,
        })

        return context

class InventoryListView(ListView):
    model = Inventory
    template_name = "inventory_list.html"

    def get_queryset(self):
        return Inventory.objects.all()

class InventoryBalanceListView(ListView):
    model = InventoryBalance
    template_name = "inventorybalance_list.html"

    def get_queryset(self):
        return InventoryBalance.objects.all()


# create view

class AddMemberView(CreateView):
    template_name = 'add_member.html'
    form_class = RegistrationForm
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Successfully submitted your query. We will add you soon "
            )
            return redirect("add_member")
        else:
            messages.error(request, "Cannot submit your data. ")
            return render(
                request,
                self.template_name,
                {"form": form},
            )

class ContactView(CreateView):
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

class CashTransactionCreateView(CreateView):
    template_name = 'cashtransaction_form.html'
    form_class = CashTransactionForm
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Successfully submitted your query. We will transaction you soon "
            )
            return redirect("cashtransaction_form")
        else:
            messages.error(request, "Cannot submit your data. ")
            return render(
                request,
                self.template_name,
                {"form": form},
            )
      
class InventoryCreateView(CreateView):
    template_name = 'inventory_form.html'
    form_class = InventoryForm
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Successfully submitted your query. We will transaction you soon "
            )
            return redirect("inventory_create")
        else:
            messages.error(request, "Cannot submit your data. ")
            return render(
                request,
                self.template_name,
                {"form": form},
            )
      
class InventoryBalanceCreateView(CreateView):
    template_name = 'inventory_form.html'
    form_class = InventoryBalanceForm
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Successfully submitted your query. We will transaction you soon "
            )
            return redirect("inventory_balance_create")
        else:
            messages.error(request, "Cannot submit your data. ")
            return render(
                request,
                self.template_name,
                {"form": form},
            )
      

