from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader
from .models import Vare
from .forms import VareForm


def index(request):
    vare = Vare.objects.all()
    context = {
        'vare':vare
    }

    if request.method == 'POST':
        form = VareForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form = VareForm()

    else:
        form = VareForm

    return render(request, 'index.html', {'form':form},)

#def footer(request):
 #   vare = Vare.objects.all()
#
 #   return render(request, 'index.html', {'vare':vare},)