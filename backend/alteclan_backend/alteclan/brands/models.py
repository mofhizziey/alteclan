from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from .display import LABEL_DISPLAY, COLLECTION_DISPLAY
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Brand(models.Model):
    brand_name = models.CharField(max_length=250, default='')
    brand_logo = models.ImageField(upload_to='Brand Logos', default='')
    brand_bio = models.TextField(default='')
    date_created = models.DateTimeField(default=timezone.now())
    slug = models.SlugField(null=True, blank=True, default='')

    def __str__(self):
        return f'{self.brand_name} Brand'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.brand_name}')
        return super().save(*args, **kwargs)



class Merchandise(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    merchandise_name = models.CharField(max_length=250, default='')
    merchandise_color = models.CharField(max_length=250, default='')
    merchandise_size = models.CharField(max_length=250, default='')
    merchandise_image = models.ImageField(upload_to='Merch Image', default='')
    labels = models.CharField(max_length=250, choices=LABEL_DISPLAY, default='None')
    collection = models.CharField(max_length=250, choices=COLLECTION_DISPLAY,
                                        default='Choose your desired collection')
    price = models.CharField(max_length=250, default='')
    delivery_cost = models.CharField(max_length=250, default='', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, default='')


    def __str__(self):
        return f'Merchandise Name : {self.merchandise_name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.brand} {self.merchandise_name} {self.merchandise_size} {self.merchandise_color}')
        return super().save(*args, **kwargs)

class MerchandisesList(models.Model):
    slug = models.SlugField(null=True, blank=True, default='')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default='', null=True, blank=True)
    merchandises = models.ManyToManyField(Merchandise)


    def __str__(self):
        return f'{self.brand} Mechandises List'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'merchandises-list-{self.brand}')
        return super().save(*args, **kwargs)



# ProductOrder, these are the items that have been
class BillingAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    street_address = models.CharField(max_length=250, default='')
    city = models.CharField(max_length=250, default='')
    state = models.CharField(max_length=250, default='')
    zip = models.CharField(max_length=250, default='')

    def __str__(self):
        return f'{self.user}'
# Inherits from brand
class BrandProfile(models.Model):
    brand = models.OneToOneField(Brand, on_delete=models.CASCADE, related_name='brand_profile', null=True, blank=True)
    merchandises = models.ManyToManyField(Merchandise)
    mobile_number = models.CharField(max_length=250, default='')
    email_address = models.CharField(max_length=250, default='')
    address = models.ForeignKey(BillingAddress, on_delete=models.CASCADE, default='', null=True, blank=True)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.brand} Profile'


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    merchandises = models.ManyToManyField(Merchandise)
    address = models.ForeignKey(BillingAddress, on_delete=models.CASCADE)
    # Inherit order and bring it into the cart
    # Show list of orders and their quantities

    def __str__(self):
        return f'{self.merchandise} x ( {self.quantity} ) pcs by {self.user} '

# Represent a particular product order
class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.ForeignKey(BillingAddress, on_delete=models.CASCADE)
    order_cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    order_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'{self.user} has made an active order!'
