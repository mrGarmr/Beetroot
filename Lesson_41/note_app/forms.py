from datetime import datetime
from django import forms

from notes.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'reminder', 'category']
        widgets = {
            'reminder': forms.DateInput(attrs={
                'type': 'datetime-local', 
                'value': datetime.now().strftime("%d.%m.%Y %H:%M"),},),}