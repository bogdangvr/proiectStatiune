from django.contrib import admin
from django.urls import path
from . import views
from .views import HomePageView, AboutPageView, CerereCazare

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('statiune/sign_up/',views.sign_up,name="sign-up"),
    path('statiune/logout/',views.logout_view,name="logout"),
    path('cazare/pens', views.pens),
    #path('cazare/cerereCazare', views.cerereCazare),
    path('cazare/adaugaRez', CerereCazare.as_view(), name="cerere_cazare"),
    path('cazare/camera', views.camera),
    path('cazare/indisponibilitate', views.indisponibilitate),
    path('cazare/show', views.show),
    path('cazare/showRezervare', views.showRezervare),
    path('cazare/listCamera', views.listCamera),
    path('cazare/listaCompleta', views.listaCompleta),
    path('cazare/showCamera', views.showCamera),
    path('cazare/list', views.list),
    path('cazare/edit/<int:id>', views.edit),
    path('cazare/update/<int:id>', views.update),
    path('cazare/deleteCamera/<int:id>', views.destroyCamera),
    path('cazare/anuleazaRezervare/<int:id>', views.destroyRezervare),
    path('cazare/delete/<int:id>', views.destroy),
    path('activitati_montane/act', views.act),
    path('activitati_montane/show', views.showAct),
    path('activitati_montane/list', views.listAct),
    path('activitati_montane/edit/<int:id>', views.editAct),
    path('activitati_montane/update/<int:id>', views.updateAct),
    path('activitati_montane/delete/<int:id>', views.destroyAct),
    path('restaurant/rest', views.rest),
    path('restaurant/showRest', views.showRest),
    path('restaurant/listRest', views.listRest),
    path('restaurant/editRest/<int:id>', views.editRest),
    path('restaurant/updateRest/<int:id>', views.updateRest),
    path('restaurant/deleteRest/<int:id>', views.destroyRest),
]
