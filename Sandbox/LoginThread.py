from PyQt4.QtCore import QStringList
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

        self.number_of_books = 0
        self.book_info = ''
        self.book_info_list = []

    def __del__(self):
        self.wait()

    def check_login(self):
        #emits signal for logging in
        self.emit(SIGNAL('update_status(QString)'), 'Trying to log in ... be patient')

        # browser
        # Use phantomjs for release
        self.libraryBrowser = webdriver.PhantomJS('C:\Users\Manash\Downloads\Compressed\phantomjs\phantomjs.exe')

        # Use Chrome as default engine
        # self.libraryBrowser = webdriver.Chrome()

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
            self.sleep(1)
            book_info_list = self.get_book_data()
            book_info_list_qstring = QStringList(book_info_list)
            self.emit(SIGNAL('fetch_book_data(QStringList)'), book_info_list_qstring)
            self.libraryBrowser.close()


    # Returns QStringList
    def get_book_data(self):
        parent_tbody = self.libraryBrowser.find_element_by_tag_name('tbody')


        for child in parent_tbody.find_elements_by_tag_name('tr'):
            self.number_of_books += 1

            title = child.find_element_by_class_name('title').text
            date_due = child.find_element_by_class_name('date_due').text
            call_no = child.find_element_by_class_name('call_no').text
            renewals = child.find_element_by_class_name('renew').text

            # Makes a dict type string
            self.book_info = "{ 'title' : '" + title + "',"
            self.book_info += "'date_due' : '"  + date_due + "', "
            self.book_info += "'call_no' : '" + call_no  + "', "
            self.book_info += "'renewals' : '" + renewals + "' }"

            self.book_info_list.append(self.book_info)

        return self.book_info_list




    def run(self):
        self.check_login()
        self.sleep(2)

