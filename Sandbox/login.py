import sys
from PyQt4 import uic, QtGui
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QStringList
from PyQt4.QtCore import QString
from LoginThread import LoginThread
import ast

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

        # Button

        # Info
        self.book_info_dict_list = []

    def init_ui(self):
        self.loginPushButton.clicked.connect(self.check_login)
        self.nextPushButton.setEnabled(False)


    def check_login(self):
        self.ID = str(self.IDLineEdit.text())
        self.password = str(self.passwordLineEdit.text())

        # Creating thread instance
        self.loginThread = LoginThread(self.ID, self.password)
        self.loginThread.start()

        # Connecting the thread
        self.connect(self.loginThread, SIGNAL('update_status(QString)'), self.update_status)
        self.connect(self.loginThread, SIGNAL('fetch_book_data(QStringList)'), self.fetch_book_data)

    def update_status(self, status):
        self.status = str(status)
        self.statusLabel.setText(self.status)

        #Enable next on successful login
        if "Successfully logged" in self.status:
            self.nextPushButton.setEnabled(True)
        elif "incorrect" in self.status:
            self.nextPushButton.setEnabled(False)



    def fetch_book_data(self, info_list):
        """
        TODO:
        Get's all info on logging in to library
        """
        # info_dict = ast.literal_eval(str(info))
        # print info_dict
        for item in info_list:
            # Deleting unnecessary strings TODO: upgrade later
            the_item = str(item)
            the_item = the_item.replace('Renew\n(', '').replace(' of 5 renewals remaining)', '')
            item_to_dict = ast.literal_eval(the_item)
            self.book_info_dict_list.append(item_to_dict)

        print self.book_info_dict_list


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())




