from django.contrib import admin

from .models import LkMercado, Validaftagg

class LkMercadoAdmin(admin.ModelAdmin):
	list_display = ('merc_lid', 'merc_desc')

class ValidaFtAggAdmin(admin.ModelAdmin):
	list_display = ('id_dia', 'tabla', 'llamadas_atendidas', 'llamadas_recibidas', 'q_plataforma')
		

admin.site.register(LkMercado, LkMercadoAdmin)