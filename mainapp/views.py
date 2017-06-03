from django.shortcuts import render, redirect

from .forms import *
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html',{})

def createCoffee(request):
    context={}
    if request.method=="POST":
        form=CoffeeForm(request.POST)
        context['form']=form
        if form.is_valid():
            coffee=form.save(commit=False)
            coffee.user=request.user
            coffee.save()
            form.save_m2m()
            return redirect("home")
        else:
            return render(request, 'createCoffee.html',context)
    else:
        form=CoffeeForm()
        context['form']=form
        return render(request, 'createCoffee.html', context)

def editCoffee(request, coffee_id):
    context={}
    coffee=Coffee.objects.get(id=coffee_id)
    context['coffee']=coffee
    if request.method=="POST":
        form=CoffeeForm(request.POST, instance=coffee)
        context['form']=form
        if form.is_valid():
            coffee=form.save(commit=False)
            coffee.user=request.user
            coffee.save()
            form.save_m2m()
            return redirect("home")
        else:
            return render(request, 'editCoffee.html',context)
    else:
        form=CoffeeForm(instance=coffee)
        context['form']=form
        return render(request, 'editCoffee.html', context)
