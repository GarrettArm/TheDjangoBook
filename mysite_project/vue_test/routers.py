from rest_framework import routers
from vue_test.views import FuelEffeciencyViewSet

router = routers.DefaultRouter()
router.register('vue_api', FuelEffeciencyViewSet)
