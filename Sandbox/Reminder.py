from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QTableWidget, QTableWidgetItem

ui_reminder = 'design/ui_reminder.ui'

Ui_ReminderWidget, Ui_ReminderBaseClass = uic.loadUiType(ui_reminder)

class Reminder(QtGui.QWidget, Ui_ReminderWidget):
    def __init__(self, book_info_dicts):

        self.book_info_dicts = book_info_dicts

        #init ui
        QtGui.QWidget.__init__(self)
        Ui_ReminderWidget.__init__(self)
        self.setupUi(self)

        self.bookInfoTable.setRowCount(len(book_info_dicts))

        self.init_ui()

    def init_ui(self):
        for row, item in enumerate (self.book_info_dicts):
            self.bookInfoTable.setItem(row, 0, QTableWidgetItem(item['title']))
            self.bookInfoTable.setItem(row, 1, QTableWidgetItem(item['date_due']))
            self.bookInfoTable.setItem(row, 2, QTableWidgetItem(item['call_no']))
            self.bookInfoTable.setItem(row, 3, QTableWidgetItem(item['renewals']))

    def __del__(self):
        del self.book_info_dicts