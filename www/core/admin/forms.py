from django import forms
from core.models import Excel


class ExcelForm(forms.ModelForm):
    class Meta:
        model = Excel
        fields = '__all__'
