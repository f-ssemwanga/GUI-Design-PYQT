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
        # print("login button was clicked")I
        # access data in form fields
        enteredUsername = self.userNameInput.text().lower()
        enteredPassword = self.passwordInput.text()

        # print(f"username: {enteredUsername} | password: {enteredPassword}") #check message box connection
        # messageBoxHandler("Login Feedback", "login Button clicked", "warning")

        # perform validation  - presence check on the message box
        if enteredPassword == "" or enteredPassword == "":
            messageBoxHandler(
                "Blank field detected!",
                "Password and username must be entered",
                "warning",
            )
        else:
            messageBoxHandler("Login Feedback", "login Button clicked", "warning")

    def clearButtonMethod(self):
        """handles the clear button events"""
        # print("clear button was clicked")
        self.userNameInput.setText("")
        self.passwordInput.setText("")

    # adding key bindings with keyPressEvent
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
        elif e.key() == QtCore.Qt.Key_Return:
            self.loginButtonMethod()


def messageBoxHandler(title, content, iconType="info"):
    """message box that display warnings"""
    msgBox = QtWidgets.QMessageBox()  # messagebox object
    # set icon type based on passed icon flag
    if iconType == "info":
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
    elif iconType == "question":
        msgBox.setIcon(QtWidgets.QMessageBox.Question)
    elif iconType == "warning":
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
    else:
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
    # set title and content
    msgBox.setText(content)
    msgBox.setWindowTitle(title)
    # show the message Box
    msgBox.exec_()


def mainApplication():
    """Main application that will load the window instance"""
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()


mainApplication()
