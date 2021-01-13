from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy

from .models import Pensiune, Activitate, Restaurant, Camera, Transport, RezervareCamere, Eveniment, RezervareEveniment
from .forms import PensiuneCreate, ActivitateCreate, RestaurantCreate, TransportCreate, CameraCreate, CerereRezervare
from .forms import CerereEveniment
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from django.contrib.auth import get_user_model
from django.views.generic import (
    TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'statiune/home.html'

class AboutPageView(TemplateView): # new
    template_name = 'statiune/about.html'

class RegisterView(CreateView):
    template_name= 'registration/register.html'
    form_class = UserCreationForm
    model = User

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(username=data['username'],
                                        password=data['password1'])
        return redirect('/')

class LoginView(TemplateView):
    template_name = 'registration/login.html'

    def get_context_data(self):
        form = AuthenticationForm()
        return {'form': form}

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'],
                                password=data['password'])
            login(request, user)
            return redirect(reverse_lazy('post_list'))
        else:
            return render(request, "login.html", {"form": form})

@login_required
def index(request):
    return render(request,'statiune/index.html'
                          '')

def logout_view(request):
    logout(request)
    return render(request,'statiune/home.html'
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

def camera_disp(check_in,check_out,camera_complex):
    rezervariActuale = RezervareEveniment.objects.all()
    for rezervare in rezervariActuale:
        #lista_camere = rezervariActuale.camereRezervate;
        #if (camera_complex in lista_camere):
        if rezervare in listRestaurant().rezervarecamere_set.all():
            if (check_in >= rezervare.check_in and check_in <= rezervare.check_out) or (check_out > rezervare.check_in and check_out <= rezervare.check_out) :
                return False;
    return True;

class CerereCazare(FormView):
    form_class = CerereRezervare
    template_name = 'cazare/adaugaRez.html'

    def form_valid(self, form):
        data = form.cleaned_data
        camere = Camera.objects.all()
        numar_camere_dorite = data['numar_camere_dorite']
        check_in = data['data_start']
        check_out = data['data_final']
        print(numar_camere_dorite)
        #verifica disponibilitate camere ->
        #raman relatie
        rezerv = []
        for camera_complex in camere:
            if camera_disp(check_in,check_out,camera_complex) == True :
                rezerv.append(camera_complex)
        if (len(rezerv) >= numar_camere_dorite):
            rezervare1 = RezervareCamere.objects.create(nume = data['nume'],
                                         prenume = data['prenume'],
                                         telefon = data['telefon'],
                                         adresaMail = data['adresaMail'],
                                         check_in = check_in,
                                         check_out = check_out,
                                         numar_camere = numar_camere_dorite
                                         )
            rezervare1.save()
            for i in range(numar_camere_dorite):
                rezervare1.camereRezervate.add(rezerv[i])
            return redirect("/cazare/showRezervare")
        else:
            return redirect("/cazare/indisponibilitate")
        return redirect("restaurant/listRest")

def indisponibilitate(request):
    return render(request,"cazare/indisponibilitate.html",{})

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

def showRezervare(request):
    user = request.user.get_username()
    rezervari = RezervareCamere.objects.all()
    rezervariUser = []
    for rezervare in rezervari:
        if rezervare.adresaMail == user:
            rezervariUser.append(rezervare)
    return render(request,"cazare/showRezervare.html",{'rezervari':rezervariUser, 'user': user})

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

def destroyRezervare(request, id):
    rez = RezervareCamere.objects.get(id=id)
    rez.delete()
    return redirect('/cazare/showRezervare')

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

def listRestaurant(request):
    evenimente = Eveniment.objects.all()
    return render(request,"restaurant/listRestaurant.html",{'evenimente':evenimente})

class CerereEveniment(FormView):
    form_class = CerereEveniment
    template_name = 'restaurant/adaugaRezEveniment.html'

    def form_valid(self, form):
        data = form.cleaned_data
        restaurante = Restaurant.objects.all()
        numar_persoane_dorite = data['numar_persoane_dorite']
        data = data['data_start']
        print(numar_persoane_dorite )
        #verifica disponibilitate restaurant ->
        #raman relatie
        rezerv = []
        for restaurant in restaurante:
            if camera_disp(data,restaurant) == True :
                rezerv.append(restaurant)
            rezervare1 = RezervareEveniment.objects.create(nume = data['nume'],
                                         prenume = data['prenume'],
                                         telefon = data['telefon'],
                                         adresaMail = data['adresaMail'],
                                         data_dorita = data['data_dorita'],
                                         numar_persoane = numar_persoane_dorite
                                         )
            rezervare1.save()
            for i in range(numar_persoane_dorite):
                rezervare1.camereRezervate.add(rezerv[i])
            return redirect("/restaurant/showRezervare")
        else:
            return redirect("/restaurant/indisponibilitate")
        return redirect("restaurant/listRest")


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
