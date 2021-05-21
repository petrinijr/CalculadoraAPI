# Generated by Django 3.2.3 on 2021-05-21 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calcapp', '0004_alter_test_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='status',
            field=models.CharField(choices=[('0', 'Success'), ('1', 'Failure')], default='0', max_length=10),
        ),
    ]
