from .models import applicant
from django.forms import ModelForm
from django import forms

class applicationForm(forms.ModelForm):
    linkedin = forms.URLField(required=False)
    github = forms.URLField(required=False)
    class Meta:
        model= applicant
        fields =['first_name','last_name','email','number','linkedin','github','position','about_me']