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
import socket
from pynmea import nmea
import json
from source.ThreadSound import ThreadingExample
from firebase import firebase

class UserMain(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui =Ui_UserWindow()
        self.ui.setupUi(self)
        self.out=None
        self.Vheight=640
        self.Vwidth=480
        self.flag=-1 #Flag for 1 -recording  -1 for no recodring and 0 for stop recording
        self.sliderFlag=-1
        #self.engine = pyttsx3.init()
        self.DisplayDateList()
        self.resultList=[]

        self.frameCount=1
        #self.capture=None
        # elf.ui.webView.load(QtCore.QUrl("D:/Project/HawkEye/html/map.html"))
        self.fourcc=None
        self.pauseFlag=0
        self.defaultOpFolder="D:\\Project\\HawkEye\\video"
        self.outDir="D:\\Project\\HawkEye\\video"
        self.currentLatitude=""
        self.currentLongitude=""
        self.gpsData =""
        self.locationFlag=False
        self.defaultGpsIp='127.0.0.1'
        self.defaultGpsPort='14551'
        self.VideoFlag=False
        self.StreamFlag=False
        self.ui.lineEdit_gpsIp.setText(self.defaultGpsIp)
        self.ui.lineEdit_3.setText(self.defaultGpsPort)
        self.ui.label_AlgoInit.setText("Check: NO")
        self.ui.label_gpsStatus.setText("Not Connected")
        self.gpsFlag=False
        self.algoFlag=False
        self.ui.label_outputDir.setText(self.defaultOpFolder)
        self.ui.label_opdirtext.setText(self.defaultOpFolder)
        #self.ui.label_player.setPixmap(QPixmap("D:\\Project\\HawkEye\\resource\\images\\playerbackground.png"))
        self.setEnabledButtonOnCreate()
        #self.updateTable()
        self.timer = QTimer()
        self.ButtonConnectOnCreate()
        self.ButtonDConnectOnCreate()
        self.ServerConnect()


    def ServerConnect(self):
        self.firebase = firebase.FirebaseApplication('https://myapplication-faa59.firebaseio.com', None)
        print("Server Connected")



    def algo_init(self):

        if not(self.algoFlag):
            options = {"model": "D:/Project/HawkEye/resource/darkflow/cfg/tiny-yolo-voc.cfg",
                       "load": "D:/Project/HawkEye/resource/darkflow/bin/tiny-yolo-voc.weights",
                       "threshold": 0.5, "gpu": 0.5}
            self.tfnet = TFNet(options)
            self.colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]
            self.ui.label_AlgoInit.setText("Check: Yes")
            msg = QtWidgets.QMessageBox()
            msg.about(self, "Message", "Algorithm Initialized")
            self.ui.label_AlgoInit.setStyleSheet("background-color: rgb(170, 255, 127);\n"
                                              "font: 10pt \"MS Shell Dlg 2\";")
            self.algoFlag=True
            return True
        else:
            return True

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
        self.ui.horizontalSlider.valueChanged.connect(self.valuechange)
        self.ui.horizontalSlider.sliderPressed.connect(self.SliderPressed)
        self.ui.horizontalSlider.sliderReleased.connect(self.SliderReleased)
        self.ui.horizontalSlider.sliderMoved.connect(self.SliderMoved)
        self.ui.pushButton_pause.clicked.connect(self.pause)
        self.ui.pushButton_ChangeOpDir.clicked.connect(self.ChangeOutputFolder)
        self.ui.pushButton_FileDialog.clicked.connect(self.ChangeOutputFolder)
        self.ui.pushButton_AlgoInit.clicked.connect(self.algo_init)
        self.ui.pushButton_GpsCon.clicked.connect(self.connectGps)
        self.ui.pushButton_logout.clicked.connect(self.OpenLoginPage)
        self.ui.pushButton_SendAlert.clicked.connect(self.SendAlert)








    def setEnabledButtonOnCreate(self):
        self.ui.pushButton_stop.setEnabled(False)
        self.ui.pushButton_startRec.setEnabled(False)
        self.ui.pushButton_stopRec.setEnabled(False)
        self.ui.pushButton_play.setEnabled(False)
        self.ui.pushButton_start.setEnabled(True)
        self.ui.pushButton_vstop.setEnabled(False)
        self.ui.pushButton_pause.setEnabled(False)
       #self.ui.pushButton_next.setEnabled(False)


    def onClickBtnPage1(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def onClickBtnPage2(self):
        self.ui.stackedWidget.setCurrentIndex(1)

#webcam  method
    def ChangeOutputFolder(self):
        self.outDir=self.getOutputDir()
        if self.outDir :
            self.ui.label_outputDir.setText(self.outDir)
            self.ui.label_opdirtext.setText(self.outDir)
            msg = QtWidgets.QMessageBox()
            msg.about(self, "Message", "Output folder changed")
        else:
            self.ui.label_outputDir.setText(self.defaultOpFolder)
            self.ui.label_opdirtext.setText(self.defaultOpFolder)
            self.outDir=self.defaultOpFolder

    def SendAlert(self):
        if(self.locationFlag):
            self.firebase.put('/LocationUpdate', "latitude", self.currentLatitude)
            self.firebase.put('/LocationUpdate', "longitude", self.currentLongitude)
            self.ui.label_5.setText("Location Sent:" + self.currentLatitude+ "," + self.currentLongitude)
            msg = QtWidgets.QMessageBox()
            msg.about(self, "Message", "Current Location Sent")

        else:
            msg = QtWidgets.QMessageBox()
            msg.about(self, "Message", "Currrent Location Not Available")

    def start(self):
        self.flag=-1
        self.StreamFlag=True
        if not(self.connectGps()):
            self.ui.label_msg.setText("Streaming Stopped")
            return
        if not(self.algo_init()):
            self.ui.label_msg.setText("Streaming Stopped")
            return

        self.ui.pushButton_startRec.setEnabled(True)
        self.ui.pushButton_stop.setEnabled(True)

        self.captureCamera = cv2.VideoCapture(0) #0 for internal webcam 1 for external camera
        if not  self.captureCamera.isOpened():
            msg = QtWidgets.QMessageBox()
            msg.about(self, "Error", "Video Device Not Connected")
            self.capture.release()
            cv2.destroyAllWindows()
            self.ui.pushButton_startRec.setEnabled(False)
            self.ui.pushButton_stopRec.setEnabled(False)
            self.ui.pushButton_stop.setEnabled(False)
            self.ui.label_player.setPixmap(QPixmap("D:\\Project\\HawkEye\\resource\\images\\playerbackground.png"))
            self.ui.label_msg.setText("Streaming Stopped")
            return
        else:
            self.captureCamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.captureCamera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.timer =QTimer()
            self.timer.timeout.connect(self.refresh_frame)
            self.timer.start(1)
            self.ui.label_msg.setText("Streaming...")

    def stop(self):
        self.timer.stop()
        self.captureCamera.release()
        cv2.destroyAllWindows()
        self.gpsFlag=False
        self.StreamFlag=False
        self.disonnectGps()
        if(self.flag==1):
            self.jsonDataWrite()
        self.ui.pushButton_startRec.setEnabled(False)
        self.ui.pushButton_stopRec.setEnabled(False)
        self.ui.pushButton_stop.setEnabled(False)
        self.ui.label_player.setPixmap(QPixmap("D:\\Project\\HawkEye\\resource\\images\\playerbackground.png"))
        self.ui.label_msg.setText("Streaming Stopped")


    def startRecord(self):

        self.flag=1 # flag to start and stop recording
        # Initilizing for recording
        self.resultList=[] #To append the output result
        self.frameCount=1
        varDate = datetime.datetime.now()
        datetoday = str(varDate.day) + "." + str(varDate.month) + "." + str(varDate.year)
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec
        self.fileName=self.getOutFileName()  #FileName without extension for creating videofile and json file
        vfileName=self.fileName+".avi"
        OutFilePath = os.path.join(self.outDir,vfileName)
        self.out = cv2.VideoWriter(OutFilePath, self.fourcc, 5.0, (int(self.Vheight), int(self.Vwidth)))
        self.DBconnection()
        userListQuery = "INSERT INTO videoDatabase VALUES (\""+vfileName+"\",\""+datetoday+"\")"
        self.db_Cursor.execute(userListQuery)
        self.db_Object.commit()
        self.DBDisconnect()
        self.DisplayDateList()

        self.ui.pushButton_startRec.setEnabled(False)
        self.ui.pushButton_stopRec.setEnabled(True)
        self.ui.label_msg.setText("Recording Started")



    def stopRecord(self):
        self.flag=0
        self.jsonDataWrite()
        #self.out.release()#Recording streaming closed
        print("Video File Saved")
        self.ui.pushButton_stopRec.setEnabled(False)
        self.ui.pushButton_startRec.setEnabled(True)
        self.ui.label_msg.setText("Recording Stopped")


    def jsonDataWrite(self):
        # Write recording result to file
        jsonFileName = self.fileName + ".json"
        OutFilePath = os.path.join(self.outDir, jsonFileName)
        with open(OutFilePath, 'w') as outputFile:
            outputFile.write(json.dumps(self.resultList, indent=2))
            outputFile.close()
        print("Data Written to json ")

    def refresh_frame(self):
        outputtext="" #To store display result string
        self.gpgga = nmea.GPGGA()
        latitude = "-1000" #invalid data
        lat_dir = ""
        longitude = "-1000" #invalid data
        long_dir = ""
        ddlongitude=""
        ddlatitude=""
        sddlatitude=""
        sddlongitude=""
        countLabel = 1  # To Count number of Object Detected
        mdataResult = {}  # To store multi detected object information i.e multiple dataresult
        dataResult = {}  # To store label and confidence
        finalData = {}  #To Store gps and mdataresult
        newFinalData = {}# To store final data and framenos
        ret, self.image = self.captureCamera.read()
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
                 # resultList Generation Code
                if(self.flag==1):
                    dataResult = {}
                    dataResult["label"]=label
                    dataResult["confidence"]='{:.0f}'.format(confidence*100)
                    mdataResult[countLabel]=dataResult
                    countLabel+=1
            self.image = frame # To write processed frame to original frame
            #To get GPS Data From Telemetry Stream
#            if (gpsdata[0:6] == '$GPGGA'):
            self.getGpsData()
            self.gpgga.parse(self.gpsdata)
            latitude = self.gpgga.latitude
            lat_dir = self.gpgga.lat_direction
            longitude = self.gpgga.longitude
            long_dir = self.gpgga.lon_direction
        # else :
            #     gpsdata = self.mySocket.recv(1024).decode()
            #     self.gpgga.parse(gpsdata)
            #     latitude = self.gpgga.latitude
            #     lat_dir = self.gpgga.lat_direction
            #     longitude = self.gpgga.longitude
            #     long_dir = self.gpgga.lon_direction



            ##Converting Latitude Longitude data to correct values
            ddlatitude = float(latitude[0:2]) + ((float(latitude[2:])) / 60.0)
            if (lat_dir == 'S' or lat_dir == 'W'):
                 ddlatitude = -ddlatitude

            ddlongitude = float(longitude[0:3]) + ((float(longitude[3:])) / 60.0)
            if (long_dir == 'S' or long_dir == 'W'):
                 ddlongitude = -ddlongitude

            sddlatitude =str(ddlatitude)
            sddlongitude=str(ddlongitude)
             #Write gps data to resultList
            if(self.flag==1):
                finalData["latitude"] = sddlatitude
                finalData["longitude"] = sddlongitude
                finalData["detection"] = mdataResult
                newFinalData[self.frameCount] = finalData
                if(mdataResult):
                    self.resultList.append(newFinalData) #Appending Result to List

            self.currentLatitude=sddlatitude
            self.currentLongitude=sddlongitude
            self.locationFlag=True
            self.displayPrediction(self.frameCount, sddlatitude, sddlongitude, outputtext)  # To Display Result
            self.frameCount += 1
        else :
            self.stop()
        ###### Image Processing Ends
        if self.flag==1 :
            self.out.write(self.image)
        elif self.flag==0 :
                self.out.release()
        self.displayImage(self.image)

    def getGpsData(self):
        self.gpsdata = self.mySocket.recv(1024).decode()  # Getting gps data
        if not (self.gpsdata[0:6] == '$GPGGA'):
            self.getGpsData()
        else :
            return


    def displayPrediction(self,frameCount,lats,longitude,outputtext):
        #self.ui.listWidgetResults.clear()
        gpsdata = str(lats) + "," + str(longitude)
        outData = "Frame no." + str(frameCount) + "\n Gps:" + gpsdata + "\n" + outputtext
        self.ui.listWidgetResults.addItem(outData)
        return


    def AlertMessage(self):
        self.engine.say("Human Detected")
        self.engine.runAndWait()
#       playsound("D:\\Project\\HawkEye\\resource\\sound\\HumanDetected.mp3")

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

    def connectGps(self):
        if not (self.gpsFlag):
            self.host =self.ui.lineEdit_gpsIp.text() #127.0.0.1
            self.port = self.ui.lineEdit_3.text() #14551
            self.mySocket = socket.socket()
            try:
                self.mySocket.connect((self.host, int(self.port)))
                self.ui.label_gpsStatus.setText("Connected")
                msg = QtWidgets.QMessageBox()
                msg.about(self, "Success", "Gps Connected")
                self.ui.label_gpsStatus.setStyleSheet("background-color: rgb(170, 255, 127);\n"
                                                   "font: 10pt \"MS Shell Dlg 2\";")
                self.gpsFlag=True
                return True
            except:
                msg = QtWidgets.QMessageBox()
                msg.about(self, "Error", "Gps Not Connected")
                self.gpsFlag=False
                return False
        else:
            return True

    def disonnectGps(self):
        self.mySocket.close()
        print("Gps Disconnected")





################################PAGE 2 ######################################

    def DBconnection(self):
        # Open database connection
        self.db_Object = MySQLdb.connect("localhost", "root", "root", "hawkeye") #database ip,username,password,database name
        # prepare a cursor object using cursor() method
        self.db_Cursor = self.db_Object.cursor()

    def play(self, filename):

        # if(self.pauseFlag==0):
        self.pauseFlag=1
        self.flag = -1
        self.VideoFlag=True
        self.capture = cv2.VideoCapture(filename)
        frameCount=self.capture.get(cv2.CAP_PROP_FRAME_COUNT)
        self.sliderValue=1
        self.sliderFlag=0
        self.Trackbar(frameCount)

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.timer.timeout.connect(self.refresh_frame2)
        self.timer.start(100)  #time as argument
    # if(self.pauseFlag==1):
        #     self.timer.timeout.connect(self.refresh_frame2)
        #     self.timer.start(100)
        #     #To Start Playing a paused video

    def pause(self):
        self.pauseFlag = 1
        self.timer.stop()
        #self.ButtonConnectOnCreate()




    def Timer(self,time):

        self.timer.timeout.connect(self.refresh_frame2)
        self.timer.start(time)

    def vstop(self):

        if (self.capture.isOpened()):
            self.timer.stop()
            self.VideoFlag=False
            self.capture.release()
            cv2.destroyAllWindows()
            self.setEnabledButtonOnCreate()
            self.ui.label_player_2.setPixmap(QPixmap("D:\\Project\\HawkEye\\resource\\images\\playerbackground.png"))

    def refresh_frame2(self):
        ret, self.image = self.capture.read()
        if(self.sliderFlag==0):
            self.ui.horizontalSlider.setValue(self.sliderValue)
            self.ui.label_frameno.setText(str(self.sliderValue))

        if ret:
        # IMAGE PROCESSING CODE GOES HERE
            self.displayImage2(self.image)
        else:
            self.vstop()

        self.sliderValue+=1

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

    def Trackbar(self,maxFrame):
        self.ui.horizontalSlider.setMinimum(1)
        self.ui.horizontalSlider.setMaximum(maxFrame)
        self.ui.horizontalSlider.setValue(1)
        self.ui.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.ui.horizontalSlider.setTickInterval(1)

    def valuechange(self):
        if(self.capture.isOpened()):
            frameNo = self.ui.horizontalSlider.value()

            self.capture.set(cv2.CAP_PROP_POS_FRAMES, frameNo)


    def SliderReleased(self):
        self.sliderFlag=0

    def SliderPressed(self):
        self.sliderFlag=1

    def SliderMoved(self):
        self.sliderFlag=1

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
            #print(self.currentFile)
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
            if(os.path.exists(filepath)):
                filesize = os.path.getsize(filepath) / (1024 * 1024)
                filesize = '{:.0f}'.format(filesize)
                filesize = filesize + "Mb"
                videoCap = cv2.VideoCapture(filepath)
                self.ui.tableWidget_Recording.insertRow(numRows)
                self.ui.tableWidget_Recording.setItem(numRows,0, QtWidgets.QTableWidgetItem(fileName))
                self.ui.tableWidget_Recording.setItem(numRows, 1, QtWidgets.QTableWidgetItem(date_info))
                self.ui.tableWidget_Recording.setItem(numRows, 2, QtWidgets.QTableWidgetItem(filesize))
                self.ui.tableWidget_Recording.setItem(numRows, 3, QtWidgets.QTableWidgetItem(str(videoCap.get(cv2.CAP_PROP_FRAME_COUNT))))
                numRows=numRows+1
                videoCap.release()
            else :
                msg = QtWidgets.QMessageBox()
                msg.about(self, "Error", "File not found")

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
            videoCap = cv2.VideoCapture(filepath)
            self.ui.tableWidget_Recording.insertRow(numRows)
            self.ui.tableWidget_Recording.setItem(numRows, 0, QtWidgets.QTableWidgetItem(fileName))
            self.ui.tableWidget_Recording.setItem(numRows, 1, QtWidgets.QTableWidgetItem(date_info))
            self.ui.tableWidget_Recording.setItem(numRows, 2, QtWidgets.QTableWidgetItem(filesize))
            self.ui.tableWidget_Recording.setItem(numRows, 3, QtWidgets.QTableWidgetItem(str(videoCap.get(cv2.CAP_PROP_FRAME_COUNT))))
            numRows = numRows + 1
            videoCap.release()

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
                    str(varDate.hour)+"."+str(varDate.minute)+"."+str(varDate.second)
        return newFileName

    def OpenLoginPage(self):
        if(self.VideoFlag):
            self.vstop()
        if(self.StreamFlag):
            self.stop()
        from source.LoginPage import LoginMain
        self.close()
        self.objectUserMain = LoginMain()
        self.objectUserMain.show()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_classobject =UserMain()  #creating the object of above class
    ui_classobject.showMaximized()   #displaying the window
    sys.exit(app.exec_())
