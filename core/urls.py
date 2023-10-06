from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create_claim/', views.create_claim, name='create_claim'),
    path('create_claim/success/', views.create_claim_success, name='success'),
    path('delete_claim/', views.claim_delete, name='delete_claim'),
    path('delete_claim/<int:pk>', views.claim_delete_confirm, name='delete_claim_confirm'),
    path('update_claim/', views.claim_update, name='update_list'),
    path('update_claim/<int:pk>', views.ClaimUpdate.as_view(), name='update_claim'),
]
