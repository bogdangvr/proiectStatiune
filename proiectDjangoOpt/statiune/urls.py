from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('statiune/sign_up/',views.sign_up,name="sign-up"),
    path('statiune/logout/',views.logout_view,name="logout"),
    path('cazare/pens', views.pens),
    path('cazare/show', views.show),
    path('cazare/edit/<int:id>', views.edit),
    path('cazare/update/<int:id>', views.update),
    path('cazare/delete/<int:id>', views.destroy),
]
