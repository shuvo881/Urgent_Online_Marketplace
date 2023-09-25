from django import forms
from .models import Conversation, ConversationMessages


class ConversationMessagesForm(forms.ModelForm):
    class Meta:
        model = ConversationMessages
        fields = ('content', )

        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-3/4 ml-20 px-40 py-4 rounded-xl border'
            })
        }