from PyQt4 import QtGui
from PyQt4.QtCore import QThread, SIGNAL
from selenium import webdriver
import time

import sys


class LoginThread(QThread):
    def __init__(self, ID, password):
        QThread.__init__(self)
        self.ID = str(ID)
        self.password = str(password)

        #library url
        self.libraryUrl = 'http://library.kuet.ac.bd'



    def __del__(self):
        self.wait()

    def check_login(self):
        #emits signal for logging in
        self.emit(SIGNAL('update_status(QString)'), 'Trying to log in ... be patient')

        # browser
        self.libraryBrowser = webdriver.Chrome()
        self.libraryBrowser.get(self.libraryUrl)
        time.sleep(1)

        userid = self.libraryBrowser.find_element_by_id('userid')
        password = self.libraryBrowser.find_element_by_id('password')

        userid.send_keys(self.ID)
        password.send_keys(self.password)

        self.libraryBrowser.find_element_by_class_name('submit').submit()

    def run(self):
        self.check_login()
        self.emit(SIGNAL('log_in(QString)'), 'logging in')
        self.sleep(2)

