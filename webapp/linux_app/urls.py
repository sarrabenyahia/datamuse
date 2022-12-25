from django.contrib import admin
from django.urls import path, include
from .views import HomeView
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path('',views.index, name="index"),
    path("predict", views.home, name="result"),
]