from django.db import models
from home.models import Product
from django.shortcuts import reverse
# Create your models here.

class Pesanan(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    date = models.DateField(auto_now=True)
    nama = models.CharField(null=False, blank=False, max_length=20)
    no_wa = models.CharField(null=False, blank=False,max_length=12)
    title = models.CharField(null=False, blank=False,max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    class Meta:
        verbose_name = 'Pesanan'

    def get_product(self,product_id):
        product = Product.objects.get(id=product_id)
        return reverse('formpesanan', kwargs={'product':product})

    # def save(self, *args, **kwargs):
    #     super().save(*args,**kwargs)
