from django.db import models

class LkClientePlataforma(models.Model):
    clnt_lid = models.BigIntegerField(primary_key=True)
    clnt_rut = models.CharField(max_length=30)
    clnt_rzn_social = models.CharField(max_length=50)
    vert_lid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lk_cliente_plataforma'


class LkHabilidad(models.Model):
    habl_lid = models.BigIntegerField(primary_key=True)
    habl_id = models.BigIntegerField()
    habl_dsc = models.CharField(max_length=40)
    srvc_lid = models.BigIntegerField()
    habl_fch_ini = models.DateField()
    habl_fch_fin = models.DateField(blank=True, null=True)
    id_plataforma = models.BigIntegerField(blank=True, null=True)
    vq = models.BigIntegerField(blank=True, null=True)
    id_agrupacion = models.BigIntegerField(blank=True, null=True)
    id_plataforma_entel = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lk_habilidad'


class LkMercado(models.Model):
    merc_lid = models.BigIntegerField(primary_key=True)
    merc_desc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lk_mercado'

    def __str__(self):
        return self.merc_lid


class LkPlataforma(models.Model):
    id_plataforma = models.BigIntegerField(primary_key=True)
    desc_plataforma = models.CharField(max_length=150, blank=True, null=True)
    clnt_lid = models.BigIntegerField(blank=True, null=True)
    sntd_trafico = models.CharField(max_length=20, blank=True, null=True)
    estado = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lk_plataforma'


class LkVertical(models.Model):
    vert_lid = models.BigIntegerField(primary_key=True)
    vert_desc = models.CharField(max_length=50, blank=True, null=True)
    vert_fch_ini = models.DateField(blank=True, null=True)
    merc_lid = models.BigIntegerField(blank=True, null=True)
    vert_fch_fin = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lk_vertical'


class TbIndicadoresAgente(models.Model):
    id_indicador = models.BigIntegerField(primary_key=True)
    rut_agente = models.BigIntegerField(blank=True, null=True)
    id_mes = models.FloatField(blank=True, null=True)
    nf_calidad = models.FloatField(blank=True, null=True)
    sn_epa = models.FloatField(blank=True, null=True)
    adherencia_real = models.FloatField(blank=True, null=True)
    tmo = models.FloatField(blank=True, null=True)
    id_dia = models.FloatField(blank=True, null=True)
    id_semana = models.FloatField(blank=True, null=True)
    id_plataforma = models.FloatField(blank=True, null=True)
    nota_calidad = models.FloatField(blank=True, null=True)
    pec = models.FloatField(blank=True, null=True)
    penc = models.FloatField(blank=True, null=True)
    epa_buenas = models.FloatField(blank=True, null=True)
    epa_malas = models.FloatField(blank=True, null=True)
    epa_neutras = models.FloatField(blank=True, null=True)
    llamadas_atendidas = models.FloatField(blank=True, null=True)
    minutos_hablados = models.FloatField(blank=True, null=True)
    adherencia_numerador = models.FloatField(blank=True, null=True)
    adherencia_denominador = models.FloatField(blank=True, null=True)
    tiempo_login = models.FloatField(blank=True, null=True)
    gestiones = models.FloatField(blank=True, null=True)
    tmo_obj = models.FloatField(blank=True, null=True)
    tc_obj = models.FloatField(blank=True, null=True)
    nota_calidad_obj = models.FloatField(blank=True, null=True)
    sn_epa_obj = models.FloatField(blank=True, null=True)
    pec_obj = models.FloatField(blank=True, null=True)
    penc_obj = models.FloatField(blank=True, null=True)
    adherencia_obj = models.FloatField(blank=True, null=True)
    ocupacion_obj = models.FloatField(blank=True, null=True)
    ventas = models.FloatField(blank=True, null=True)
    montos = models.FloatField(blank=True, null=True)
    atend_sc = models.FloatField(blank=True, null=True)
    llamadas_recibidas = models.FloatField(blank=True, null=True)
    base_recorrida = models.FloatField(blank=True, null=True)
    c_efectivos = models.FloatField(blank=True, null=True)
    c_no_valido = models.FloatField(blank=True, null=True)
    no_contesta = models.FloatField(blank=True, null=True)
    monto_cursado = models.FloatField(blank=True, null=True)
    licencias = models.FloatField(blank=True, null=True)
    ausencias = models.FloatField(blank=True, null=True)
    vacaciones = models.FloatField(blank=True, null=True)
    atrasos = models.FloatField(blank=True, null=True)
    llamadas_contactadas = models.FloatField(blank=True, null=True)
    llamadas_emitidas = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_indicadores_agente'


class TodoTodo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'todo_todo'


class Validaftagg(models.Model):
    id_dia = models.DateField(blank=True, null=True)
    tabla = models.CharField(max_length=10, blank=True, null=True)
    llamadas_atendidas = models.BigIntegerField(blank=True, null=True)
    q_plataforma = models.BigIntegerField(blank=True, null=True)
    llamadas_recibidas = models.IntegerField(blank=True, null=True)
    id_valida = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'validaftagg'