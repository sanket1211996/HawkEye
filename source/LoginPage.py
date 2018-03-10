import sys
from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
from ui.UiLoginPage import Ui_MainWindow
import MySQLdb
from source.UserPage import UserMain
class LoginMain(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

        #Class Variable
        self.db_Object=None
        self.db_Cursor=None
        self.username =None
        self.password=None
        self.Admin_Login = "Admin_Login"
        self.User_Login = "User_Login"

        #Initliazaton method:
        self.ComboBoxInit()
        self.ButtonConnect()

        # Connecting the button to action
    def ButtonConnect(self):
        self.ui.pushButton_Login.clicked.connect(self.authOfficer)

        # The function is called when the button clicked
    def onClickLoginIn(self):
        UserValidate=self.ui.comboBox_UserType.currentText()
        if (UserValidate==self.Admin_Login):
            self.authAdmin()
        elif (UserValidate==self.User_Login):
            self.authOfficer()

    def ComboBoxInit(self):
        self.ui.comboBox_UserType.addItem(self.Admin_Login)
        self.ui.comboBox_UserType.addItem(self.User_Login)


    def DBconnection(self):
        # Open database connection
        self.db_Object = MySQLdb.connect("localhost", "root", "root", "hawkeye") #database ip,username,password,database name
        # prepare a cursor object using cursor() method
        self.db_Cursor = self.db_Object.cursor()

    def authAdmin(self):
        pass



    def DBDisconnect(self):
        # disconnect from server
        self.db_Object.close()

    def authOfficer(self):
        self.DBconnection()   #Check Exception need

        self.username = self.ui.lineEdit_UserName.text()
        self.password = self.ui.lineEdit_Password.text()


        userListQuery ="SELECT username,user_password FROM user"

        self.db_Cursor.execute(userListQuery)
        results = self.db_Cursor.fetchall()

        for row in results:
            username_fetched=row[0]
            password_fetched=row[1]
            print (username_fetched)
            print (password_fetched)
            if(username_fetched==self.username and password_fetched==self.password):
                self.DBDisconnect()
                self.OpenUserPage()




        #Opening another window code
    def OpenUserPage(self):
        self.close()
        self.objectUserMain =UserMain()
        self.objectUserMain.showMaximized()










if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    objectLoginMain =LoginMain()  #creating the object of above class we can name it to any file
    objectLoginMain.show()   #displaying the window
    sys.exit(app.exec_())