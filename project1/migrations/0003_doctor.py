# Generated by Django 4.2.5 on 2023-11-17 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0002_departmentss_delete_departments'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=100)),
                ('doc_specilization', models.CharField(max_length=100)),
                ('doc_pic', models.ImageField(upload_to='doctors')),
            ],
        ),
    ]