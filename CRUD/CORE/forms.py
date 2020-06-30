from django import forms
from .models import Note, OPTIONS

#Clase usada para el formilario del modelo Note
class NoteForm(forms.ModelForm):
	end_date = forms.DateField(label='Fecha fin', required=True, widget=forms.TextInput(attrs={'type':'date', 'placeholder': 'Fecha fin'}))
	note = forms.CharField(label=False, widget=forms.Textarea(attrs={'cols' : "49", 'rows': "5", 'placeholder': 'Información de la nota aquí', }), required=True)
	attach = forms.FileField(label="Adjunto", required=False)
	task = forms.BooleanField(label="Tarea", required=False)
	tag = forms.CharField(label=False, required=True, widget=forms.TextInput(attrs={'placeholder': 'Etiqueta'}))
	type = forms.ChoiceField(label="Tipo", choices=OPTIONS, required=True)

	class Meta:
		model = Note
		fields = ('end_date', 'note', 'attach', 'task', 'tag', 'type', 'user',)