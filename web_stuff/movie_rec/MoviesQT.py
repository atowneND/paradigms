# Ashley Towne
# 2/28/2016
# movie recommendations

# get requests for 2.6 nastiness
import sys
sys.path.append('/afs/nd.edu/user37/cmc/Public/paradigms/python/local/lib/python2.6/site-packages/requests-2.0.0-py2.6.egg')
sys.path.append('/afs/nd.edu/user37/cmc/Public/cse332_sp16/cherrpy/data/images/')

# real code
from moviedb import _webservice_primer as mdb# from webservice primer
import PyQt4.QtCore as qtcore
import PyQt4.QtGui as qtgui
import requests
import json

class MoviesQT(qtgui.QMainWindow):
    def __init__(self):
        super(MoviesQT, self).__init__()
        self.movies = mdb._webservice_primer()

        self.setWindowTitle("Movie Recommender")
        
        self.central = MoviesCentral(parent = self)
        self.setCentralWidget(self.central)

        self.uid = 5
        mid = self.getMID()
        img = self.getMoviePoster(mid)

        pixmap = qtgui.QPixmap(str(img))
        movie_pic = qtgui.QLabel(self)
        movie_pic.setPixmap(pixmap)

    def getMID(self):
        r = requests.get(self.movies.RECOMMENDATIONS_URL + str(self.uid))
        return r.json()['movie_id']
        
    def getMoviePoster(self, mid):
        r = requests.get(self.movies.MOVIES_URL + str(mid))
        return r.json()['img']

class MoviesCentral(qtgui.QWidget):
    def __init__(self, parent=None):
        super(MoviesCentral, self).__init__(parent)

if __name__ == "__main__":
    app = qtgui.QApplication(sys.argv)
    gui = MoviesQT()
    gui.show()
    sys.exit(app.exec_())
