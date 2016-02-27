# Ashley Towne
# 2/26/2016
# web service primer

# get requests for 2.6 nastiness
import sys
sys.path.append('/afs/nd.edu/user37/cmc/Public/paradigms/python/local/lib/python2.6/site-packages/requests-2.0.0-py2.6.egg')

# real code
import requests
import json

class _webservice_primer:
    print "hi"

    def __init__(self, apikey):
        self.API_KEY = apikey
        self.SITE_URL = 'http://student02.cse.nd.edu:40001'
        self.MOVIES_URL = self.SITE_URL + '/movies/'
        self.RESET_URL = self.SITE_URL + '/reset/'

    def get_movie(self, mid):
        r = requests.get(self.MOVIES_URL + str(mid))
        return r.json()

    def set_movie_title(self, mid, title):
        movie = self.get_movie(mid)
        movie['title'] = 'Something Else'
        movie['apikey'] = self.API_KEY
        r = requests.put(self.MOVIES_URL + str(mid), data = json.dumps(movie))
        return r.json()

    def delete_movie(self, mid):
        mydata = {}
        mydata['apikey'] = self.API_KEY
        r = requests.delete(self.MOVIES_URL + str(mid), data = json.dumps(mydata))
        return r.json()

    def reset_movie(self, mid):
        mydata = {}
        mydata['apikey'] = self.API_KEY
        r = requests.put(self.RESET_URL + str(mid), data = json.dumps(mydata))
        return r.json()

