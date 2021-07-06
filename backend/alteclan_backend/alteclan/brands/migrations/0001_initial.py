# Generated by Django 3.2.5 on 2021-07-04 15:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(default='', max_length=250)),
                ('city', models.CharField(default='', max_length=250)),
                ('state', models.CharField(default='', max_length=250)),
                ('zip', models.CharField(default='', max_length=250)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(default='', max_length=250)),
                ('brand_logo', models.ImageField(default='', upload_to='Brand Logos')),
                ('brand_bio', models.TextField(default='')),
                ('date_created', models.DateTimeField(default=datetime.datetime(2021, 7, 4, 15, 48, 52, 336912, tzinfo=utc))),
                ('slug', models.SlugField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.billingaddress')),
            ],
        ),
        migrations.CreateModel(
            name='Merchandise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchandise_name', models.CharField(default='', max_length=250)),
                ('merchandise_color', models.CharField(default='', max_length=250)),
                ('merchandise_size', models.CharField(default='', max_length=250)),
                ('merchandise_image', models.ImageField(default='', upload_to='Merch Image')),
                ('labels', models.CharField(choices=[('None', 'None'), ('New Merchandise', 'New Merchandise'), ('Limited Stock', 'Limited Stock'), ('FREE DELIVERY', 'FREE DELIVERY')], default='None', max_length=250)),
                ('collection', models.CharField(choices=[('Choose your desired collection', 'Choose your desired collection'), ('Tees', 'Tees'), ('Rings', 'Rings'), ('Joggers and Track', 'Joggers and Track'), ('Chains', 'Chains'), ('Jeans', 'Jeans'), ('Skating', 'Skating'), ('Durags, Caps and Hats', 'Durags, Caps and Hats'), ('Skating', 'Skating'), ('Sweatshirts and Hoodies', 'Sweatshirts and Hoodies'), ('Kicks and Sandals', 'Kicks and Sandals'), ('Masks', 'Masks'), ('Shades', 'Shades'), ('Lumberjacks and Vintage', 'Lumberjacks and Vintage'), ('Piercings and Studs', 'Piercings and Studs'), ('Baggy Wears', 'Baggy Wears'), ('Tattoos', 'Tattoos'), ('Graffiti', 'Graffiti')], default='Choose your desired collection', max_length=250)),
                ('price', models.CharField(default='', max_length=250)),
                ('delivery_cost', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('slug', models.SlugField(blank=True, default='', null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('delivered', models.BooleanField(default=False)),
                ('order_date', models.DateTimeField(default=datetime.datetime(2021, 7, 4, 15, 48, 52, 344722, tzinfo=utc))),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.billingaddress')),
                ('order_cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='brands.cart')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MerchandisesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='', null=True)),
                ('brand', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='brands.brand')),
                ('merchandises', models.ManyToManyField(to='brands.Merchandise')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='merchandises',
            field=models.ManyToManyField(to='brands.Merchandise'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='BrandProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(default='', max_length=250)),
                ('email_address', models.CharField(default='', max_length=250)),
                ('street_address', models.CharField(default='', max_length=250)),
                ('city', models.CharField(default='', max_length=250)),
                ('state', models.CharField(default='', max_length=250)),
                ('zip', models.CharField(default='', max_length=250)),
                ('brand', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand_profile', to='brands.brand')),
                ('merchandises', models.ManyToManyField(to='brands.Merchandise')),
            ],
        ),
    ]
