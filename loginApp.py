# import required modules
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import sqlite3
from PyQt5.QtCore import Qt

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
        print(
            f"username: {enteredUsername} | password: {enteredPassword}"
        )  # only for testing purposes

        # perform validation  - presence check and display appropriate message box
        if enteredPassword == "" or enteredUsername == "":
            messageBoxHandler(
                "Blank fields detected!",
                "Password and username must be entered",
                "warning",
            )
        else:
            # connect to the database and validate the credentials
            query = f"""Select password FROM users WHERE username=?"""
            data = executeStatementHelper(query, args=(enteredUsername,))
            # clear clear fields
            self.clearButtonMethod()
            print(data)  # check return data
            # handle login
            try:
                if data[0][0] == enteredPassword:
                    messageBoxHandler("Logon Success", "You logged in successfully")
                    self.close()
                else:
                    messageBoxHandler(
                        "Login attempt failed",
                        "Incorrect username or password",
                        "warning",
                    )
            except IndexError:
                messageBoxHandler("Login attempt failed", "try again", "warning")

    def clearButtonMethod(self):
        """handles the clear button events"""
        # print("clear button was clicked")
        self.userNameInput.setText("")
        self.passwordInput.setText("")

    # adding key bindings with keyPressEvent
    def keyPressEvent(self, e):
        """This method handles keyboard button events"""
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_Return:
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


# connecting to the database
def dbConnection():
    conn = sqlite3.connect("usersAndFilms.db")
    cur = conn.cursor()
    return (conn, cur)


def executeStatementHelper(query, args=None):
    "connects and executes a given query"
    conn, cur = dbConnection()
    if not args:
        cur.execute(query)
    else:
        cur.execute(query, args)
    # fetch data
    selectedData = cur.fetchall()
    conn.commit()
    conn.close()
    return selectedData


def mainApplication():
    """Main application that will load the window instance"""
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())

mainApplication()
