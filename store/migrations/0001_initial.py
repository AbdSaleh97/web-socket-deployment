# Generated by Django 5.1 on 2024-08-31 11:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='store_logos/')),
                ('description', models.TextField()),
                ('social_links', models.JSONField(blank=True, default=dict)),
                ('views', models.PositiveIntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
