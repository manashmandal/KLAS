from PyQt4 import QtGui, QtCore, uic
import sys
from PyQt4.QtGui import QTableWidget
from PyQt4.QtGui import QTableWidgetItem

TestTableWidget, TestTableBaseClass = uic.loadUiType('ui_tablewidget.ui')

class TestTable(QtGui.QWidget, TestTableWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        TestTableWidget.__init__(self)
        self.setupUi(self)



        self.dictionary = [{'title': 'C++', 'call_no' : 'C01', 'due_date':'01-01-1995', 'renew' : '4'},
                           {'title': 'C#', 'call_no': 'C02', 'due_date': '02-01-1995', 'renew': '3'}]

        self.tableWidget.setRowCount(len(self.dictionary))

        self.add_item()




    def add_item(self):
        print "adding"
        for row, item in enumerate(self.dictionary):
            print item['title']
            title = QTableWidgetItem(item['title'])
            self.tableWidget.setItem(row, 1, title)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    table = TestTable()
    table.show()
    sys.exit(app.exec_())