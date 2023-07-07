# Generated by Django 4.2.1 on 2023-06-11 10:51

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
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_of_document', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('customers_name', models.CharField(max_length=255)),
                ('customers_signature', models.IntegerField(help_text='Use id number')),
                ('no_of_pages', models.IntegerField()),
                ('quantity_rate', models.IntegerField()),
                ('total', models.IntegerField()),
                ('date_created', models.DateField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types', to='services.servicetype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]