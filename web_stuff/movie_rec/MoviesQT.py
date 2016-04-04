# Ashley Towne
# 2/28/2016
# movie recommendations

# get requests for 2.6 nastiness
import sys
sys.path.append('/afs/nd.edu/user37/cmc/Public/paradigms/python/local/lib/python2.6/site-packages/requests-2.0.0-py2.6.egg')
sys.path.append('/afs/nd.edu/user37/cmc/Public/cse332_sp16/cherrypy/data/images/')

# real code
import PyQt4.QtCore as qtcore
import PyQt4.QtGui as qtgui
import requests
import json

class MoviesQT(qtgui.QMainWindow):
    def __init__(self):
        super(MoviesQT, self).__init__()
        self.SITE_URL = 'http://student02.cse.nd.edu:40001'
        self.MOVIES_URL = self.SITE_URL + '/movies/'
        self.RESET_URL = self.SITE_URL + '/reset/'
        self.RECOMMENDATIONS_URL = self.SITE_URL + '/recommendations/'
        self.RATINGS_URL = self.SITE_URL + '/ratings/'
        self.USERS_URL = self.SITE_URL + '/users/'
        self.APIKEY = '1O44fU28eQ'

        self.initUI()

    def initUI(self): 
        self.uid = 10
        self.mid = self.getMID()

        self.central = MoviesCentral(parent = self)
        self.setCentralWidget(self.central)

        layout = qtgui.QHBoxLayout()
        
        self.setWindowTitle("Movie Recommender")

        self.movie_title = qtgui.QLabel(self)
        self.movie_title.setGeometry(200,20,1000,100)
        self.movie_genres = qtgui.QLabel(self)
        self.movie_pic = qtgui.QLabel(self)
        self.movie_rating = qtgui.QLabel(self)

        layout.addWidget(self.movie_title)
        layout.addWidget(self.movie_genres)
        layout.addWidget(self.movie_pic)
        layout.addWidget(self.movie_rating)

        self.update()

        self.up_button = qtgui.QPushButton("UP", self)
        self.up_button.move(30,150)
        self.down_button = qtgui.QPushButton("DOWN",self)
        self.down_button.move(450,150)

        hbox = qtgui.QHBoxLayout()
        hbox.addWidget(self.up_button)
        hbox.addWidget(self.down_button)

        self.connect(self.up_button, qtcore.SIGNAL("clicked()"), self.upvote)
        self.connect(self.down_button, qtcore.SIGNAL("clicked()"), self.downvote)

        exitAction = qtgui.QAction(qtgui.QIcon('Exit'),'Exit',self)
        exitAction.triggered.connect(self.close)
        menu = self.menuBar()
        fileMenu = menu.addMenu('&File')
        fileMenu.addAction(exitAction)

        viewAction = qtgui.QAction(qtgui.QIcon('View Profile'),'View Profile',self)
        viewAction.triggered.connect(self.getProfile)
        setUserAction = qtgui.QAction(qtgui.QIcon('Set User'),'Set User', self)
        setUserAction.triggered.connect(self.setUser)
        userMenu = menu.addMenu('&User')
        userMenu.addAction(viewAction)
        userMenu.addAction(setUserAction)

    def setUser(self):
        uid, ans = qtgui.QInputDialog.getText(
                self,
                'Set User',
                "User ID:",
            )
        if ans:
            try:
                uid = int(uid)
                self.uid = uid
                self.update()
            except Exception as ex:
                msg = qtgui.QMessageBox.warning(
                        self,
                        'WARNING',
                        "User ID must be an integer",
                    )

    def getProfile(self):
        r = requests.get(self.USERS_URL + str(self.uid)).json()
        msg = qtgui.QMessageBox.information(
                self,
                'Message',
                "Profile\nGender: {gender}\nZipcode: {zipcode}\nAge: {age}".format(gender=r['gender'],zipcode=r['zipcode'],age=r['age']),
                qtgui.QMessageBox.Ok,
            )

    def upvote(self):
        info = {}
        info['movie_id'] = self.mid
        info['rating'] = 5
        info['apikey'] = self.APIKEY
        r = requests.put(self.RECOMMENDATIONS_URL+str(self.uid), data = json.dumps(info))
        self.update()

    def downvote(self):
        info = {}
        info['movie_id'] = self.mid
        info['rating'] = 1
        info['apikey'] = self.APIKEY
        r = requests.put(self.RECOMMENDATIONS_URL+str(self.uid), data = json.dumps(info))
        self.update()

    def update(self):
        self.mid = self.getMID()
        img = self.getMovieFile()
        self.setMoviePoster(img)
        self.setMovieInfo()
        self.getMovieRating()

    def getMovieRating(self):
        rating = requests.get(self.RATINGS_URL+str(self.mid)).json()['rating']
        self.movie_rating.setText("{r:.2f}".format(r=rating))
        self.movie_rating.move(200,430)

    def setMovieInfo(self):
        info = requests.get(self.MOVIES_URL+str(self.mid)).json()
        title = info['title']
        self.movie_title.setText(title)
        self.movie_title.move(200,20)

        genres = info['genres']
        self.movie_genres.setText(genres)
        self.movie_genres.move(200,400)

    def setMoviePoster(self, img):
        self.movie_pic.setPixmap(qtgui.QPixmap(img))
        self.movie_pic.setGeometry(200,200,400,400)
        self.movie_pic.move(200,20)

    def getMID(self):
        r = requests.get(self.RECOMMENDATIONS_URL + str(self.uid))
        return r.json()['movie_id']
        
    def getMovieFile(self):
        r = requests.get(self.MOVIES_URL + str(self.mid))
        return '/afs/nd.edu/user37/cmc/Public/cse332_sp16/cherrypy/data/images'+str(r.json()['img'])

class MoviesCentral(qtgui.QWidget):
    def __init__(self, parent = None):
        super(MoviesCentral, self).__init__(parent)


if __name__ == "__main__":
    app = qtgui.QApplication(sys.argv)
    gui = MoviesQT()
    gui.show()
    sys.exit(app.exec_())
