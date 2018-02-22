import  time
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


from ui.UiOfficerPage import Ui_MainWindow
import cv2
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.out=None
        self.Vheight=640
        self.Vwidth=480
        self.fourcc=None
        self.FILE_OUTPUT ='test.avi'
        self.ui.pushButton_page1.clicked.connect(self.onClickBtnPage1)
        self.ui.pushButton_page2.clicked.connect(self.onClickBtnPage2)


        #Stacked Page_1 Button
        self.ui.label_player.setPixmap(QPixmap("D:\\Project\\HawkEye\\resource\\images\\playerbackground.png"))
        self.ui.pushButton_start.clicked.connect(self.start)
        self.ui.pushButton_stop.clicked.connect(self.stop)
        self.ui.pushButton_startRec.setEnabled(False)
        self.ui.pushButton_stopRec.setEnabled(False)
        self.ui.pushButton_startRec.clicked.connect(self.startRecord)
        self.ui.pushButton_stopRec.clicked.connect(self.stopRecord)

        self.ui.tableWidget_Recording.setItem(0, 0, QtWidgets.QTableWidgetItem("test.avi"))
        self.ui.tableWidget_Recording.doubleClicked.connect(self.on_DClickTable)


    def onClickBtnPage1(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def onClickBtnPage2(self):
        self.ui.stackedWidget.setCurrentIndex(1)

#video player method
    def start(self):
        self.flag=-1
        self.ui.pushButton_startRec.setEnabled(True)
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        #Initilizing for recording
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID') #Codec
        self.out = cv2.VideoWriter(self.FILE_OUTPUT,self.fourcc, 20.0, (int(self.Vheight),int(self.Vwidth)))
        #####

        self.timer =QTimer()
        self.timer.timeout.connect(self.refresh_frame)
        self.timer.start(5)

    def play(self, filename):
        self.flag = -1

        self.capture = cv2.VideoCapture(filename)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh_frame)
        self.timer.start(50)

    def stop(self):
        self.timer.stop()
        self.capture.release()
        self.out.release()
        self.ui.pushButton_startRec.setEnabled(False)
        self.ui.pushButton_stopRec.setEnabled(False)
        self.ui.label_player.setPixmap(QPixmap("D:\\Project\\HawkEye\\resource\\images\\playerbackground.png"))

    def startRecord(self):
        self.flag=1
        self.ui.pushButton_startRec.setEnabled(False)
        self.ui.pushButton_stopRec.setEnabled(True)



    def stopRecord(self):
        self.flag=0
        self.ui.pushButton_stopRec.setEnabled(False)
        self.ui.pushButton_startRec.setEnabled(True)




    def refresh_frame(self):
        ret, self.image = self.capture.read()
        # IMAGE PROCESSING CODE GOES HERE
        self.image = cv2.flip(self.image, 1)
        if self.flag==1 :
            self.out.write(self.image)
        elif self.flag==0 :
            self.out.release()
        self.displayImage(self.image)

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

##################
    def on_DClickTable(self):
        self.play('test1.avi')





if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_classobject =Main()  #creating the object of above class
    ui_classobject.show()   #displaying the window
    sys.exit(app.exec_())