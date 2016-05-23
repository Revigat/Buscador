from django.db import models

# Create your models here.

class Empresa (models.Model):
	id = models.IntegerField(primary_key=True)
	nome = models.CharField(max_length=256)
	tipo = models.CharField(max_length=256)

	def __str__(self):
		return self.nome

		