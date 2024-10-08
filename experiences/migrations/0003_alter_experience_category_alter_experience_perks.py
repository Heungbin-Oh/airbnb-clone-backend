# Generated by Django 5.1 on 2024-08-23 05:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('experiences', '0002_experience_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='experiences', to='categories.category'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='perks',
            field=models.ManyToManyField(related_name='experiences', to='experiences.perk'),
        ),
    ]
