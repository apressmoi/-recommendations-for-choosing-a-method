from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import TypePrint
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserRegisterForm, CalculateForm


def home(request):
    return render(request, 'core/home.html')


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('core:home-page')
    return render(request, 'core/signup.html', {'auth_form': form})


def register(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('core:home-page')
    return render(request, 'core/signup.html', {'register_form': form})


def logout_view(request):
    logout(request)
    return render(request, 'core/home.html')


def calculate_view(request):
    form = CalculateForm(request.POST or None)
    if form.is_valid():
        colorfulness = form.cleaned_data.get('colorfulness')
        production = form.cleaned_data.get('production')
        count = form.cleaned_data.get('count')
        # List with available types of printing
        type_printing = TypePrint.objects.filter(
            production__name_product__icontains=production,
            )
        print(colorfulness, production, count)
        return render(request, 'core/home.html')
    return render(request, 'core/home.html', {'calc_form': form})

