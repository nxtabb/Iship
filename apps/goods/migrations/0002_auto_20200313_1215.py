# Generated by Django 2.2 on 2020-03-13 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='ename',
            field=models.CharField(default='', max_length=30, verbose_name='英文名称'),
        ),
    ]
