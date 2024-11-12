from django.urls import path
from rest_framework import routers

from files import views
from files.views import FileInfoSet

router = routers.DefaultRouter()
router.register('files', FileInfoSet)
urlpatterns = [
    path('test', views.test, name='files-test'),
]
