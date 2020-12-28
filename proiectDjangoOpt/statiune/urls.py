from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('statiune/sign_up/',views.sign_up,name="sign-up"),
    path('statiune/logout/',views.logout_view,name="logout"),
    path('statiune/activitati_montane',views.activitati_montane,name="activitati_montane")
]
