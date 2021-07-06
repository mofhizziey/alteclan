from rest_framework import routers
from .views import MerchandiseViewSet, OrderViewSet, CartViewSet, BrandViewSet, BrandProfileViewSet, MerchandiseListViewSet

router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'brand_profile', BrandProfileViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'merchandises', MerchandiseViewSet)
router.register(r'merchandises_list', MerchandiseListViewSet)
router.register(r'cart', CartViewSet)





