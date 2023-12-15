from django.urls import path
from cms_app import views
from cms_app.views import (
    SubscriptionDetailView,
    ContactView,
    AttendanceListView,
    CashTransactionListView,
    CashTransactionCreateView,
    InventoryListView,
    InventoryCreateView,
    InventoryBalanceListView,
    InventoryBalanceCreateView,
    AddMemberView,
)


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("plan/", views.Plan.as_view(), name="plan"),
    path("signin/", views.SignInView.as_view(), name="signin"),
    path("subscription/", SubscriptionDetailView.as_view(), name="subscription_detail"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("attendance/", AttendanceListView.as_view(), name="attendance"),
 
    path("add_member/",AddMemberView.as_view(), name="add_member"),
    path("cashtransaction_list/", CashTransactionListView.as_view(), name="cashtransaction_list"),
    path("cashtransaction_form/", CashTransactionCreateView.as_view(), name="cashtransaction_form"),
    path("inventory_list/", InventoryListView.as_view(), name="inventory_list"),
    path("inventory_create/", InventoryCreateView.as_view(), name="inventory_create"),
    path("inventory_balance/", InventoryBalanceListView.as_view(), name="inventory_balance"),
    path("inventory_balance_create/", InventoryBalanceCreateView.as_view(), name="inventory_balance_create"),
]
