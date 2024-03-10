# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Git Projects\PYGT5\GUI-Design-PYQT\videoDatabase.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1072, 395)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QLabel#lblMainTitle, Spacer#titleVerticalSpacer{\n"
"background-color:rgb(0, 255, 255);}\n"
"\n"
"#lblTitleData, #lblStudioData, #lblReleaseDateData, #lblClassificationData{\n"
"background-color:rgb(170, 170, 255);\n"
"font: 10pt \"Arial\";\n"
"margin-top:5px;\n"
"\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"background:rgb(192,182,238);\n"
"    font: 75 11pt \"Arial\";\n"
"color:\"black\";\n"
"}\n"
"QPushButton{\n"
"background:rgb(0, 0, 127);\n"
"    \n"
"    font: 75 11pt \"Arial\";\n"
"color:rgb(170, 255, 255);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 1021, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblMainTitle = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lblMainTitle.setFont(font)
        self.lblMainTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMainTitle.setObjectName("lblMainTitle")
        self.verticalLayout_2.addWidget(self.lblMainTitle)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.titleField = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.titleField.setFont(font)
        self.titleField.setObjectName("titleField")
        self.horizontalLayout.addWidget(self.titleField)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.studioField = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.studioField.setFont(font)
        self.studioField.setObjectName("studioField")
        self.horizontalLayout.addWidget(self.studioField)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.releaseField = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.releaseField.setFont(font)
        self.releaseField.setObjectName("releaseField")
        self.horizontalLayout.addWidget(self.releaseField)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.classificationField = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.classificationField.setFont(font)
        self.classificationField.setObjectName("classificationField")
        self.horizontalLayout.addWidget(self.classificationField)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(2, 3)
        self.horizontalLayout.setStretch(4, 4)
        self.horizontalLayout.setStretch(6, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblTitleData = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblTitleData.setObjectName("lblTitleData")
        self.horizontalLayout_2.addWidget(self.lblTitleData)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.lblStudioData = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblStudioData.setObjectName("lblStudioData")
        self.horizontalLayout_2.addWidget(self.lblStudioData)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.lblReleaseDateData = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblReleaseDateData.setObjectName("lblReleaseDateData")
        self.horizontalLayout_2.addWidget(self.lblReleaseDateData)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.lblClassificationData = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblClassificationData.setObjectName("lblClassificationData")
        self.horizontalLayout_2.addWidget(self.lblClassificationData)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 1)
        self.horizontalLayout_2.setStretch(4, 2)
        self.horizontalLayout_2.setStretch(5, 1)
        self.horizontalLayout_2.setStretch(6, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(460, 330, 75, 23))
        self.btnClose.setObjectName("btnClose")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1072, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblMainTitle.setText(_translate("MainWindow", "Films Database"))
        self.titleField.setText(_translate("MainWindow", "Title"))
        self.studioField.setText(_translate("MainWindow", "Studio"))
        self.releaseField.setText(_translate("MainWindow", "Release Date"))
        self.classificationField.setText(_translate("MainWindow", "Classification"))
        self.lblTitleData.setText(_translate("MainWindow", "titleData"))
        self.lblStudioData.setText(_translate("MainWindow", "studioData"))
        self.lblReleaseDateData.setText(_translate("MainWindow", "releaseDateData"))
        self.lblClassificationData.setText(_translate("MainWindow", "classificationData"))
        self.btnClose.setText(_translate("MainWindow", "Close"))
