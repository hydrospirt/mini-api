from api.views import TextFileViewset
from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('txt', TextFileViewset, basename='textfiles')

urlpatterns = [
    path(settings.API_VERSION, include(router.urls)),
]
