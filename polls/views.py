from django.shortcuts import render, redirect
from polls.models import Sign
from .forms import SignForm
from django.http import HttpResponseRedirect

# Create your views here.


def thankYou(request):
    return render(request, "thank_you.html")

def polls(request):
    if request.method == "POST":
        form = SignForm(request.POST)
        email = request.POST["email"]
        password = request.POST["password"]
        data = Sign(email = email, password = password)
        data.save()
        return HttpResponseRedirect('thank_you.html')
    
    else:
        form = SignForm()


    return render(request, "polls.html", {'form':form})
