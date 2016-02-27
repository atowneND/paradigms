# Ashley Towne
# 2/28/2016
# movie recommendations

# get requests for 2.6 nastiness
import sys
sys.path.append('/afs/nd.edu/user37/cmc/Public/paradigms/python/local/lib/python2.6/site-packages/requests-2.0.0-py2.6.egg')

# real code
import requests
import json

class MoviesQT(QMainWindow):
    def __init__(self):
        super(MoviesQT, self).__init__()
        self.setWindowTitle("Movie Recommender")
