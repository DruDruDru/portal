from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from core.models import Claim
from users.forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.views import generic


class SighUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/sighup.html'


class ClaimListView(LoginRequiredMixin, generic.ListView):
    model = Claim
    template_name = 'users/profile.html'
    context_object_name = 'claims'
    paginate_by = 1

    def get_queryset(self):
        user = self.request.user
        queryset = Claim.objects.filter(who_created=user)
        return queryset





