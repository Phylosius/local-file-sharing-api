from django.shortcuts import redirect
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="File Sharing API",
      default_version='v1',
      description="API for file hosting",
      # terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="hei.phylosius@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny,],
)

def default_view(request):

   return redirect('schema-swagger-ui')
