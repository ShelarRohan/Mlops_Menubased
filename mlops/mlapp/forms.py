from django import forms
from .models import *
from django.db import models

class Startup_Form(forms.ModelForm):

	class Meta:
		model = startup_info
		fields = ['rnd', 'admin', 'marketing', 'state']
		widgets = {
                'rnd':forms.TextInput(attrs={'class':'form-control'}),
                'admin':forms.TextInput(attrs={'class':'form-control'}),
                'marketing':forms.TextInput(attrs={'class':'form-control'}),
                'state':forms.TextInput(attrs={'class':'form-control'}),
                
		}

class Titanic_Form(forms.ModelForm):

	class Meta:
		model = titanic_info
		fields = ['passenger_class', 'sex', 'age', 'no_sibling', 'parch', 'fare_amt','embarc_c','embarc_q','embarc_s']
		widgets = {
                'passenger_class':forms.TextInput(attrs={'class':'form-control'}),
                'sex':forms.TextInput(attrs={'class':'form-control'}),
                'age':forms.TextInput(attrs={'class':'form-control'}),
                'no_sibling':forms.TextInput(attrs={'class':'form-control'}),
                'parch':forms.TextInput(attrs={'class':'form-control'}),
                'fare_amt':forms.TextInput(attrs={'class':'form-control'}),
                'embarc_c':forms.TextInput(attrs={'class':'form-control'}),
                'embarc_q':forms.TextInput(attrs={'class':'form-control'}),
                'embarc_s':forms.TextInput(attrs={'class':'form-control'}),
                
		}
  
class Catdog_Form(forms.ModelForm):
        class Meta:
                model = dogcat_info
                fields = ['image']

class Wine_Form(forms.ModelForm):

	class Meta:
		model = wine_info
		fields = ['alcohol', 'malic_acid', 'ash', 'acl', 'mg', 'phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanth', 'color_int', 'hue', 'od', 'proline']
		widgets = {
                'alcohol':forms.TextInput(attrs={'class':'form-control'}),
                'malic_acid':forms.TextInput(attrs={'class':'form-control'}),
                'ash':forms.TextInput(attrs={'class':'form-control'}),
                'acl ':forms.TextInput(attrs={'class':'form-control'}),
                'mg':forms.TextInput(attrs={'class':'form-control'}),
                'phenols':forms.TextInput(attrs={'class':'form-control'}),
                'flavanoids':forms.TextInput(attrs={'class':'form-control'}),
                'nonflavanoid_phenols':forms.TextInput(attrs={'class':'form-control'}),
                'proanth':forms.TextInput(attrs={'class':'form-control'}),
                'color_int':forms.TextInput(attrs={'class':'form-control'}),
                'hue':forms.TextInput(attrs={'class':'form-control'}),
                'od':forms.TextInput(attrs={'class':'form-control'}),
                'proline':forms.TextInput(attrs={'class':'form-control'}),
                
		}
