from django.contrib import admin
from .models import BrandProfile, Brand, Merchandise, Cart, Order, MerchandisesList, BillingAddress
# Register your models here.

class BrandInline(admin.TabularInline):
    model = Brand
    extra = 3

class BrandAdmin(admin.ModelAdmin):
    #inlines = [BrandInline]
    list_display = ['brand_name', 'brand_logo', 'brand_bio', 'date_created', 'slug']
    list_filter = ['date_created']

class BrandProfileAdmin(admin.ModelAdmin):
    #inlines = [BrandInline]
    list_display = ['brand_name', 'brand_logo', 'brand_bio', 'date_created', 'slug']
    list_filter = ['date_created']

class BrandAdmin(admin.ModelAdmin):
    #inlines = [BrandInline]
    list_display = ['brand_name', 'brand_logo', 'date_created', 'slug']

class MechandiseAdmin(admin.ModelAdmin):
    #inlines = [BrandInline]
    list_display = ['brand', 'merchandise_name', 'merchandise_color', 'merchandise_size', 'merchandise_image', 'labels', 'collection', 'price', 'delivery_cost', 'slug']


admin.site.register(BillingAddress)
admin.site.register(Brand, BrandAdmin)
admin.site.register(BrandProfile)
admin.site.register(Merchandise, MechandiseAdmin)
admin.site.register(MerchandisesList)
admin.site.register(Cart)
admin.site.register(Order)



