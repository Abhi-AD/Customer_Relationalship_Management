from django.urls import path
from cms_app import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("add_member/", views.AddMember.as_view(), name="add_member"),
    path("plan/", views.Plan.as_view(), name="plan"),
]
