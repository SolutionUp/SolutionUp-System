# Generated by Django 3.2.6 on 2021-09-11 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Terceiro',
            fields=[
                ('nome', models.CharField(max_length=100)),
                ('ramo', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=80)),
                ('telefone', models.CharField(blank=True, max_length=11, null=True)),
                ('celular', models.CharField(blank=True, max_length=11, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
