from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Pensiune, Activitate, Restaurant
from .forms import PensiuneCreate, ActivitateCreate, RestaurantCreate
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'statiune/home.html'

class AboutPageView(TemplateView): # new
    template_name = 'statiune/about.html'

@login_required
def index(request):
    return render(request,'statiune/index.html'
                          '')
def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'statiune/index.html')
    context['form']=form
    return render(request,'registration/sign_up.html',context)

def logout_view(request):
    logout(request)
    return render(request,'registration/logged_out.html'
                          '')

def pens(request):
    if request.method == "POST":
        form = PensiuneCreate(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/cazare/show')
            except:
                pass
    else:
        form = PensiuneCreate()
    return render(request,"cazare/index.html",{'form':form})

def show(request):
    pensiuni = Pensiune.objects.all()
    return render(request,"cazare/show.html",{'pensiuni':pensiuni})

def list(request):
    pensiuni = Pensiune.objects.all()
    return render(request,"cazare/list.html",{'pensiuni':pensiuni})

def edit(request, id):
    pensiune = Pensiune.objects.get(id=id)
    return render(request,'cazare/edit.html', {'pensiune':pensiune})

def update(request, id):
    pensiune = Pensiune.objects.get(id=id)
    form = PensiuneCreate(request.POST, instance = pensiune)
    if form.is_valid():
        form.save()
        return redirect("cazare/show")
    return render(request, 'cazare/edit.html', {'pensiune': pensiune})

def destroy(request, id):
    pensiune = Pensiune.objects.get(id=id)
    pensiune.delete()
    return redirect('/cazare/show')

def act(request):
    if request.method == "POST":
        form = ActivitateCreate(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/activitati_montane/show')
            except:
                pass
    else:
        form = ActivitateCreate()
    return render(request,"activitati_montane/index.html",{'form':form})

def showAct(request):
    activitati = Activitate.objects.all()
    return render(request,"activitati_montane/show.html",{'activitati':activitati})

def listAct(request):
    activitati = Activitate.objects.all()
    return render(request,"activitati_montane/list.html",{'activitati':activitati})

def editAct(request, id):
    activitate = Activitate.objects.get(id=id)
    return render(request,'activitati_montane/edit.html', {'activitate':activitate})

def updateAct(request, id):
    activitate = Activitate.objects.get(id=id)
    form = PensiuneCreate(request.POST, instance = activitate)
    if form.is_valid():
        form.save()
        return redirect("activitati_montane/show")
    return render(request, 'activitati_montane/edit.html', {'activitate':activitate})

def destroyAct(request, id):
    activitate = Activitate.objects.get(id=id)
    activitate.delete()
    return redirect('/activitati_montane/show')

def rest(request):
    if request.method == "POST":
        form = RestaurantCreate(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/restaurant/showRest')
            except:
                pass
    else:
        form = RestaurantCreate()
    return render(request,"restaurant/indexRest.html",{'form':form})

def showRest(request):
    restaurante = Restaurant.objects.all()
    return render(request,"restaurant/showRest.html",{'restaurante':restaurante})

def listRest(request):
    restaurante = Restaurant.objects.all()
    return render(request,"restaurant/listRest.html",{'restaurante':restaurante})

def editRest(request, id):
    restaurant = Restaurant.objects.get(id=id)
    return render(request,'restaurant/editRest.html', {'restaurant':restaurant})

def updateRest(request, id):
    restaurant = Restaurant.objects.get(id=id)
    form = RestaurantCreate(request.POST, instance = restaurant)
    if form.is_valid():
        form.save()
        return redirect("restaurant/showRest")
    return render(request, 'restaurant/editRest.html', {'restaurant': restaurant})

def destroyRest(request, id):
    restaurant = Restaurant.objects.get(id=id)
    restaurant.delete()
    return redirect('/restaurant/showRest')
