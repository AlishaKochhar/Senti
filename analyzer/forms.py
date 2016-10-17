from django import forms
from .models import EnterSenti

class EnterSentiForm(forms.ModelForm) :
    class Meta :
        model=EnterSenti
        fields=[
            'sentiment'
            ]
