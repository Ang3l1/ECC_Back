# Generated by Django 3.0.2 on 2020-01-29 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LkClientePlataforma',
            fields=[
                ('clnt_lid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('clnt_rut', models.CharField(max_length=30)),
                ('clnt_rzn_social', models.CharField(max_length=50)),
                ('vert_lid', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lk_cliente_plataforma',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LkHabilidad',
            fields=[
                ('habl_lid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('habl_id', models.BigIntegerField()),
                ('habl_dsc', models.CharField(max_length=40)),
                ('srvc_lid', models.BigIntegerField()),
                ('habl_fch_ini', models.DateField()),
                ('habl_fch_fin', models.DateField(blank=True, null=True)),
                ('id_plataforma', models.BigIntegerField(blank=True, null=True)),
                ('vq', models.BigIntegerField(blank=True, null=True)),
                ('id_agrupacion', models.BigIntegerField(blank=True, null=True)),
                ('id_plataforma_entel', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lk_habilidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LkPlataforma',
            fields=[
                ('id_plataforma', models.BigIntegerField(primary_key=True, serialize=False)),
                ('desc_plataforma', models.CharField(blank=True, max_length=150, null=True)),
                ('clnt_lid', models.BigIntegerField(blank=True, null=True)),
                ('sntd_trafico', models.CharField(blank=True, max_length=20, null=True)),
                ('estado', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lk_plataforma',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LkVertical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vert_lid', models.BigIntegerField()),
                ('vert_desc', models.CharField(blank=True, max_length=50, null=True)),
                ('vert_fch_ini', models.DateField(blank=True, null=True)),
                ('merc_lid', models.BigIntegerField(blank=True, null=True)),
                ('vert_fch_fin', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lk_vertical',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbIndicadoresAgente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut_agente', models.BigIntegerField(blank=True, null=True)),
                ('id_mes', models.FloatField(blank=True, null=True)),
                ('nf_calidad', models.FloatField(blank=True, null=True)),
                ('sn_epa', models.FloatField(blank=True, null=True)),
                ('adherencia_real', models.FloatField(blank=True, null=True)),
                ('tmo', models.FloatField(blank=True, null=True)),
                ('id_dia', models.FloatField(blank=True, null=True)),
                ('id_semana', models.FloatField(blank=True, null=True)),
                ('id_plataforma', models.FloatField(blank=True, null=True)),
                ('nota_calidad', models.FloatField(blank=True, null=True)),
                ('pec', models.FloatField(blank=True, null=True)),
                ('penc', models.FloatField(blank=True, null=True)),
                ('epa_buenas', models.FloatField(blank=True, null=True)),
                ('epa_malas', models.FloatField(blank=True, null=True)),
                ('epa_neutras', models.FloatField(blank=True, null=True)),
                ('llamadas_atendidas', models.FloatField(blank=True, null=True)),
                ('minutos_hablados', models.FloatField(blank=True, null=True)),
                ('adherencia_numerador', models.FloatField(blank=True, null=True)),
                ('adherencia_denominador', models.FloatField(blank=True, null=True)),
                ('tiempo_login', models.FloatField(blank=True, null=True)),
                ('gestiones', models.FloatField(blank=True, null=True)),
                ('tmo_obj', models.FloatField(blank=True, null=True)),
                ('tc_obj', models.FloatField(blank=True, null=True)),
                ('nota_calidad_obj', models.FloatField(blank=True, null=True)),
                ('sn_epa_obj', models.FloatField(blank=True, null=True)),
                ('pec_obj', models.FloatField(blank=True, null=True)),
                ('penc_obj', models.FloatField(blank=True, null=True)),
                ('adherencia_obj', models.FloatField(blank=True, null=True)),
                ('ocupacion_obj', models.FloatField(blank=True, null=True)),
                ('ventas', models.FloatField(blank=True, null=True)),
                ('montos', models.FloatField(blank=True, null=True)),
                ('atend_sc', models.FloatField(blank=True, null=True)),
                ('llamadas_recibidas', models.FloatField(blank=True, null=True)),
                ('base_recorrida', models.FloatField(blank=True, null=True)),
                ('c_efectivos', models.FloatField(blank=True, null=True)),
                ('c_no_valido', models.FloatField(blank=True, null=True)),
                ('no_contesta', models.FloatField(blank=True, null=True)),
                ('monto_cursado', models.FloatField(blank=True, null=True)),
                ('licencias', models.FloatField(blank=True, null=True)),
                ('ausencias', models.FloatField(blank=True, null=True)),
                ('vacaciones', models.FloatField(blank=True, null=True)),
                ('atrasos', models.FloatField(blank=True, null=True)),
                ('llamadas_contactadas', models.FloatField(blank=True, null=True)),
                ('llamadas_emitidas', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tb_indicadores_agente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TodoTodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('completed', models.BooleanField()),
            ],
            options={
                'db_table': 'todo_todo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Validaftagg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_dia', models.DateField(blank=True, null=True)),
                ('tabla', models.CharField(blank=True, max_length=10, null=True)),
                ('llamadas_atendidas', models.BigIntegerField(blank=True, null=True)),
                ('q_plataforma', models.BigIntegerField(blank=True, null=True)),
                ('llamadas_recibidas', models.IntegerField(blank=True, null=True)),
                ('id_valida', models.BigIntegerField()),
            ],
            options={
                'db_table': 'validaftagg',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LkMercado',
            fields=[
                ('merc_lid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('merc_desc', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'lk_mercado',
                'managed': True,
            },
        ),
    ]
