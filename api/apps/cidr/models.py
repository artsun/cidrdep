from django.db import models
import socket, struct

class Iprange(models.Model):
    first_ip = models.CharField(max_length=255, null=False)
    last_ip = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.first_ip, self.last_ip)

    def _iscorrect(self, ip, cidr_zer=None):
    	if cidr_zer is not None:
    		if cidr_zer<0:
    			return False
    	if (len(ip.split(".")) != 4):
    		return False
    	else:
    		return True

    def _getnums(self, ip, cidr_zer):
    	i = struct.unpack('>I', socket.inet_aton(ip))[0]
    	first_ip = (i >> cidr_zer) << cidr_zer
    	last_ip = first_ip | ((1 << cidr_zer) - 1)
    	return first_ip, last_ip

    def getrange(self, ip, cidr):
    	cidr_zer = 32 - int(cidr)
    	ip = ip.replace("_", ".")
    	if not self._iscorrect(ip, cidr_zer):
    		return False    	
    	try:
    		firstip, lastip = self._getnums(ip, cidr_zer)    		
    	except:
    		return False
    	self.first_ip = socket.inet_ntoa(struct.pack('>I',firstip))
    	self.last_ip = socket.inet_ntoa(struct.pack('>I',lastip))
    	return True

    def isinrange(self, ipin, rangein, cidr):
    	cidr_zer = 32 - int(cidr)
    	ipin = ipin.replace("_", ".")
    	rangein = rangein.replace("_", ".")
    	if not self._iscorrect(ipin):
    		return False, False
    	if not self._iscorrect(rangein, cidr_zer):
    		return False, False
    	try:
    		firstip, lastip = self._getnums(rangein, cidr_zer)
    		ipin = struct.unpack('>I', socket.inet_aton(ipin))[0]
    	except:
    		return False, False
    	if (firstip<=ipin<=lastip):
    		return True, True
    	else:
    		return True, False

