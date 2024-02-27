# import required modules
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

# create the widget class - each window must have its own class


class Ui(QtWidgets.QMainWindow):
    """Window class based on the ui xml file created in QT Designer"""

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("login.ui", self)

        # add button event listeners
        self.btnLogin.clicked.connect(self.loginButtonMethod)
        self.btnClear.clicked.connect(self.clearButtonMethod)
        # show the window
        self.show()

    # button event handlers
    def loginButtonMethod(self):
        """handles the events initiated by the login button"""
        print("login button was clicked")

    def clearButtonMethod(self):
        """handles the clear button events"""
        print("clear button was clicked")


def mainApplication():
    """Main application that will load the window instance"""
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()


mainApplication()
