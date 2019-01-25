from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cidr/', include('cidr.urls')),
    path('cidr_range/', include('cidr.urls')),
    path('', include('cidr.urls'))
]