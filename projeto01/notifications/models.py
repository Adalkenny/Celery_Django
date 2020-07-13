from django.db import models

# Create your models here.

class Livro(models.Model):

	titulo = models.CharField(max_length=100)
	subtitulo = models.CharField(max_length=200)
	autor = models.CharField(max_length=200)
	presso = models.FloatField()
	data_publicacao = models.DateField(auto_now_add=True)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return self.titulo

