# Generated by Django 5.0.3 on 2024-03-24 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person_for', '0016_alter_department_college_alter_professor_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
