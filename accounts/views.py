from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.sessions.models import Session
from referrals.models import Refer
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=password)
            login(request, user)
            return redirect('/accounts/profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# separation of concern principle
@login_required
def profile(request):
    products = Product.objects.filter(owner=request.user)
    refers = Refer.objects.filter(inviter=request.user)
    for refer in refers:
        print(refer.product.name)
        print(refer.product.price)

    context = {
        'products': products,
        'refers': refers,
        'user': request.user.email
    }
    return render(request, template_name="registration/profile.html", context=context)
