# Generated by Django 4.2.4 on 2023-09-22 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_version'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='version',
            options={'verbose_name': 'Версию', 'verbose_name_plural': 'Версии'},
        ),
        migrations.AlterField(
            model_name='version',
            name='version_number',
            field=models.IntegerField(unique=True, verbose_name='Номер версии'),
        ),
    ]