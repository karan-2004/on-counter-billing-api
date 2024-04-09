from rest_framework import viewsets
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout as userLogout
from rest_framework.response import Response
from . import serializers
from . import models
from .perms import IsAdmin
from rest_framework import serializers as restSerializers


def logout(request):
     userLogout(request)
     return redirect('index')

# Create your views here.
class ProductViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    lookup_field = 'productName'

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer_class()
        data = serializer(queryset, many=True).data
        return Response([datum['productName'] for datum in data])
    
class BillViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BillSerializer
    queryset = models.Bill.objects.all()
    lookup_field = 'id'

class BilledProductViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BilledProductSerializer
    queryset = models.BilledProduct.objects.all()
    lookup_field = 'id'

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=0)
    serializer_class = serializers.CustomerSerializer
    lookup_field = 'username'

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=1)
    serializer_class = serializers.EmployeeSerializer
    lookup_field = 'username'
    permission_classes = [IsAdmin]

    

