import sys
from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
from ui.UiLoginPage import Ui_MainWindow


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox_UserType.addItem("Admin_Login")
        self.ui.comboBox_UserType.addItem("Officer_Login")
        self.ui.pushButton_Login.clicked.connect(self.onClickLoginIn)  #Connecting the button to action.

    def onClickLoginIn(self):  #The function is called when the button clicked
        username=self.ui.lineEdit_UserName.text()
        password=self.ui.lineEdit_UserName.text()
        Admin_Login = "Admin_Login"
        Officer_Login = "Officer_Login"
        text=self.ui.comboBox_UserType.currentText()
        if (text==Admin_Login):
            self.authAdmin()
        elif (text==Officer_Login):
            self.authOfficer()

    def authAdmin(self):
        pass

    def authOfficer(self):
        pass









if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_classobject =Main()  #creating the object of above class we can name it to any file
    ui_classobject.show()   #displaying the window
    sys.exit(app.exec_())