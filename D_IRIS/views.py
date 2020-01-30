from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LkMercadoSerializer, ValidaFtAggSerializer
from .models import LkMercado, Validaftagg

class LkMercadoView(viewsets.ModelViewSet):
	serializer_class = LkMercadoSerializer
	queryset = LkMercado.objects.all()

class ValidaFtAggView(viewsets.ModelViewSet):
	serializer_class = ValidaFtAggSerializer
	queryset = Validaftagg.objects.all()