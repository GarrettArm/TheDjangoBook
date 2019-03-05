from rest_framework import routers
from .views import FuelEffeciencyViewSet

router = routers.DefaultRouter()
router.register('vue_api', FuelEffeciencyViewSet, base_name='FuelEffeciency')
