from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

class BilledProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BilledProduct
        exclude = ['bill']
        read_only_fields = ['price']




class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from django.core import exceptions
from django.utils.translation import gettext_lazy as _


class EmployeeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)


    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.is_staff = True
        user.save()
        return user

class BillSerializer(serializers.ModelSerializer):
    billedProduct = BilledProductSerializer(many = True)
    employee = serializers.PrimaryKeyRelatedField(queryset = User.objects.filter(is_staff=True))
    customer = serializers.PrimaryKeyRelatedField(queryset = User.objects.filter(is_staff=False))


    class Meta:
        model = models.Bill
        fields = '__all__'
        read_only_fields = ['total']

    def create(self, validated_data):
        bill = models.Bill(
            employee = validated_data['employee'],
            customer = validated_data['customer'])
        bill.save()
        billedProducts = validated_data['billedProduct']
        for product in billedProducts:
            productObj = product['product']
            obj = models.BilledProduct(
                product = productObj,
                bill = bill,
                quantity = product['quantity']
            )
            obj.save()
            bill.total += obj.price
            bill.save()
            productObj.inStockQuantity -= product['quantity']
            productObj.save()
        return bill
    def update(self, instance, validated_data):
        pass
        


    
