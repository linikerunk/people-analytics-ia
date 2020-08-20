# Generated by Django 2.2 on 2020-08-20 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entity',
            options={'verbose_name': 'Treinamento', 'verbose_name_plural': 'Treinamentos'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Evento', 'verbose_name_plural': 'Eventos'},
        ),
        migrations.AlterModelOptions(
            name='instructor',
            options={'verbose_name': 'Instrutor', 'verbose_name_plural': 'Instrutores'},
        ),
        migrations.AlterModelOptions(
            name='training',
            options={'verbose_name': 'Treinamento', 'verbose_name_plural': 'Treinamentos'},
        ),
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]