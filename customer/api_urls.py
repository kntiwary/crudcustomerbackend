from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register('Customer',CustomerViewSet)
# router.register('callstatusmaster',ClientCallStatusTypeViewSet)


# router.register('')


urlpatterns =[
    path('',include(router.urls))
]