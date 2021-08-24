# Generated by Django 3.2.6 on 2021-08-22 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tipo', models.CharField(max_length=30)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('marca', models.CharField(blank=True, max_length=30, null=True)),
                ('link', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
