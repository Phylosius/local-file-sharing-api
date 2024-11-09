from django.urls import path

from files import views

urlpatterns = [
    path('test', views.test, name='files-test'),
]
