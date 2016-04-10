from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader
from .models import Vare
from .forms import VareForm, UserForm
from django.contrib.auth import authenticate, login
from django.views.generic import View


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

#def footer(request):
 #   vare = Vare.objects.all()
#
 #   return render(request, 'index.html', {'vare':vare},)