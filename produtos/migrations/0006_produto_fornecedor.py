# Generated by Django 3.2.6 on 2021-09-02 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_fornecedor_telefonefornecedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='fornecedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='produtos.fornecedor'),
        ),
    ]
