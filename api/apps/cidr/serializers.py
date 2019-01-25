from rest_framework import serializers
from .models import Iprange


class IpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iprange
        fields = ("first_ip", "last_ip")