# Generated by Django 3.2.6 on 2021-09-06 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0008_alter_categoriaproduto_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='fornecedor',
            name='celular',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='telefone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='email',
            field=models.CharField(max_length=80),
        ),
        migrations.DeleteModel(
            name='TelefoneFornecedor',
        ),
    ]