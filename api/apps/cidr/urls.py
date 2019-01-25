from django.urls import path
from .views import incorrect, getiprange, checkiprange


urlpatterns = [
    path('', incorrect),
    path('<ip>/', incorrect),
    path('<ip>/<cidr>', getiprange),
    path('ip/<ipin>/in_range/<rangein>/<cidr>', checkiprange),
]