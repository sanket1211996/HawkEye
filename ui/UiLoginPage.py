# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiLoginPage.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(514, 352)
        MainWindow.setMinimumSize(QtCore.QSize(514, 352))
        MainWindow.setMaximumSize(QtCore.QSize(514, 352))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 20, 281, 71))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-image: url(:/images/images/hawkeye_logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(110, 110, 281, 151))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelUserName = QtWidgets.QLabel(self.widget)
        self.labelUserName.setObjectName("labelUserName")
        self.gridLayout.addWidget(self.labelUserName, 0, 0, 1, 1)
        self.lineEdit_UserName = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_UserName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_UserName.setObjectName("lineEdit_UserName")
        self.gridLayout.addWidget(self.lineEdit_UserName, 0, 1, 1, 1)
        self.labelPassword = QtWidgets.QLabel(self.widget)
        self.labelPassword.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelPassword.setObjectName("labelPassword")
        self.gridLayout.addWidget(self.labelPassword, 1, 0, 1, 1)
        self.lineEdit_Password = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_Password.setAutoFillBackground(False)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.gridLayout.addWidget(self.lineEdit_Password, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.labelUserType = QtWidgets.QLabel(self.widget)
        self.labelUserType.setObjectName("labelUserType")
        self.gridLayout.addWidget(self.labelUserType, 2, 0, 1, 1)
        self.comboBox_UserType = QtWidgets.QComboBox(self.widget)
        self.comboBox_UserType.setObjectName("comboBox_UserType")
        self.comboBox_UserType.addItem("")
        self.comboBox_UserType.addItem("")
        self.gridLayout.addWidget(self.comboBox_UserType, 2, 1, 1, 1)
        self.pushButton_Login = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Login.sizePolicy().hasHeightForWidth())
        self.pushButton_Login.setSizePolicy(sizePolicy)
        self.pushButton_Login.setStyleSheet("background-image: url(:/images/images/LoginButtonLogo.jpg);\n"
"")
        self.pushButton_Login.setText("")
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.gridLayout.addWidget(self.pushButton_Login, 3, 1, 1, 1)
        self.labelUserName.raise_()
        self.labelPassword.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelUserName.setText(_translate("MainWindow", "   Username "))
        self.labelPassword.setText(_translate("MainWindow", "  Password "))
        self.labelUserType.setText(_translate("MainWindow", "  User Type "))
        self.comboBox_UserType.setItemText(0, _translate("MainWindow", "Admin Login"))
        self.comboBox_UserType.setItemText(1, _translate("MainWindow", "Officer Login"))

from resource.qrc import LoginPage_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

