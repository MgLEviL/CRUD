from django.db import models
from django.utils import timezone

# Create your models here.
class UserNote(models.Model):
    name = models.CharField(max_length=30, default="", verbose_name='Nombre')
    email = models.EmailField(max_length=150, default="", blank=True, verbose_name='Email')

    def __str__(self):
        return self.name

OPTIONS = (
	('A', 'Ejemplo 1'),
	('B', 'Ejemplo 2'),
	)

class Note(models.Model):
	date = models.DateTimeField(default=timezone.now, verbose_name='Fecha y hora actual')
	end_date = models.DateField(verbose_name='Selector de fecha')
	note = models.TextField(blank=True, verbose_name='Nota')
	attach = models.FileField(blank=True, verbose_name='Adjunto')
	user = models.ForeignKey(UserNote, on_delete=models.CASCADE)
	task = models.BooleanField(verbose_name='Tarea')
	tag = models.CharField(max_length=40, verbose_name='Etiqueta')
	type = models.CharField(max_length=1, choices=OPTIONS)

	def __str__(self):
		return self.note