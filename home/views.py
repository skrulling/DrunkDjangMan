from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.template import loader
from .models import Vare
from .forms import VareForm, UserForm, TempVareForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.models import User

def notuser(request):
    if request.method == 'POST':
        form = TempVareForm(request.POST)
        if form.is_valid():
            pris = form.pris
            volum = form.volum
            alkohol = form.alkohol
            kalkulering = do_calc(pris, volum, alkohol)

            return HttpResponse(kalkulering)

    return render(request, 'not_user_home.html',)

def index(request):
    if not request.user.is_authenticated():
        return redirect(notuser)
    else:
        vare = Vare.objects.filter(user=request.user).order_by('-id')
        top = Vare.objects.filter(user=request.user).order_by('kalkulering')[:3]


        if request.method == 'POST':
            form = VareForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.kalkulering = do_calc(post.pris, post.volum, post.alkohol)
                post.user = request.user
                post.save()
                form = VareForm()

        else:
            form = VareForm

        return render(request, 'index.html', {'form':form, 'vare':vare, 'top':top},)

def do_calc(pris, volum, alkohol):

    resultat = (float(pris)/((float(alkohol)/100) * float(volum)))/50
    resultat = "%.2f" % resultat

    return resultat

def register(request):
    form = UserForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(index)
    context = {
        "form": form,
    }
    return render(request, 'registration_form.html', context)

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'logged_out.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                vare = Vare.objects.all().order_by('-id')
                form = UserForm()

                return redirect(index)
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})

    return render(request, 'login.html', {})
