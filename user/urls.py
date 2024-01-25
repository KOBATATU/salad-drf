from django.urls import path, include
from rest_framework import routers
from user.views import UserView,UserMeViews
app_name = 'user'

router = routers.SimpleRouter()
router.register(r'users', UserView, basename="users")

urlpatterns = [
    path('',include(router.urls)),
    path('user/me/', UserMeViews.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='user-me'),
]