# Generated by Django 2.1.4 on 2019-02-19 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
                ('tipo', models.CharField(max_length=150, verbose_name='Tipo')),
            ],
        ),
    ]
