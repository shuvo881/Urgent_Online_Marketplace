from django import forms
from django.contrib.auth.models import User


INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl'


class Form_profile_edit(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
        widgets = {

            'username': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'first_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

            'last_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
