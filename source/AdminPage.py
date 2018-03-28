import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.UiAdminPage import Ui_MainWindow
import MySQLdb
import string
from random import choice
import ntpath
import  datetime
from shutil import copyfile
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.BtConnect()



    def BtConnect(self):
        self.ui.pushButton_adduser.clicked.connect(self.AddUser)
        self.ui.pushButton_deleteuser.clicked.connect(self.DeleteUser)
        self.ui.pushButton_updateuser.clicked.connect(self.UpdateUser)
        self.ui.pushButton_searchuser.clicked.connect(self.SearchUser)
        self.ui.pushButton_clear.clicked.connect(self.ClearData)
        #self.ui.pushButton_changepic.clicked.connect(self.ChangePic)

    def ClearData(self):
        self.ui.lineEdit_userid.clear()
        self.ui.lineEdit_firstname.clear()
        self.ui.lineEdit_lastname.clear()
        self.ui.lineEdit_username.clear()
        self.ui.lineEdit_emailid.clear()
        self.ui.lineEdit_mobileno.clear()
        imagepath="D:\\Project\\HawkEye\\resource\\images\\playerbackground.png"
        self.ui.label_propic_img.setPixmap(QtGui.QPixmap(imagepath))
        self.EditEnableTrue()



    def getFileName(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                    'c:\\',"Image files (*.jpg *.gif)")
        print(path)
        src=path
        #in_filename = ntpath.basename(path)
        op_filename =self.getOutFileName()
        print(op_filename)
        dest = "D:\\Project\\HawkEye\\database\\userpic\\" + op_filename
        copyfile(src,dest)
        print(op_filename)
        return op_filename

    def getOutFileName(self):
        varDate = datetime.datetime.now()
        newFileName=str(varDate.day)+"."+str(varDate.month)+"."+str(varDate.year)+"."+\
                    str(varDate.hour)+"."+str(varDate.minute)+"."+str(varDate.second)+".jpg"
        return newFileName

    def GenPasswd(self):
        chars = string.ascii_letters + string.digits
        newpasswd = ""
        for i in range(8):
            newpasswd = newpasswd + choice(chars)
        return newpasswd

    def AddUser(self):
        self.DBconnection()  # Check Exception need

        user_name = self.ui.lineEdit_username.text()
        first_name = self.ui.lineEdit_firstname.text()
        last_name = self.ui.lineEdit_lastname.text()
        email_id = self.ui.lineEdit_emailid.text()
        mobile_no = int(self.ui.lineEdit_mobileno.text())
        filename ="pic.jpg" #self.getFileName()
        #print(filename)
        user_password =self.GenPasswd()
        #print(user_password)


        addUserQuery = "insert into user (first_name,last_name,user_name,user_password,email_id,mobile_no,profile_pic) " \
                       " values ('%s', '%s', '%s', '%s', '%s',%d,'%s' )" % (first_name,last_name,user_name,user_password,email_id,mobile_no,filename)
        print(addUserQuery)

        try:
            # Execute the SQL command
            self.db_Cursor.execute(addUserQuery)
            # Commit your changes in the database
            self.db_Object.commit()
        except:
            # Rollback in case there is any error
            self.db_Object.rollback()

        self.DBDisconnect()


    def DeleteUser(self):
        pass

    def UpdateUser(self):
        pass

    def SearchUser(self):

        self.DBconnection()  # Check Exception need

        user_name = self.ui.lineEdit_username.text()

        searchUserQuery = "select user_id,first_name,last_name,user_name,email_id,mobile_no,profile_pic from user where user_name=\""+user_name+"\""
        print(searchUserQuery)

        self.db_Cursor.execute(searchUserQuery)
        results = self.db_Cursor.fetchall()


        if not results:
            msg =QtWidgets.QMessageBox()
            msg.about(self, "Error","User Not Found")

        for row in results:

            self.ui.lineEdit_userid.setText(str(row[0]))    #user_id in string to interger
            self.ui.lineEdit_firstname.setText(row[1])
            self.ui.lineEdit_lastname.setText(row[2])
            self.ui.lineEdit_username.setText(row[3])
            self.ui.lineEdit_emailid.setText(row[4])
            self.ui.lineEdit_mobileno.setText(str(row[5]))
            imagepath ="D:\\Project\\HawkEye\\database\\userpic\\"+row[6]
            self.ui.label_propic_img.setPixmap(QtGui.QPixmap(imagepath))
            self.EditEnableFalse()

        self.DBDisconnect()


    def EditEnableFalse(self):
        self.ui.lineEdit_userid.setReadOnly(True)
        self.ui.lineEdit_firstname.setReadOnly(True)
        self.ui.lineEdit_lastname.setReadOnly(True)
        self.ui.lineEdit_username.setReadOnly(True)
        self.ui.lineEdit_emailid.setReadOnly(True)
        self.ui.lineEdit_mobileno.setReadOnly(True)

    def EditEnableTrue(self):
        self.ui.lineEdit_userid.setReadOnly(False)
        self.ui.lineEdit_firstname.setReadOnly(False)
        self.ui.lineEdit_lastname.setReadOnly(False)
        self.ui.lineEdit_username.setReadOnly(False)
        self.ui.lineEdit_emailid.setReadOnly(False)
        self.ui.lineEdit_mobileno.setReadOnly(False)

    def ChangePic(self):
        pass


    def DBconnection(self):
        # Open database connection
        self.db_Object = MySQLdb.connect("localhost", "root", "root", "hawkeye") #database ip,username,password,database name
        # prepare a cursor object using cursor() method
        self.db_Cursor = self.db_Object.cursor()





    def DBDisconnect(self):
        # disconnect from server
        self.db_Object.close()



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_classobject =Main()  #creating the object of above class
    ui_classobject.show()   #displaying the window
    sys.exit(app.exec_())