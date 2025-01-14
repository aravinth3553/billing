# Generated by Django 5.1.1 on 2024-10-08 10:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coca', '0005_invoice_installment1_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceitem',
            name='address',
            field=models.TextField(default='N/A'),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='degree',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='passed_out_year',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='validity_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='installment1_amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='installment1_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='installment2_amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='installment2_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='description',
            field=models.TextField(default='No Description'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='parent_contact',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='student_contact',
            field=models.CharField(max_length=20),
        ),
    ]
