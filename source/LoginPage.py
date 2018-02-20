import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.UiLoginPage import Ui_MainWindow


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_Login.clicked.connect(self.onClick)  #Connecting the button to action.

    def onClick(self):  #The function is called when the button clicked
        self.ui.lineEdit_UserName.setText("Sanket_Darwante")


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_classobject =Main()  #creating the object of above class we can name it to any file
    ui_classobject.show()   #displaying the window
    sys.exit(app.exec_())