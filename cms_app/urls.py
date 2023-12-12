from django.urls import path
from cms_app import views
from cms_app.views import SubscriptionDetailView,ContactView


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("add_member/", views.AddMember.as_view(), name="add_member"),
    path("plan/", views.Plan.as_view(), name="plan"),
    path("signin/", views.SignInView.as_view(), name="signin"),
    path("login/", views.LogInView.as_view(), name="login"),
    path("subscription/", SubscriptionDetailView.as_view(), name="subscription_detail"),
    path("contact/", ContactView.as_view(), name="contact"),
]

