import  time
from resource.darkflow.darkflow.net.build import TFNet
import numpy as np
import datetime
import re
import sys,os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from numpy.testing.tests.test_utils import my_cacw
import subprocess
import pyttsx3
import MySQLdb
from ui.UiUserPage import Ui_UserWindow
import cv2
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer
from mutagen.mp4 import MP4
from playsound import playsound
import threading
import time
from source.ThreadSound import ThreadingExample

class UserMain(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui =Ui_UserWindow()
        self.ui.setupUi(self)
        self.out=None
        self.Vheight=640
        self.Vwidth=480
        self.flag=-1       #Flag for 1 -recording  -1 for no recodring and 0 for stop recording
        #s
        self.engine = pyttsx3.init()
        self.DisplayDateList()



        # elf.ui.webView.load(QtCore.QUrl("D:/Project/HawkEye/html/map.html"))
        self.fourcc=None
        self.outDir="D:\\Project\\HawkEye\\video"
        self.ui.label_opdirtext.setText(self.outDir)
        #self.ui.label_player.setPixmap(QPixmap("D:\\Project\\HawkEye\\resource\\images\\playerbackground.png"))
        self.setEnabledButtonOnCreate()
        #self.updateTable()
        self.algo_init()
        self.ButtonConnectOnCreate()
        self.ButtonDConnectOnCreate()

    def run(self):
        while True:
            # Do something
            print('Doing something imporant in the background')
            engine = pyttsx3.init()
            engine.say("Human Detected")
            engine.runAndWait()
            time.sleep(1)  #Sleep Interval


    def algo_init(self):
        options = {"model": "D:/Project/HawkEye/resource/darkflow/cfg/tiny-yolo-voc.cfg",
                   "load": "D:/Project/HawkEye/resource/darkflow/bin/tiny-yolo-voc.weights",
                   "threshold": 0.5, "gpu": 0.5}
        ####################################################################################
        self.tfnet = TFNet(options)
        self.colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]

    def ButtonDConnectOnCreate(self):
        self.ui.tableWidget_Recording.doubleClicked.connect(self.on_DClickTable)

    def ButtonConnectOnCreate(self):
        self.ui.pushButton_page1.clicked.connect(self.onClickBtnPage1)
        self.ui.pushButton_page2.clicked.connect(self.onClickBtnPage2)
        self.ui.pushButton_FileDialog.clicked.connect(self.DisplayTable)
        self.ui.pushButton_start.clicked.connect(self.start)
        self.ui.pushButton_stop.clicked.connect(self.stop)
        self.ui.pushButton_startRec.clicked.connect(self.startRecord)
        self.ui.pushButton_stopRec.clicked.connect(self.stopRecord)
        self.ui.pushButton_vstop.clicked.connect(self.vstop)
        self.ui.pushButton_show.clicked.connect(self.DisplayTable)
        self.ui.pushButton_today.clicked.connect(self.Today)


    def setEnabledButtonOnCreate(self):
        self.ui.pushButton_stop.setEnabled(False)
        self.ui.pushButton_startRec.setEnabled(False)
        self.ui.pushButton_stopRec.setEnabled(False)
        self.ui.pushButton_play.setEnabled(False)
        self.ui.pushButton_start.setEnabled(True)
        self.ui.pushButton_vstop.setEnabled(False)
        #self.ui.pushButton_prev.setEnabled(False)
       #self.ui.pushButton_next.setEnabled(False)


    def onClickBtnPage1(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def onClickBtnPage2(self):
        self.ui.stackedWidget.setCurrentIndex(1)

#video player method
    def start(self):
        self.flag=-1

        self.ui.pushButton_startRec.setEnabled(True)
        self.ui.pushButton_stop.setEnabled(True)

        self.capture = cv2.VideoCapture(0)   #0 for internal webcam 1 for external camera
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.timer =QTimer()
        self.timer.timeout.connect(self.refresh_frame)
        self.timer.start(5)
        self.ui.label_msg.setText("Streaming...")

    def stop(self):
        self.timer.stop()
        self.capture.release()
        cv2.destroyAllWindows()
        self.ui.pushButton_startRec.setEnabled(False)
        self.ui.pushButton_stopRec.setEnabled(False)
        self.ui.pushButton_stop.setEnabled(False)
        self.ui.label_player.setPixmap(QPixmap("D:\\Project\\HawkEye\\resource\\images\\playerbackground.png"))
        self.ui.label_msg.setText("Streaming Stopped")


    def startRecord(self):

        self.flag=1
        # Initilizing for recording
        varDate = datetime.datetime.now()
        datetoday = str(varDate.day) + "." + str(varDate.month) + "." + str(varDate.year)
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec
        fileName=self.getOutFileName()
        OutFilePath = os.path.join(self.outDir,fileName)
        self.out = cv2.VideoWriter(OutFilePath, self.fourcc, 5.0, (int(self.Vheight), int(self.Vwidth)))
        self.DBconnection()
        userListQuery = "INSERT INTO videoDatabase VALUES (\""+fileName+"\",\""+datetoday+"\")"
        self.db_Cursor.execute(userListQuery)
        self.db_Object.commit()
        self.DBDisconnect()
        self.DisplayDateList()
        self.ui.pushButton_startRec.setEnabled(False)
        self.ui.pushButton_stopRec.setEnabled(True)
        self.ui.label_msg.setText("Recording Started")



    def stopRecord(self):
        self.flag=0
        self.ui.pushButton_stopRec.setEnabled(False)
        self.ui.pushButton_startRec.setEnabled(True)
        self.ui.label_msg.setText("Recording Stopped")




    def refresh_frame(self):

        outputtext=""
        ret, self.image = self.capture.read()
        self.image = cv2.flip(self.image, 1)
        #IMAGE PROCESSING CODE GOES HERE
        frame = self.image
        results = self.tfnet.return_predict(frame)
        if ret:
            for color, result in zip(self.colors, results):
                tl = (result['topleft']['x'], result['topleft']['y'])
                br = (result['bottomright']['x'], result['bottomright']['y'])
                label = result['label']
                confidence = result['confidence']
                text = '{}: {:.0f}%'.format(label, confidence * 100)
                frame = cv2.rectangle(frame, tl, br, color, 5)
                frame = cv2.putText(frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                outputtext+="\n"+text
                #if(label=="person" and confidence>0.5):
                    #example = ThreadingExample(1)
            self.displayPrediction(outputtext)
            self.image=frame
        else :
            self.stop()
        ###### Image Processing Ends
        if self.flag==1 :
            self.out.write(self.image)
        elif self.flag==0 :
                self.out.release()
        self.displayImage(self.image)

    def displayPrediction(self,text):
        self.ui.label_optext.setText(text)
        return


    def AlertMessage(self):
        self.engine.say("Human Detected")
        self.engine.runAndWait()
#        playsound("D:\\Project\\HawkEye\\resource\\sound\\HumanDetected.mp3")

    def displayImage(self, img):
        qFormat = QImage.Format_Indexed8
        if (len(img.shape)) == 3:
            if img.shape[2] == 4:
                qFormat = QImage.Format_RGBA8888
            else:
                qFormat = QImage.Format_RGB888

        outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qFormat)
        # BGR>>RGB
        outImage = outImage.rgbSwapped()
        self.ui.label_player.setPixmap(QPixmap.fromImage(outImage))
        self.ui.label_player.setScaledContents(True)
################################PAGE 2 ######################################

    def DBconnection(self):
        # Open database connection
        self.db_Object = MySQLdb.connect("localhost", "root", "root", "hawkeye") #database ip,username,password,database name
        # prepare a cursor object using cursor() method
        self.db_Cursor = self.db_Object.cursor()

    def play(self, filename):
        self.flag = -1
        self.capture = cv2.VideoCapture(filename)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh_frame2)
        self.timer.start(100)

    def vstop(self):
        self.timer.stop()
        self.capture.release()
        cv2.destroyAllWindows()
        self.setEnabledButtonOnCreate()
        self.ui.label_player_2.setPixmap(QPixmap("D:\\Project\\HawkEye\\resource\\images\\playerbackground.png"))

    def refresh_frame2(self):
        ret, self.image = self.capture.read()
        if ret:
        # IMAGE PROCESSING CODE GOES HERE
            self.displayImage2(self.image)
        else:
            self.stop()

    def displayImage2(self, img):
        qFormat = QImage.Format_Indexed8
        if (len(img.shape)) == 3:
            if img.shape[2] == 4:
                qFormat = QImage.Format_RGBA8888
            else:
                qFormat = QImage.Format_RGB888

        outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qFormat)
        # BGR>>RGB
        outImage = outImage.rgbSwapped()
        self.ui.label_player_2.setPixmap(QPixmap.fromImage(outImage))
        self.ui.label_player_2.setScaledContents(True)



##################
    def on_DClickTable(self):
        self.ui.pushButton_stop.setEnabled(False)
        self.ui.pushButton_start.setEnabled(False)
        self.ui.pushButton_startRec.setEnabled(False)
        self.ui.pushButton_stopRec.setEnabled(False)

        self.ui.pushButton_play.setEnabled(True)
        #self.ui.pushButton_pause.setEnabled(True)
        self.ui.pushButton_vstop.setEnabled(True)
        #self.ui.pushButton_prev.setEnabled(True)
        #self.ui.pushButton_next.setEnabled(True)

        for currentQTableWidgetItem in self.ui.tableWidget_Recording.selectedItems():
            self.currentFile =self.outDir+"/"+currentQTableWidgetItem.text()
            print(self.currentFile)
            self.play(self.currentFile)

    def DisplayTable(self):
        self.DBconnection()  # Check Exception need
        currentDate = self.ui.comboBox.currentText()
        userListQuery = "SELECT fileName,date FROM videoDatabase where date=\""+currentDate+"\""
        self.db_Cursor.execute(userListQuery)
        results = self.db_Cursor.fetchall()
        self.ui.tableWidget_Recording.clearContents()
        self.ui.tableWidget_Recording.setRowCount(0);
        numRows = 0

        if not results:
            msg = QtWidgets.QMessageBox()
            msg.about(self, "Error", "Data Not Found")

        for row in results:
            fileName=row[0]
            date_info = row[1]
            filepath = self.outDir + "/" + fileName
            filesize = os.path.getsize(filepath) / (1024 * 1024)
            filesize = '{:.0f}'.format(filesize)
            filesize = filesize + "Mb"

            self.ui.tableWidget_Recording.insertRow(numRows)
            self.ui.tableWidget_Recording.setItem(numRows,0, QtWidgets.QTableWidgetItem(fileName))
            self.ui.tableWidget_Recording.setItem(numRows, 1, QtWidgets.QTableWidgetItem(date_info))
            self.ui.tableWidget_Recording.setItem(numRows, 2, QtWidgets.QTableWidgetItem(filesize))
            numRows=numRows+1

        self.DBDisconnect()

       # self.outDir = self.getOutputDir()  #######################Error HERE
        #self.ui.tableWidget_Recording.clearContents()
        #self.numRows=0
        #self.dirList = os.listdir(self.outDir)
        #for self.file in self.dirList:
          #  self.ui.tableWidget_Recording.insertRow(self.numRows)
         #   self.ui.tableWidget_Recording.setItem(self.numRows,0, QtWidgets.QTableWidgetItem(self.file))
        #    self.numRows=self.numRows+1


    def Today(self):
        varDate = datetime.datetime.now()
        self.datetoday = str(varDate.day) + "." + str(varDate.month) + "." + str(varDate.year)
        self.DBconnection()  # Check Exception need
        userListQuery = "SELECT fileName,date FROM videoDatabase where date=\"" + self.datetoday+ "\""
        self.db_Cursor.execute(userListQuery)
        results = self.db_Cursor.fetchall()
        self.ui.tableWidget_Recording.clearContents()

        self.ui.tableWidget_Recording.setRowCount(0);
        numRows = 0

        if not results:
            msg = QtWidgets.QMessageBox()
            msg.about(self, "Error", "Data Not Found")

        for row in results:
            fileName = row[0]
            date_info = row[1]
            filepath = self.outDir + "/" + fileName
            filesize = os.path.getsize(filepath) / (1024 * 1024)
            filesize = '{:.0f}'.format(filesize)
            filesize = filesize + "Mb"
            self.ui.tableWidget_Recording.insertRow(numRows)
            self.ui.tableWidget_Recording.setItem(numRows, 0, QtWidgets.QTableWidgetItem(fileName))
            self.ui.tableWidget_Recording.setItem(numRows, 1, QtWidgets.QTableWidgetItem(date_info))
            self.ui.tableWidget_Recording.setItem(numRows, 2, QtWidgets.QTableWidgetItem(filesize))
            numRows = numRows + 1

    def DisplayDateList(self):
        self.ui.comboBox.clear()
        self.DBconnection()  # Check Exception need
        userListQuery = "SELECT DISTINCT(date) FROM videoDatabase"
        self.db_Cursor.execute(userListQuery)
        results = self.db_Cursor.fetchall()
        if not results:
            msg = QtWidgets.QMessageBox()
            msg.about(self, "Error", "Data Not Found")

        for row in results:
            date_info = row[0]
            self.ui.comboBox.addItem(date_info)
        self.DBDisconnect()



    def DBDisconnect(self):
        # disconnect from server
        self.db_Object.close()




    def updateTable(self):

        self.ui.tableWidget_Recording.clearContents()
        self.numRows = 0
        self.dirList = os.listdir(self.outDir)
        for self.file in self.dirList:
            filepath=self.outDir + "/" + self.file
            self.ui.tableWidget_Recording.insertRow(self.numRows)
            self.ui.tableWidget_Recording.setItem(self.numRows, 0, QtWidgets.QTableWidgetItem(self.file))
            self.ui.tableWidget_Recording.setItem(self.numRows, 1, QtWidgets.QTableWidgetItem(time.ctime(os.path.getctime(filepath))))
            filesize=os.path.getsize(filepath)/(1024*1024)
            filesize= '{:.0f}'.format(filesize)
            filesize=filesize+"Mb"
            self.ui.tableWidget_Recording.setItem(self.numRows, 2,  QtWidgets.QTableWidgetItem(filesize))
            #self.ui.tableWidget_Recording.setItem(self.numRows, 0, QtWidgets.QTableWidgetItem(self.getLength(filepath)) )
            self.numRows = self.numRows + 1


    def getOutputDir(self):
        output_dir = QFileDialog.getExistingDirectory(self,"Open a folder",".",QFileDialog.ShowDirsOnly|QFileDialog.DontResolveSymlinks)
        return output_dir

    def getOutFileName(self):
        varDate = datetime.datetime.now()
        newFileName=str(varDate.day)+"."+str(varDate.month)+"."+str(varDate.year)+"."+\
                    str(varDate.hour)+"."+str(varDate.minute)+"."+str(varDate.second)+".avi"
        return newFileName



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_classobject =UserMain()  #creating the object of above class
    ui_classobject.showMaximized()   #displaying the window
    sys.exit(app.exec_())
