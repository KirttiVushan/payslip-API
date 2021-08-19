from django.db import models

# Create your models here.

class Payslip(models.Model):

	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	pan_No = models.CharField(max_length=200)
	uan_No = models.CharField(max_length=200)
	basic_pay = models.IntegerField()
	benefits = models.IntegerField()
	taxes = models.IntegerField()

	def __str__(self):
		return self.name


	def tax_percent_calculate(self,*args,**kwargs):
		tax_percent = 1/10
		self.taxes = (self.taxes)*(tax_percent)
		super.save(*args,**kwargs)


	tax_percentage = property(tax_percent_calculate)
        