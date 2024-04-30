# Generated by Django 5.0.3 on 2024-03-20 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person_for', '0003_remove_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person_for.book'),
        ),
    ]