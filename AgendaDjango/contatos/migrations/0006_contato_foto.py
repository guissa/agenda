# Generated by Django 4.1.3 on 2022-11-18 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0005_alter_contato_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='foto',
            field=models.FileField(blank=True, upload_to='fotos/%Y/%m/'),
        ),
    ]
