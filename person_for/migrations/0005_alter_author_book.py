# Generated by Django 5.0.3 on 2024-03-20 12:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person_for', '0004_alter_author_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='person_for.book'),
        ),
    ]
