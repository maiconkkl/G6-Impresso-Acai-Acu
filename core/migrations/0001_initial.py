# Generated by Django 3.0.1 on 2020-06-05 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro', models.CharField(max_length=100, verbose_name='Registro')),
                ('valor', models.CharField(max_length=100, verbose_name='Valor')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parcelas', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]
