from django.db import models
from django.utils import timezone

# Create your models here.



class Operator(models.Model):
	Telcos = models.CharField(max_length = 50)
	def __str__(self):
		return self.Telcos

class SIM(models.Model):
	operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
	number = models.CharField(max_length = 11)
	price = models.CharField(max_length = 20)
	status = models.CharField(max_length = 10)
	def __str__(self):
		return self.number

