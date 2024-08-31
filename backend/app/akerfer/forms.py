from django import forms
from .models import SushiCard

class SushiCardForm(forms.ModelForm):
    class Meta:
        model = SushiCard
        fields = ['title', 'description', 'price', 'sushi_type', 'image']