from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Pensiune, Activitate, Restaurant, Camera, Transport
from .forms import PensiuneCreate, ActivitateCreate, RestaurantCreate, TransportCreate, CameraCreate, CerereRezervare
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView


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
'''
def cerereCazare(request):
    if request.method == "POST":
        form = CerereRezervare(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/cazare/show')
            except:
                pass
    else:
        form = CerereRezervare()
    return render(request,"cazare/adaugaRez.html",{'form':form})
'''
class CerereCazare(FormView):
    form_class = CerereRezervare
    template_name = 'cazare/adaugaRez.html'

    def form_valid(self, form):
        data = form.cleaned_data
        camere = Camera.objects.all()
        #verifica disponibilitate camere ->
        #raman relatie
        return redirect("/cazare/show")


def camera(request):
    if request.method == "POST":
        form = CameraCreate(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/cazare/showCamera')
            except:
                pass
    else:
        form = CameraCreate()
    return render(request,"cazare/indexCamera.html",{'form':form})

def showCamera(request):
    pensiuni = Camera.objects.all()
    return render(request,"cazare/showCamera.html",{'pensiuni':pensiuni})

def listaCompleta(request):
    pensiuni = Camera.objects.all()
    return render(request,"cazare/listaCompleta.html",{'pensiuni':pensiuni})

def listCamera(request):
    camere = Camera.objects.all()
    nr_total_pers = 0
    nr_total_camere = 0
    for camera in camere:
        nr_total_pers += camera.nr_persoane;
        nr_total_camere += 1;

    return render(request,"cazare/listCamera.html",{'pensiuni':camere, 'camere': nr_total_camere, 'pers': nr_total_pers});



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

def destroyCamera(request, id):
    pensiune = Camera.objects.get(id=id)
    pensiune.delete()
    return redirect('/cazare/showCamera')

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


def trans(request):
    if request.method == "POST":
        form = TransportCreate(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/transport/showTrans')
            except:
                pass
    else:
        form = TransportCreate()
    return render(request,"transport/indexTrans.html",{'form':form})

def showTrans(request):
    transporturi = Transport.objects.all()
    return render(request,"transport/showTrans.html",{'transporturi':transporturi})

def listTrans(request):
    transporturi = Transport.objects.all()
    return render(request,"transport/listTrans.html",{'transporturi':transporturi})

def editTrans(request, id):
    transport = Transport.objects.get(id=id)
    return render(request,'transport/editTrans.html', {'transport':transport})

def updateTrans(request, id):
    transport = Transport.objects.get(id=id)
    form = TransportCreate(request.POST, instance = transport)
    if form.is_valid():
        form.save()
        return redirect("transport/showTrans")
    return render(request, 'transport/editTrans.html', {'transport': transport})

def destroyTrans(request, id):
    transport = Transport.objects.get(id=id)
    transport.delete()
    return redirect('/transport/showTrans')
