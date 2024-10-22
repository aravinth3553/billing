# Generated by Django 5.1.1 on 2024-09-27 10:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coca', '0003_invoiceitem_course_invoiceitem_student_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceitem',
            name='parent_contact',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='parent_name',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='student_contact',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='course',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='description',
            field=models.TextField(blank=True, default='No Description'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]