# name is notworldssimplest.pyw
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#app = QApplication(sys.argv)
#form = QDialog()
#QTimer.singleShot(5000,app.quit)
#
#form.show()
#app.exec_()
class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.exitbutton = QPushButton("Exit")
        layout = QHBoxLayout()
        layout.addWidget(self.exitbutton)
        self.setLayout(layout)
        self.connect(self.exitbutton, SIGNAL("clicked()"), self.exitProgram)

    def exitProgram(self):
        sys.exit()

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()

