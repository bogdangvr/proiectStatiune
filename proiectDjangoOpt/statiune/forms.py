from django import forms
from .models import Pensiune, Activitate, Restaurant, Camera, RezervareCamere, Transport


#DataFlair
class PensiuneCreate(forms.ModelForm):

    class Meta:
        model = Pensiune
        fields = '__all__'

class CameraCreate(forms.ModelForm):

    class Meta:
        model = Camera
        fields = '__all__'

class CerereRezervare(forms.Form):
    nume =forms.CharField(required=True, max_length=100)
    prenume =forms.CharField(required=True, max_length=100)
    adresaMail =forms.CharField(required=True, max_length=100)
    telefon = forms.CharField(required=True, max_length=100)
    data_start = forms.DateTimeField(required=True, input_formats=["%Y-%m-%d", ])
    data_final = forms.DateTimeField(required=True, input_formats=["%Y-%m-%d", ])
    numar_camere_dorite = forms.IntegerField(required=True)

class ActivitateCreate(forms.ModelForm):

    class Meta:
        model = Activitate
        fields = '__all__'

class RestaurantCreate(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = '__all__'

class TransportCreate(forms.ModelForm):

    class Meta:
        model = Transport
        fields = '__all__'
