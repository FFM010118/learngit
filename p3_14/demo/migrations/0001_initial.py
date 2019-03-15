# Generated by Django 2.0.13 on 2019-03-14 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Stuendt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=50)),
                ('cls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.Cls')),
            ],
        ),
    ]
