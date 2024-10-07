from django import forms
from .models import Study

class StudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = ['study_name', 'study_description', 'study_phase', 'sponsor_name']
        widgets = {
            'study_name': forms.TextInput(attrs={'class': 'study_name', 'placeholder': 'Enter study name'}),
            'study_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'study_phase': forms.Select(attrs={'class': 'form-control'}),
            'sponsor_name': forms.TextInput(attrs={'class': 'form-control sponder', 'placeholder': 'Enter sponsor name'}),
        }