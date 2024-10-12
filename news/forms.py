from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title','anons','full_text','date']

        widgets = {
            "title":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Заңның аты',
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс',
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст заң',
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Жаслған күні'
            }),
        }