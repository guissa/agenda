# Generated by Django 4.1.3 on 2022-11-17 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='data_criacao',
            new_name='Data_de_criacao',
        ),
    ]
