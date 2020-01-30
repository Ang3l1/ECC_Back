from rest_framework import serializers
from .models import LkMercado, Validaftagg

class LkMercadoSerializer(serializers.ModelSerializer):
	class Meta:
		model = LkMercado
		fields = ('merc_lid', 'merc_desc')

class ValidaFtAggSerializer(serializers.ModelSerializer):
	class Meta:
		model = Validaftagg
		fields = ('id_dia', 'tabla', 'llamadas_atendidas', 'llamadas_recibidas', 'q_plataforma')