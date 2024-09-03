# Generated by Django 4.2.15 on 2024-09-01 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.CharField(choices=[('TECH', 'Technology'), ('FIN', 'Finance'), ('EDU', 'Education'), ('HEALTH', 'Healthcare'), ('AGR', 'Agriculture')], max_length=50)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('expenses', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ideas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
