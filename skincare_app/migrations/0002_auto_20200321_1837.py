# Generated by Django 3.0.3 on 2020-03-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skincare_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
