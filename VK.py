import urllib, urllib2, random, hashlib, time, re
from django.utils import simplejson

API_VERSION='3.0'

def vktime():
    md5 = hashlib.md5()
    api_id='123456'
    secret='secret'
    md5.update('api_id=%s'%api_id)
    md5.update('format=JSON')
    md5.update('method=getServerTime')
    md5.update('v=2.0')
    md5.update(secret)
    url="http://api.vkontakte.ru/api.php?api_id=%s&format=JSON&method=getServerTime&v=2.0&sig=%s" %(api_id, md5.hexdigest())
    r = urllib2.urlopen(url).read()
    m = re.match('\{"response":([0-9]+)\}', r)
    if (m):
        return int(m.group(1))
    else:
        return int(time.time())

DELTA_UNIXTIME = vktime() - int(time.time())
def timestamp():
    return int(time.time())+DELTA_UNIXTIME

class VKReq():
    def __init__(self, api_id, api_secret):
        self.api_id = api_id
        self.api_secret = api_secret
        self.random = 0

    def _update_random(self):
        while(True):
            r = random.randint(0, 1000000)
            if (r != self.random):
                self.random = r
                break

    def _sig(self, params):
        m = hashlib.md5()
        list = params.items()
        list.sort()
        str = ["%s=%s" % (k, v) for k, v in list]
        m.update(''.join(str))
        m.update(self.api_secret)
        return m.hexdigest()

    def _params(self, method_params):
        self._update_random()
        p = {'api_id': self.api_id,
             'format': 'JSON',
             'timestamp': timestamp(),
             'random': self.random,
             'v': API_VERSION}
        p.update(method_params)
        p.update(sig=self._sig(p))
        return p

    def get(self, method_params):
        """return response (dict)"""
        p = self._params(method_params)
        data = urllib.urlencode(p)
        return simplejson.loads(urllib2.urlopen(urllib2.Request('http://api.vkontakte.ru/api.php', data)).read())['response']
