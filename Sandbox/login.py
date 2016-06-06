import sys
from PyQt4 import uic, QtGui
from PyQt4.QtCore import SIGNAL
from LoginThread import LoginThread

#Login design path
ui_login = 'design/ui_login.ui'

# Getting Ui class
Ui_LoginWidget, Ui_LoginBaseClass = uic.loadUiType(ui_login)

class Login(QtGui.QWidget, Ui_LoginWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        Ui_LoginWidget.__init__(self)
        self.setupUi(self)
        self.init_ui()

        #variables
        self.ID = ''
        self.password = ''

        self.IDLineEdit.setText('051203043')
        self.passwordLineEdit.setText('051203043')

    def init_ui(self):
        self.loginPushButton.clicked.connect(self.check_login)


    def check_login(self):
        self.ID = str(self.IDLineEdit.text())
        self.password = str(self.passwordLineEdit.text())

        #Debugging purpose
        print self.ID, self.password

        self.loginThread = LoginThread(self.ID, self.password)
        self.loginThread.start()
        self.connect(self.loginThread, SIGNAL("log_in(QString)"), self.clogin)
        self.connect(self.loginThread, SIGNAL('update_status(QString)'), self.update_status)

    def clogin(self, text):
        print str(text)

    def update_status(self, status):
        self.status = str(status)
        self.statusLabel.setText(self.status)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())




