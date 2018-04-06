# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiUserPage.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UserWindow(object):
    def setupUi(self, UserWindow):
        UserWindow.setObjectName("UserWindow")
        UserWindow.resize(1360, 730)
        UserWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(UserWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
"    background-image: url(:/UserPage/images/greyMetal.jpg);\n"
"    \n"
"\n"
"}\n"
"QTableWidget#tableWidget_Recording{\n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-10, 80, 1381, 611))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_video_tab = QtWidgets.QWidget()
        self.page_video_tab.setObjectName("page_video_tab")
        self.label_player = QtWidgets.QLabel(self.page_video_tab)
        self.label_player.setGeometry(QtCore.QRect(20, 10, 640, 480))
        self.label_player.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 0, 0);")
        self.label_player.setText("")
        self.label_player.setObjectName("label_player")
        self.line_2 = QtWidgets.QFrame(self.page_video_tab)
        self.line_2.setGeometry(QtCore.QRect(660, 10, 20, 481))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(self.page_video_tab)
        self.line.setGeometry(QtCore.QRect(1080, 10, 20, 481))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.page_video_tab)
        self.layoutWidget.setGeometry(QtCore.QRect(1100, 10, 258, 481))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidgetResults = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidgetResults.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.listWidgetResults.setObjectName("listWidgetResults")
        self.gridLayout.addWidget(self.listWidgetResults, 1, 0, 1, 1)
        self.label_prediction = QtWidgets.QLabel(self.layoutWidget)
        self.label_prediction.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(180, 0, 0);\n"
"background-color: rgb(170, 255, 255);")
        self.label_prediction.setAlignment(QtCore.Qt.AlignCenter)
        self.label_prediction.setObjectName("label_prediction")
        self.gridLayout.addWidget(self.label_prediction, 0, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.page_video_tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(720, 11, 321, 361))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit_gpsIp = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_gpsIp.setObjectName("lineEdit_gpsIp")
        self.gridLayout_5.addWidget(self.lineEdit_gpsIp, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_5.addWidget(self.lineEdit_3, 2, 1, 1, 2)
        self.pushButton_GpsCon = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_GpsCon.setObjectName("pushButton_GpsCon")
        self.gridLayout_5.addWidget(self.pushButton_GpsCon, 3, 0, 1, 1)
        self.label_gpsStatus = QtWidgets.QLabel(self.layoutWidget1)
        self.label_gpsStatus.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_gpsStatus.setText("")
        self.label_gpsStatus.setObjectName("label_gpsStatus")
        self.gridLayout_5.addWidget(self.label_gpsStatus, 3, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 4, 0, 1, 3)
        self.pushButton_AlgoInit = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_AlgoInit.setObjectName("pushButton_AlgoInit")
        self.gridLayout_5.addWidget(self.pushButton_AlgoInit, 5, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 255, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 6, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 3)
        self.pushButton_ChangeOpDir = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_ChangeOpDir.setObjectName("pushButton_ChangeOpDir")
        self.gridLayout_5.addWidget(self.pushButton_ChangeOpDir, 8, 1, 1, 1)
        self.label_AlgoInit = QtWidgets.QLabel(self.layoutWidget1)
        self.label_AlgoInit.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_AlgoInit.setText("")
        self.label_AlgoInit.setObjectName("label_AlgoInit")
        self.gridLayout_5.addWidget(self.label_AlgoInit, 5, 1, 1, 2)
        self.label_outputDir = QtWidgets.QLabel(self.layoutWidget1)
        self.label_outputDir.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_outputDir.setText("")
        self.label_outputDir.setObjectName("label_outputDir")
        self.gridLayout_5.addWidget(self.label_outputDir, 7, 0, 1, 3)
        self.layoutWidget2 = QtWidgets.QWidget(self.page_video_tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 502, 641, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_msg = QtWidgets.QLabel(self.layoutWidget2)
        self.label_msg.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"")
        self.label_msg.setText("")
        self.label_msg.setObjectName("label_msg")
        self.horizontalLayout.addWidget(self.label_msg)
        self.pushButton_start = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout.addWidget(self.pushButton_start)
        self.pushButton_stop = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalLayout.addWidget(self.pushButton_stop)
        self.pushButton_startRec = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_startRec.setObjectName("pushButton_startRec")
        self.horizontalLayout.addWidget(self.pushButton_startRec)
        self.pushButton_stopRec = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_stopRec.setObjectName("pushButton_stopRec")
        self.horizontalLayout.addWidget(self.pushButton_stopRec)
        self.layoutWidget3 = QtWidgets.QWidget(self.page_video_tab)
        self.layoutWidget3.setGeometry(QtCore.QRect(721, 391, 321, 131))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_4.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_5.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.pushButton_SendAlert = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_SendAlert.setObjectName("pushButton_SendAlert")
        self.verticalLayout_2.addWidget(self.pushButton_SendAlert)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.label_player.raise_()
        self.layoutWidget.raise_()
        self.line_2.raise_()
        self.line.raise_()
        self.stackedWidget.addWidget(self.page_video_tab)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.tableWidget_Recording = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget_Recording.setGeometry(QtCore.QRect(670, 10, 411, 291))
        self.tableWidget_Recording.setStyleSheet("")
        self.tableWidget_Recording.setObjectName("tableWidget_Recording")
        self.tableWidget_Recording.setColumnCount(4)
        self.tableWidget_Recording.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Recording.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Recording.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Recording.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Recording.setHorizontalHeaderItem(3, item)
        self.label_opdirtext = QtWidgets.QLabel(self.page_2)
        self.label_opdirtext.setGeometry(QtCore.QRect(770, 320, 311, 21))
        self.label_opdirtext.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_opdirtext.setText("")
        self.label_opdirtext.setObjectName("label_opdirtext")
        self.pushButton_FileDialog = QtWidgets.QPushButton(self.page_2)
        self.pushButton_FileDialog.setGeometry(QtCore.QRect(670, 320, 91, 23))
        self.pushButton_FileDialog.setObjectName("pushButton_FileDialog")
        self.label_player_2 = QtWidgets.QLabel(self.page_2)
        self.label_player_2.setGeometry(QtCore.QRect(20, 10, 640, 480))
        self.label_player_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 0, 0);")
        self.label_player_2.setText("")
        self.label_player_2.setObjectName("label_player_2")
        self.pushButton_vstop = QtWidgets.QPushButton(self.page_2)
        self.pushButton_vstop.setGeometry(QtCore.QRect(410, 540, 75, 23))
        self.pushButton_vstop.setObjectName("pushButton_vstop")
        self.pushButton_play = QtWidgets.QPushButton(self.page_2)
        self.pushButton_play.setGeometry(QtCore.QRect(250, 540, 75, 23))
        self.pushButton_play.setObjectName("pushButton_play")
        self.comboBox = QtWidgets.QComboBox(self.page_2)
        self.comboBox.setGeometry(QtCore.QRect(770, 370, 131, 21))
        self.comboBox.setObjectName("comboBox")
        self.label_date = QtWidgets.QLabel(self.page_2)
        self.label_date.setGeometry(QtCore.QRect(670, 370, 91, 21))
        self.label_date.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 170, 255);")
        self.label_date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date.setObjectName("label_date")
        self.pushButton_show = QtWidgets.QPushButton(self.page_2)
        self.pushButton_show.setGeometry(QtCore.QRect(920, 370, 75, 23))
        self.pushButton_show.setObjectName("pushButton_show")
        self.pushButton_today = QtWidgets.QPushButton(self.page_2)
        self.pushButton_today.setGeometry(QtCore.QRect(1000, 370, 75, 23))
        self.pushButton_today.setObjectName("pushButton_today")
        self.horizontalSlider = QtWidgets.QSlider(self.page_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(120, 510, 531, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.line_3 = QtWidgets.QFrame(self.page_2)
        self.line_3.setGeometry(QtCore.QRect(1080, 10, 16, 481))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.layoutWidget_2 = QtWidgets.QWidget(self.page_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(1100, 10, 258, 481))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_prediction_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_prediction_2.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(180, 0, 0);\n"
"background-color: rgb(170, 255, 255);")
        self.label_prediction_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_prediction_2.setObjectName("label_prediction_2")
        self.gridLayout_2.addWidget(self.label_prediction_2, 0, 0, 1, 1)
        self.listWidgetResults_2 = QtWidgets.QListWidget(self.layoutWidget_2)
        self.listWidgetResults_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.listWidgetResults_2.setObjectName("listWidgetResults_2")
        self.gridLayout_2.addWidget(self.listWidgetResults_2, 1, 0, 1, 1)
        self.label_frameno = QtWidgets.QLabel(self.page_2)
        self.label_frameno.setGeometry(QtCore.QRect(20, 510, 91, 21))
        self.label_frameno.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_frameno.setText("")
        self.label_frameno.setObjectName("label_frameno")
        self.pushButton_pause = QtWidgets.QPushButton(self.page_2)
        self.pushButton_pause.setGeometry(QtCore.QRect(330, 540, 75, 23))
        self.pushButton_pause.setObjectName("pushButton_pause")
        self.stackedWidget.addWidget(self.page_2)
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(500, 9, 280, 61))
        self.label_logo.setStyleSheet("background-color: rgb(208, 208, 208);\n"
"\n"
"background-image: url(:/UserPage/images/hawkeye_logo.png);")
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.pushButton_page1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_page1.setGeometry(QtCore.QRect(11, 11, 91, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_page1.sizePolicy().hasHeightForWidth())
        self.pushButton_page1.setSizePolicy(sizePolicy)
        self.pushButton_page1.setStyleSheet("background-image: url(:/UserPage/images/video-icon.jpg);\n"
"")
        self.pushButton_page1.setText("")
        self.pushButton_page1.setFlat(False)
        self.pushButton_page1.setObjectName("pushButton_page1")
        self.pushButton_page2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_page2.setGeometry(QtCore.QRect(110, 10, 91, 61))
        self.pushButton_page2.setObjectName("pushButton_page2")
        self.pushButton_logout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_logout.setGeometry(QtCore.QRect(1210, 20, 111, 31))
        self.pushButton_logout.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 75 12pt \"Arial\";")
        self.pushButton_logout.setObjectName("pushButton_logout")
        UserWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UserWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1360, 21))
        self.menubar.setObjectName("menubar")
        UserWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UserWindow)
        self.statusbar.setObjectName("statusbar")
        UserWindow.setStatusBar(self.statusbar)

        self.retranslateUi(UserWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(UserWindow)

    def retranslateUi(self, UserWindow):
        _translate = QtCore.QCoreApplication.translate
        UserWindow.setWindowTitle(_translate("UserWindow", "HawkEye"))
        self.label_prediction.setText(_translate("UserWindow", "Prediction"))
        self.label.setText(_translate("UserWindow", "Gps Ip Adrress:"))
        self.label_3.setText(_translate("UserWindow", "Gps Port No:"))
        self.pushButton_GpsCon.setText(_translate("UserWindow", "Connect"))
        self.label_8.setText(_translate("UserWindow", "Initialize Video System "))
        self.pushButton_AlgoInit.setText(_translate("UserWindow", "Initialize"))
        self.label_9.setText(_translate("UserWindow", "Output Folder Location"))
        self.label_2.setText(_translate("UserWindow", "Gps Setting"))
        self.pushButton_ChangeOpDir.setText(_translate("UserWindow", "Change Output Folder"))
        self.pushButton_start.setText(_translate("UserWindow", "Start"))
        self.pushButton_stop.setText(_translate("UserWindow", "Stop"))
        self.pushButton_startRec.setText(_translate("UserWindow", "Start Rec"))
        self.pushButton_stopRec.setText(_translate("UserWindow", "Stop Rec"))
        self.label_4.setText(_translate("UserWindow", "Alert Message"))
        self.label_5.setText(_translate("UserWindow", "Location Sent:"))
        self.pushButton_SendAlert.setText(_translate("UserWindow", "Send Alert"))
        item = self.tableWidget_Recording.horizontalHeaderItem(0)
        item.setText(_translate("UserWindow", "File Name"))
        item = self.tableWidget_Recording.horizontalHeaderItem(1)
        item.setText(_translate("UserWindow", "Date/Time"))
        item = self.tableWidget_Recording.horizontalHeaderItem(2)
        item.setText(_translate("UserWindow", "Size"))
        item = self.tableWidget_Recording.horizontalHeaderItem(3)
        item.setText(_translate("UserWindow", "Duration"))
        self.pushButton_FileDialog.setText(_translate("UserWindow", "OutPut Folder"))
        self.pushButton_vstop.setText(_translate("UserWindow", "Stop"))
        self.pushButton_play.setText(_translate("UserWindow", "Play"))
        self.label_date.setText(_translate("UserWindow", "Date Select"))
        self.pushButton_show.setText(_translate("UserWindow", "Show"))
        self.pushButton_today.setText(_translate("UserWindow", "Today"))
        self.label_prediction_2.setText(_translate("UserWindow", "Prediction"))
        self.pushButton_pause.setText(_translate("UserWindow", "Pause"))
        self.pushButton_page2.setText(_translate("UserWindow", "Player"))
        self.pushButton_logout.setText(_translate("UserWindow", "Logout"))

from resource.qrc import UserPage_rc
