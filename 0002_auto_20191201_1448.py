# Generated by Django 2.2.6 on 2019-12-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='sfile',
        ),
        migrations.AlterField(
            model_name='student',
            name='sadress',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='sdob',
            field=models.CharField(max_length=50),
        ),
    ]