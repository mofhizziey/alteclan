
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Brand, BrandProfile, Merchandise, MerchandisesList

# If a new brand is created, silmultaneously create a profile for the brand.
@receiver(post_save, sender=Brand)
def create_brand_profile(sender, instance, created, **kwargs):
    if created:
        BrandProfile.objects.create(brand=instance)
        print("New Brand profile has been created")

@receiver(post_save, sender=Brand)
def save_brand_profile(sender, instance, **kwargs):
    instance.brand_profile.save()
    print("Brand Profile saved!")


