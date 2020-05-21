from django.urls import path
from django.conf.urls import url, include
from .views import UserView


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/', UserView.as_view())
]
