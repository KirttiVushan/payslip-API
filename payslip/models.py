from django.db import models

# Create your models here.

class Payslip(models.Model):

	Name = models.CharField(max_length=200)
	Address = models.CharField(max_length=200)
	PAN_No = models.CharField(max_length=200)
	UAN_No = models.CharField(max_length=200)
	Basic_pay = models.CharField(max_length=200)
	Benefits = models.CharField(max_length=200)
	Taxes = models.IntegerField(max_length=200)

	def tax_rate(self,Taxes):
		return (self.Taxes//10)*100 