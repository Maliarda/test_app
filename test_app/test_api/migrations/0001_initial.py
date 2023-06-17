# Generated by Django 3.2 on 2023-06-16 21:29

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=10, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='IQTestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)])),
                ('time_taken', models.DateTimeField(auto_now_add=True)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_api.participant')),
            ],
        ),
        migrations.CreateModel(
            name='EQTestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letters', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('а', 'A'), ('б', 'B'), ('в', 'C'), ('г', 'D'), ('д', 'E')], max_length=2), size=5)),
                ('time_taken', models.DateTimeField(auto_now_add=True)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_api.participant')),
            ],
        ),
    ]
