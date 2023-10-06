from django.urls import path

from . import views

urlpatterns = [
    path('sighup/', views.SighUpView.as_view(), name='sighup'),
    path('profile/', views.ClaimListView.as_view(), name='profile'),
]
