from api.views import Userviewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', Userviewsets)#, base_name='user_api')

