from rest_framework.response import Response
from . serializers import PayslipSerializer
from . models import Payslip
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (ListModelMixin , 
	CreateModelMixin , 
	RetrieveModelMixin , 
	UpdateModelMixin , 
	DestroyModelMixin)
import json
# Create your views here.
# Fields in the PAYSLIP
# - Name
# - Address
# - PAN No
# - UAN No
# - Basic pay
# - Benefits
# - Taxes
# Tax percentage: 10%
# 1. Add API to add users with above mentioned Fields
# 2. Add API to update fields
# 3. Add API to get user with tax amount less than 10000 rupees.
# 4. Update tax percentage
# 5. Compute new taxes for all users after taxation percentage change.
# 6. Notify users for taxation percentage change.



class PayslipFunc(GenericAPIView , CreateModelMixin):


	query_set = Payslip.objects.all()
	serializer_class = PayslipSerializer

	def post(self, request, *args , **kwargs):
		return self.create(request , *args , **kwargs)



		
		
class APIUpdateFields(GenericAPIView , UpdateModelMixin):

	query_set = Payslip.objects.all()
	serializer_class = PayslipSerializer


	def put(self, *args , **kwargs):
		return self.put(request, *args , **kwargs)
		
		



	# def tax_amount_less_thousand(mixins.RetrieveModelMixin):
		
	# 	users_less_tax=[]
	# 	payslip = Payslip.Objects.all()
	# 	payslip = payslip.json()
		
	# 	for users in payslip:

	# 		if users['Taxes'] < 10000:
	# 			users_less_tax.append(users['Taxes'])

	# 	return Response(users_less_tax)







	# def update_tax_percentage(self, *args , **kwargs):
		
	# 	new_tax_percent = request.data.get('percentage')
	# 	payslip = Payslip.objects.all()
	# 	payslip.tax_rate = 

	# def taxation_change(self, *args , **kwargs):
	# 	pass

	# def notify_tax_chng(self, *args , **kwargs):
	# 	pass

