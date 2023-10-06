from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, reverse
from .models import Claim
from django.contrib.auth.decorators import login_required
from .forms import ClaimForm
from .models import validate_image_size
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import CreateView, UpdateView


def home(request):
    user = request.user
    claims = Claim.objects.all().filter(status='в').order_by('-updated_at')[0:4]
    claims_count = Claim.objects.all().filter(status='в').count()
    return render(request, 'core/home.html',
                  context={'claims': claims, 'user': user,
                           'claims_count': claims_count})


@login_required
def create_claim(request):
    if request.method == 'POST':
        form = ClaimForm(request.POST, request.FILES)
        if form.is_valid():
            if validate_image_size(form.cleaned_data.get('image')):
                return HttpResponse('<p style="color: red;">Слишком большой файл</p>')
            current_user = request.user

            form.save()
            claim = form.save(commit=False)
            claim.who_created = current_user
            form.save()

            return redirect('success/', permanent=True)
    else:
        form = ClaimForm()
    return render(request, 'create_claim.html',
                  {'form': form, 'user': request.user})


@login_required
def claim_delete(request):
    claims = Claim.objects.filter(who_created=request.user)
    return render(request, 'delete_claim.html',
                  context={'claims': claims})


@login_required
def claim_delete_confirm(request, pk):
    claim = get_object_or_404(Claim, pk=pk)
    claim.delete()
    return redirect('profile')


@login_required
def create_claim_success(request):
    return render(request, 'create_claim_success.html')


@login_required
def claim_update(request):
    claims = Claim.objects.all()
    return render(request, 'claim_update.html',
                  context={'claims': claims})


class ClaimUpdate(LoginRequiredMixin, UpdateView):
    model = Claim
    template_name = 'claim_update_form.html'
    fields = ['status', 'category']
