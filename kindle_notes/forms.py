from django import forms
from kindle_notes.models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('highlight', 'note', 'location', 'page')
        widgets = {
                'highlight': forms.Textarea(attrs={'class': 'form-control', 
                                                   'rows': 3,
                                                   'placeholder': 'Highlighted Text'}),
                'note': forms.Textarea(attrs={'class': 'form-control',
                                              'rows': 3,
                                              'placeholder': 'Note Text'}),
                'location': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Location'}),
                'page': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Page'}),
                }
