
from django.urls import include, path

# urls
urlpatterns = [
    path('api/v1/test', include('test_api.urls')),
    path('api/v1/auth/', include('authentication.urls')),
]