from django import forms
from .models import Banking

class BankingForm(forms.ModelForm):
    class Meta:
        model = Banking
        fields = "__all__"
        widgets= {
            'dob': forms.DateInput(attrs={'type':'date'}),
            'address': forms.Textarea(attrs={'rows':5})
        }
