# Generated by Django 2.1.2 on 2018-11-26 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('envios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='envio',
            name='ciudad_des',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ciudad del destinatario'),
        ),
        migrations.AddField(
            model_name='envio',
            name='ciudad_rem',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ciudad del remitente'),
        ),
        migrations.AddField(
            model_name='envio',
            name='codigo_pais_des_id',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Codigo Pais Destinatario'),
        ),
        migrations.AddField(
            model_name='envio',
            name='codigo_pais_rem',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Codigo Pais Remitente'),
        ),
        migrations.AddField(
            model_name='envio',
            name='codigo_postal_des_id',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Codigo Postal destinatario'),
        ),
        migrations.AddField(
            model_name='envio',
            name='codigo_postal_rem',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Codigo Postal remitente'),
        ),
        migrations.AddField(
            model_name='envio',
            name='departamento_des_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='envios.Departamento', verbose_name='Departamento ID Destinatario'),
        ),
        migrations.AddField(
            model_name='envio',
            name='departamento_rem_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='envios.Departamento', verbose_name='Departamento ID Remintente'),
        ),
        migrations.AddField(
            model_name='envio',
            name='direccion2_des',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Direccion 2 del destinatario'),
        ),
        migrations.AddField(
            model_name='envio',
            name='direccion2_rem',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Direccion 2 del remitente'),
        ),
        migrations.AddField(
            model_name='envio',
            name='direccion3_des',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Direccion 3 del destinatario'),
        ),
        migrations.AddField(
            model_name='envio',
            name='direccion3_rem',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Direccion 3 del remitente'),
        ),
        migrations.AddField(
            model_name='envio',
            name='direccion_des',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Direccion del destinatario'),
        ),
        migrations.AddField(
            model_name='envio',
            name='direccion_rem',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Direccion del remitente'),
        ),
        migrations.AddField(
            model_name='envio',
            name='documento_identidad_rem',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Documento Identidad Remitente'),
        ),
        migrations.AddField(
            model_name='envio',
            name='email_des',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Correo electronico del destinatario'),
        ),
        migrations.AddField(
            model_name='envio',
            name='email_rem',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Correo electronico del remitente'),
        ),
        migrations.AddField(
            model_name='envio',
            name='empresa_des',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre de la empresa del destinatario'),
        ),
        migrations.AddField(
            model_name='envio',
            name='empresa_rem',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre de la empresa'),
        ),
        migrations.AddField(
            model_name='envio',
            name='extension_rem',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Extension del remitente'),
        ),
        migrations.AddField(
            model_name='envio',
            name='nombre_des',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre del Destinatario'),
        ),
        migrations.AddField(
            model_name='envio',
            name='nombre_rem',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre del remitente'),
        ),
        migrations.AddField(
            model_name='envio',
            name='notas_des',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Notas u observaciones del destinatario'),
        ),
        migrations.AddField(
            model_name='envio',
            name='pais_des_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='envios.Pais', verbose_name='Pais ID Destinatario'),
        ),
        migrations.AddField(
            model_name='envio',
            name='pais_rem_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='envios.Pais', verbose_name='Pais ID Remitente'),
        ),
        migrations.AddField(
            model_name='envio',
            name='telefono_des',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono del destinatario'),
        ),
        migrations.AddField(
            model_name='envio',
            name='telefono_rem',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono del remitente'),
        ),
        migrations.AddField(
            model_name='envio',
            name='tipo_tel_des',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de telefono del destinatario'),
        ),
        migrations.AddField(
            model_name='envio',
            name='tipo_tel_rem',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='tipo de telefono del remitente'),
        ),
    ]
