from django.http import JsonResponse
from .models import Iprange
from .serializers import IpSerializer


def incorrect(request, ip=None):
	return JsonResponse({'error': 'Invalid cidr'}, status=404)

def getiprange(request, ip=None, cidr=None):
    entry = Iprange()
    if entry.getrange(ip, cidr):
    	serializer = IpSerializer(entry, many=False)
    	return JsonResponse(serializer.data, safe=False)
    else:
    	return JsonResponse({'error': 'Invalid cidr'}, safe=False)

def checkiprange(request, ipin=None, rangein=None, cidr=None):
	entry = Iprange()
	check = entry.isinrange(ipin, rangein, cidr)
	if not (check[0] or check[1]):
		return JsonResponse({'error': 'Invalid cidr'}, safe=False)
	elif not (check[1]):
		return JsonResponse({'result': 'False'}, safe=False)
	else:
		return JsonResponse({'result': 'True'}, safe=False)
