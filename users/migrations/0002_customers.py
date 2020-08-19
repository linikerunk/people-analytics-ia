# Generated by Django 3.0.8 on 2020-07-30 01:48

from django.db import migrations


def create_data(apps, schema_editor):
    Customer = apps.get_model('users', 'Customer')
    Customer(first_name="Customer 001", last_name="Customer 001", email="customer001@email.com",
             phone="00000000", address="Customer 000 Address", description="Customer 001 description").save()


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_data),
    ]