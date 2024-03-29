# Generated by Django 2.2.2 on 2019-11-26 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0003_product_productcustomfield_snipcartsettings'),
        ('formpesanan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesanan',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='pesanan',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='home.Product'),
        ),
    ]
