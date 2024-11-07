from django.urls import path

from api.files import views

urlpatterns = [
    path('test', views.test, name='files-test'),
]
