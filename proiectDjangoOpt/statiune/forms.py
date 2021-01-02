from django import forms
from .models import Pensiune, Activitate


#DataFlair
class PensiuneCreate(forms.ModelForm):

    class Meta:
        model = Pensiune
        fields = '__all__'

class ActivitateCreate(forms.ModelForm):

    class Meta:
        model = Activitate
        fields = '__all__'