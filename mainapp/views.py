from django.shortcuts import render, redirect

from .forms import *
from django.contrib.auth.models import User
import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import logout
# def home(request):
#     return render(request, 'home.html',{})

def naughty_page(request):
    return render(request, 'naughty_page.html', {})

# def auth(x):
#     if not x.user.is_authenticated():
#         return redirect('/accounts/github/login')
#
# def super_awsome_user(x):
#     if not x.user.is_authenticated():
#         return redirect('/admin')
#     if not x.user.is_staff:
#         return redirect('/admin')


def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    context={}
    if not request.user.is_authenticated():
        return redirect('/accounts/github/login')
    user=request.user
    context['user']=user
    if request.method=="POST":
        form =SearchForm(request.POST)
        if form.is_valid():
            context['form']=form
            date=form.cleaned_data['date']
            context['today']=date
            order_list=Order.objects.filter(user=user, date=date)
            context['order_list']=order_list
    else:
        form =SearchForm()
        context['form']=form
        today=datetime.date.today()
        context['today']=today
        order_list=Order.objects.filter(user=user, date=today)
        context['order_list']=order_list
    coffee_list=Coffee.objects.filter(user=user)
    context['coffee_list']=coffee_list
    return render(request, 'home.html', context)

def createCoffee(request):
    context={}
    if not request.user.is_authenticated():
        return redirect('/accounts/github/login')
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
    if not request.user.is_authenticated():
        return redirect('/accounts/github/login')
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

def deleteCoffee(request, coffee_id):
    if not request.user.is_authenticated():
        return redirect('/accounts/github/login')
    Coffee.objects.get(id=coffee_id).delete()
    return redirect("home")


def createBean(request):
    context={}
    if not request.user.is_authenticated():
        return redirect('/admin')
    if not request.user.is_staff:
        return redirect('/admin')

    if request.method=="POST":
        form=BeanForm(request.POST)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'createBean.html',context)
    else:
        form=BeanForm()
        context['form']=form
        return render(request, 'createBean.html', context)

def editBean(request, bean_id):
    context={}
    if not request.user.is_authenticated():
        return redirect('/admin')
    if not x.user.is_staff:
        return redirect('/admin')
    bean=Bean.objects.get(id=bean_id)
    context['bean']=bean
    if request.method=="POST":
        form=BeanForm(request.POST, instance=bean)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'editBean.html',context)
    else:
        form=BeanForm(instance=bean)
        context['form']=form
        return render(request, 'editBean.html', context)

def deleteBean(request, bean_id):
    if not request.user.is_authenticated():
        return redirect('/admin')
    if not request.user.is_staff:
        return redirect('/admin')
    Bean.objects.get(id=bean_id).delete()
    return redirect("home")



def createRoast(request):
    context={}
    if not request.user.is_authenticated():
        return redirect('/admin')
    if not request.user.is_staff:
        return redirect('/admin')
    if request.method=="POST":
        form=RoastForm(request.POST)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'createRoast.html',context)
    else:
        form=RoastForm()
        context['form']=form
        return render(request, 'createRoast.html', context)

def editRoast(request, roast_id):
    context={}
    if not request.user.is_authenticated():
        return redirect('/admin')
    if not request.user.is_staff:
        return redirect('/admin')
    roast=Roast.objects.get(id=roast_id)
    context['roast']=roast
    if request.method=="POST":
        form=RoastForm(request.POST, instance=roast)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'editRoast.html',context)
    else:
        form=RoastForm(instance=roast)
        context['form']=form
        return render(request, 'editRoast.html', context)

def deleteRoast(request, roast_id):
    if not request.user.is_authenticated():
        return redirect('/admin')
    if not request.user.is_staff:
        return redirect('/admin')
    Roast.objects.get(id=roast_id).delete()
    return redirect("home")



def createPowder(request):
    context={}
    if not request.user.is_authenticated():
        return redirect('/admin')
    if not request.user.is_staff:
        return redirect('/admin')
    if request.method=="POST":
        form=PowderForm(request.POST)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'createPowder.html',context)
    else:
        form=PowderForm()
        context['form']=form
        return render(request, 'createPowder.html', context)

def editPowder(request, powder_id):
    context={}
    if not requestx.user.is_authenticated():
        return redirect('/admin')
    if not request.user.is_staff:
        return redirect('/admin')
    powder=Powder.objects.get(id=powder_id)
    context['powder']=powder
    if request.method=="POST":
        form=PowderForm(request.POST, instance=powder)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'editPowder.html',context)
    else:
        form=PowderForm(instance=powder)
        context['form']=form
        return render(request, 'editPowder.html', context)

def deletePowder(request, powder_id):
    if not request.user.is_authenticated():
        return redirect('/admin')
    if not request.user.is_staff:
        return redirect('/admin')
    Powder.objects.get(id=powder_id).delete()
    return redirect("home")




def createSyrup(request):
    context={}
    if not request.user.is_authenticated():
        return redirect('/admin')
    if not request.user.is_staff:
        return redirect('/admin')
    if request.method=="POST":
        form=SyrupForm(request.POST)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'createSyrup.html',context)
    else:
        form=SyrupForm()
        context['form']=form
        return render(request, 'createSyrup.html', context)

def editSyrup(request, syrup_id):
    context={}
    if not request.user.is_authenticated():
        return redirect('/admin')
    if not request.user.is_staff:
        return redirect('/admin')
    syrup=Syrup.objects.get(id=syrup_id)
    context['syrup']=syrup
    if request.method=="POST":
        form=SyrupForm(request.POST, instance=syrup)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'editSyrup.html',context)
    else:
        form=SyrupForm(instance=syrup)
        context['form']=form
        return render(request, 'editSyrup.html', context)

def deleteSyrup(request, syrup_id):
    if not request.user.is_authenticated():
        return redirect('/admin')
    if not request.user.is_staff:
        return redirect('/admin')
    Syrup.objects.get(id=syrup_id).delete()
    return redirect("home")

def createOrder(request,coffee_id):
    context={}
    if not request.user.is_authenticated():
        return redirect('/accounts/github/login')
    coffee=Coffee.objects.get(id=coffee_id)
    context['coffee']=coffee
    if request.method=='POST':
        form=OrderForm(request.POST)
        context['form']=form
        if form.is_valid():
            order=form.save(commit=False)
            order.user=request.user
            order.coffee=coffee
            form.save()
            return redirect("home")
        else:
            return render(request, 'createOrder.html',context)
    else:
        form=OrderForm()
        context['form']=form
        return render(request, 'createOrder.html', context)

def user_list(request):
    context={}
    if not request.user.is_authenticated():
        return redirect('/admin')
    if not request.user.is_staff:
        return redirect('/admin')
    user_list=User.objects.all()
    context['user_list']=user_list
    return render(request, 'user_list.html', context)
#ggggg

def user_coffees(request, user_id):
    context={}
    if not request.user.is_authenticated():
        return redirect('/admin')
    if not request.user.is_staff:
        return redirect('/admin')
    user=User.objects.get(id=user_id)
    context['user']=user
    coffees=Coffee.objects.filter(user=user)
    context['coffees']=coffees
    return render(request, 'user_coffees.html', context)

def send_order_email(request, year, month, day):
    context={}
    if not request.user.is_authenticated():
        return redirect('/accounts/github/login')
    date=datetime.datetime.strptime('%s%s%s'%(year, month, day),"%Y%m%d").date()
    order_list=Order.objects.filter(user=request.user, date=date)
    subject="Noobs Caffee"
    message="Get your order..\n"
    for order in order_list:
        message +="%s, "%(order.coffee)
    send_mail(subject, message , settings.EMAIL_HOST_USER, ['a.naqi.07@hotmail.com'])
    return redirect('home')

def replicate_order(request, year, month, day):
    context={}
    if not request.user.is_authenticated():
        return redirect('/accounts/github/login')
    date=datetime.datetime.strptime('%s%s%s'%(year, month, day),"%Y%m%d").date()
    context['today']=date
    order_list=Order.objects.filter(user=request.user, date=date)
    if request.method=="POST":
        form =SearchForm(request.POST)
        context['form']=form
        if form.is_valid():
            obj=form.cleaned_data['date']
            for order in order_list:
                new_order=Order(user=order.user, coffee=order.coffee, date=obj)
                new_order.save()
            return redirect("home")
        else:
            return render(request,'replicate_order.html', context)
    else:
        form =SearchForm()
        context['form']=form
    return render(request,'replicate_order.html', context)
