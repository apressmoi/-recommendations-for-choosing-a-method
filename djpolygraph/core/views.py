from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import TypePrint, Profile
from django.contrib.auth import authenticate, login, logout
from django.db.models import Min, Max
from .forms import UserLoginForm, UserRegisterForm, CalculateForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


def home(request):
    return render(request, 'core/landing.html')


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('core:home-page')
    return render(request, 'core/login.html', {'auth_form': form})


def register(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        return redirect('core:login')
    return render(request, 'core/registration.html', {'register_form': form})


def logout_view(request):
    logout(request)
    return render(request, 'core/landing.html')


@login_required
def calculate_view(request):
    form = CalculateForm(request.POST or None)
    if form.is_valid():
        result = None
        colorfulness = form.cleaned_data.get('colorfulness')
        production = form.cleaned_data.get('production')
        count = form.cleaned_data.get('count')
        type_paper = form.cleaned_data.get('paper').split(" ")[0]
        type_printing = TypePrint.objects.filter(
            production__name_product__icontains=production,
            production__paper__type_paper=type_paper,
            colorfulness__colorfulness__icontains=colorfulness,
            count__min_count__lte=count,
            count__max_count__gte=count,
            )
        
        if len(type_printing) > 1:
            minimal_count = type_printing.aggregate(Min('count__max_count'))['count__max_count__min']
            result = TypePrint.objects.get(count__max_count=minimal_count)
        else:
            result = TypePrint.objects.get(id=type_printing.first().id)
        profile = Profile.objects.get(user=request.user)
        profile.result = result
        profile.save()
        return redirect('core:home-page')
    return render(request, 'core/calculate.html', {'calc_form': form})


@login_required
def send_message_to_email(request):
    profile = Profile.objects.get(user=request.user)
    result_calculate = profile.result
    if result_calculate == None:
        return redirect('core:calculate')
    another_product = [obj.name_product for obj in profile.result.production.all()]
    subject = "Расчет от сайта calculator 2.0"
    message = f"""Здравствуйте {request.user}! Наилучшим результатом для вашего последнего
    расчета явлется выбор печати: {profile.result.name_print}, благодаря ей вы также можете печатать
    {another_product}"""
    _from =  'calculator2@gmail.com' 
    _to = profile.user.email
    send_mail(subject, message, _from, [_to])
    return redirect('core:home-page')
    

