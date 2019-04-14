from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
# from django_filters.rest_framework import DjangoFilterBackend
# from django_filters import FilterSet
# from django_filters import rest_framework as filters
# from rest_framework.filters import OrderingFilter,SearchFilter

from .models import Customer
from .serializer import CustomerSerializer
# from rest_framework.decorators import action
# from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from django.db.models import Count


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_field = 'id'