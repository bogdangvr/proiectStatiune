from django import forms
from .models import Pensiune
#DataFlair
class PensiuneCreate(forms.ModelForm):

    class Meta:
        model = Pensiune
        fields = '__all__'