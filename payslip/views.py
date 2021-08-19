from . serializers import PayslipSerializer
from . models import Payslip
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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





class PayslipAPI(APIView):

	

# 1. Add API to add users with above mentioned Fields
	def post(self, request,format=None):

		if request.method == 'POST':

			serializer = PayslipSerializer(data = request.data)
			
		if serializer.is_valid():

			serializer.save()
			return Response({'msg':'data created'} , status=status.HTTP_201_CREATED)

		return Response(serializer.errors)


# 2. Add API to update fields
	def put(self, request ,pk,format=None):

		if request.method == 'PUT':

			payslip = Payslip.objects.get(id=id)
			serializer = PayslipSerializer(payslip , data=request.data)
		
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'data updated completely'})
		return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

# 3. Add API to get user with tax amount less than 10000 rupees.

	def get(self,request,pk=None,format=None):

		if request.method == 'GET':

			names = Payslip.objects.filter(taxes__lte=10000)
			serializer = PayslipSerializer(names , many=True)
			return Response(serializer.data)

		return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)



# 4. Update tax percentage

	def update_tax_percentage(self,request,pk=None,format=None):

		pass
	


# 5. Compute new taxes for all users after taxation percentage change.
# 6. Notify users for taxation percentage change.