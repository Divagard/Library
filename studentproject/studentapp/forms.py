from django import forms
from studentapp.models import stud_det,stud_fee

class stud_form(forms.ModelForm):
    class Meta:
        model = stud_det
        fields = '__all__'
        

class stud_fees(forms.ModelForm):
    class Meta:
        model = stud_fee
        fields = '__all__'
        
        