# Generated by Django 4.2.3 on 2024-08-06 14:44

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
            name='ProcessorToDistributorTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(blank=True, help_text='This is an optional field to add a description to the products', max_length=200, null=True)),
                ('batch_number', models.CharField(blank=True, max_length=1000, null=True, unique=True)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('haverst_date', models.DateTimeField(verbose_name='Production Date')),
                ('expiration_date', models.DateTimeField()),
                ('accepted', models.BooleanField(default=False, verbose_name='Accepted Status')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/')),
                ('product_url', models.URLField(blank=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('distributor', models.ForeignKey(limit_choices_to={'groups__name': 'Distributor', 'profile__address__isnull': False}, on_delete=django.db.models.deletion.CASCADE, related_name='processor_to_distributor', to=settings.AUTH_USER_MODEL)),
                ('processor', models.ForeignKey(limit_choices_to={'groups__name': 'Processor'}, on_delete=django.db.models.deletion.CASCADE, related_name='processor_distributor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FarmerToProcessorTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(blank=True, help_text='This is an optional field to add a description to the products', max_length=200, null=True)),
                ('batch_number', models.CharField(blank=True, max_length=1000, null=True, unique=True)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('haverst_date', models.DateTimeField()),
                ('accepted', models.BooleanField(default=False, verbose_name='Accepted Status')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/')),
                ('product_url', models.URLField(blank=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('farmer', models.ForeignKey(limit_choices_to={'groups__name': 'Farmer'}, on_delete=django.db.models.deletion.CASCADE, related_name='farmer_processor', to=settings.AUTH_USER_MODEL)),
                ('processor', models.ForeignKey(limit_choices_to={'groups__name': 'Processor', 'profile__address__isnull': False}, on_delete=django.db.models.deletion.CASCADE, related_name='farmer_to_processor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FarmerToAggregatorTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(blank=True, help_text='This is an optional field to add a description to the products', max_length=200, null=True)),
                ('batch_number', models.CharField(blank=True, max_length=1000, null=True, unique=True)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('haverst_date', models.DateTimeField()),
                ('accepted', models.BooleanField(default=False, verbose_name='Accepted Status')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/')),
                ('product_url', models.URLField(blank=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('aggregator', models.ForeignKey(limit_choices_to={'groups__name': 'Aggregator', 'profile__address__isnull': False}, on_delete=django.db.models.deletion.CASCADE, related_name='farmer_to_aggregator', to=settings.AUTH_USER_MODEL)),
                ('farmer', models.ForeignKey(limit_choices_to={'groups__name': 'Farmer'}, on_delete=django.db.models.deletion.CASCADE, related_name='farmer_aggregator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DistributorToRetailerTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(blank=True, help_text='This is an optional field to add a description to the products', max_length=200, null=True)),
                ('batch_number', models.CharField(blank=True, max_length=1000, null=True, unique=True)),
                ('accepted', models.BooleanField(default=False, verbose_name='Accepted Status')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/')),
                ('product_url', models.URLField(blank=True)),
                ('distributor', models.ForeignKey(limit_choices_to={'groups__name': 'Distributor'}, on_delete=django.db.models.deletion.CASCADE, related_name='distributor_retailer', to=settings.AUTH_USER_MODEL)),
                ('retailer', models.ForeignKey(limit_choices_to={'groups__name': 'Retailer', 'profile__address__isnull': False}, on_delete=django.db.models.deletion.CASCADE, related_name='distributor_to_retailer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AggregatorToProcessorTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(blank=True, help_text='This is an optional field to add a description to the products', max_length=200, null=True)),
                ('batch_number', models.CharField(blank=True, max_length=1000, null=True, unique=True)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('accepted', models.BooleanField(default=False, verbose_name='Accepted Status')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/')),
                ('product_url', models.URLField(blank=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('aggregator', models.ForeignKey(limit_choices_to={'groups__name': 'Aggregator'}, on_delete=django.db.models.deletion.CASCADE, related_name='aggregator_processor', to=settings.AUTH_USER_MODEL)),
                ('processor', models.ForeignKey(limit_choices_to={'groups__name': 'Processor', 'profile__address__isnull': False}, on_delete=django.db.models.deletion.CASCADE, related_name='aggregator_to_processor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
