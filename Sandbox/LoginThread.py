from PyQt4 import QtGui
from PyQt4.QtCore import QThread, SIGNAL
from selenium import webdriver
import time
import re

import sys


class LoginThread(QThread):
    def __init__(self, ID, password):
        QThread.__init__(self)
        self.ID = str(ID)
        self.password = str(password)

        #library url
        self.libraryUrl = 'http://library.kuet.ac.bd'
        self.loggedIn = False


    def __del__(self):
        self.wait()

    def check_login(self):
        #emits signal for logging in
        self.emit(SIGNAL('update_status(QString)'), 'Trying to log in ... be patient')

        # browser
        # Use phantomjs for release
        #self.libraryBrowser = webdriver.PhantomJS('C:\Users\Manash\Downloads\Compressed\phantomjs\phantomjs.exe')

        # Use Chrome as default engine
        self.libraryBrowser = webdriver.Chrome()

        self.libraryBrowser.get(self.libraryUrl)
        time.sleep(1)

        userid = self.libraryBrowser.find_element_by_id('userid')
        password = self.libraryBrowser.find_element_by_id('password')

        userid.send_keys(self.ID)
        password.send_keys(self.password)

        self.libraryBrowser.find_element_by_class_name('submit').submit()

        web_element = self.libraryBrowser.find_elements_by_tag_name('p')

        self.loggedIn = not (True in ['incorrect' in item.text for item in web_element])

        if not self.loggedIn:
            self.emit(SIGNAL('update_status(QString)'), 'ID or password is incorrect, try again')
            self.libraryBrowser.close()
        else:
            self.emit(SIGNAL('update_status(QString)'), 'Successfully logged in')
            self.get_book_data()


    def get_book_data(self):
        parent_tbody = self.libraryBrowser.find_element_by_tag_name('tbody')
        child_tr = parent_tbody.find_elements_by_tag_name('tr')
        

        for item in child_tr:
            print item.text



    def run(self):
        self.check_login()
        self.sleep(2)

