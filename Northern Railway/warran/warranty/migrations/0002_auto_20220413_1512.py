# Generated by Django 3.0.5 on 2022-04-13 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warranty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additem',
            name='aac',
            field=models.TextField(max_length=120),
        ),
        migrations.AlterField(
            model_name='additem',
            name='gw',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='additem',
            name='plno',
            field=models.TextField(max_length=120),
        ),
        migrations.AlterField(
            model_name='additem',
            name='relatedplno',
            field=models.TextField(max_length=120),
        ),
        migrations.AlterField(
            model_name='additem',
            name='specno',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='additem',
            name='unifiedplno',
            field=models.TextField(max_length=120),
        ),
    ]