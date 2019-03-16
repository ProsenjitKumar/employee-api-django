from django.conf.urls import re_path, include
from .views import HomeView, EmployeerView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employeers', EmployeerView)


urlpatterns = [
    re_path('^$', HomeView.as_view(), name='home'),
    re_path('api/', include(router.urls)),
]