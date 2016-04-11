from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.template import loader
from .models import Vare
from .forms import VareForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.models import User


def index(request):
    vare = Vare.objects.all().order_by('-id')


    if request.method == 'POST':
        form = VareForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.kalkulering = do_calc(post.pris, post.volum, post.alkohol)
            post.save()
            form = VareForm()

    else:
        form = VareForm

    return render(request, 'index.html', {'form':form, 'vare':vare},)

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
                return redirect('index.html')
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
    return render(request, 'login.html', context)

def login_user(request):
    context = RequestContext(request)
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('index')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print
            "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('login.html', {}, context)
