
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
        self.SearchByEmail = "Email_Id"
        self.SearchByUserName = "UserName"
        self.databaseProfilePic="D:\\Project\\HawkEye\\database\\userpic"
        self.SearchFlag=False
        self.Editflag=True
        self.CurrentUserId=""
        self.CurrentProfilePic=""
        self.ui.comboBox.addItem("Admin")
        self.ui.comboBox.addItem("User")
        self.BtConnect()
        self.ComboBoxInit()


    def BtConnect(self):
        self.ui.pushButton_adduser.clicked.connect(self.AddUser)
        self.ui.pushButton_deleteuser.clicked.connect(self.DeleteUser)
        self.ui.pushButton_updateuser.clicked.connect(self.UpdateUser)
        self.ui.pushButton_searchuser.clicked.connect(self.SearchUser)
        self.ui.pushButton_clear.clicked.connect(self.ClearData)
        self.ui.pushButton_ResetPassword.clicked.connect(self.ResetPassword)
        self.ui.pushButton_changePic.clicked.connect(self.ChangePic)
        self.ui.pushButton_Edit.clicked.connect(self.EditUser)
        self.ui.pushButton_Logout.clicked.connect(self.OpenLoginPage)


    def ComboBoxInit(self):
        self.ui.comboBox_SearchBy.addItem(self.SearchByUserName)
        self.ui.comboBox_SearchBy.addItem(self.SearchByEmail)

    def ResetPassword(self):
        pass


    def ClearData(self):
        self.CurrentUserId=""
        self.ui.lineEdit_UserIdText.clear()
        self.ui.lineEdit_firstname.clear()
        self.ui.lineEdit_lastname.clear()
        self.ui.lineEdit_username.clear()
        self.ui.lineEdit_emailid.clear()
        self.ui.lineEdit_mobileno.clear()
        self.ui.lineEdit_SearchText.clear()
        imagepath="D:\\Project\\HawkEye\\resource\\images\\profilePicture.png"
        self.ui.label_propic_img.setPixmap(QtGui.QPixmap(imagepath))
        self.SearchFlag=False
        self.Editflag=False

        self.EditEnableTrue()



    # def getFileName(self):
    #     path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
    #                 'c:\\',"Image files (*.jpg *.gif)")
    #     print(path)
    #     src=path
    #     #in_filename = ntpath.basename(path)
    #     op_filename =self.getOutFileName()
    #     print(op_filename)
    #     dest = "D:\\Project\\HawkEye\\database\\userpic\\" + op_filename
    #     copyfile(src,dest)
    #     print(op_filename)
    #     return op_filename

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


        picPath=self.getPicturePath() #self.getFileName()
        #print("Profile Pic:"+picPath)
        user_password =self.GenPasswd()
        #print("Password:"+user_password)


        addUserQuery = "insert into user (first_name,last_name,user_name,user_password,email_id,mobile_no,profile_pic) " \
                       " values ('%s', '%s', '%s', '%s', '%s',%d,'%s' )" % (first_name,last_name,user_name,user_password,email_id,mobile_no,picPath)
        print(addUserQuery)

        try:
            # Execute the SQL command
            self.db_Cursor.execute(addUserQuery)
            # Commit your changes in the database
            self.db_Object.commit()
            msg = QtWidgets.QMessageBox()
            msg.about(self, "Success", "User Added SuccessFully")
            self.ClearData()

        except:
            # Rollback in case there is any error
            self.db_Object.rollback()
            msg = QtWidgets.QMessageBox()
            msg.about(self, "Error", "User Registration Failed")
            self.ClearData()

        self.DBDisconnect()



    def DeleteUser(self):

        if(self.SearchFlag):

            self.DBconnection()  # Check Exception need
            DeleteUserQuery = "delete from  user where user_id="+str(self.CurrentUserId)
            print(DeleteUserQuery)

            try:
                # Execute the SQL command
                self.db_Cursor.execute(DeleteUserQuery)
                # Commit your changes in the database
                self.db_Object.commit()
                msg = QtWidgets.QMessageBox()
                msg.about(self, "Success", "User Deleted Successfully")
                self.ClearData()

            except:
                # Rollback in case there is any error
                self.db_Object.rollback()

            self.DBDisconnect()
        else:
            msg = QtWidgets.QMessageBox()
            msg.about(self, "Message", "Please Search User.... ")

    def UpdateUser(self):

        if(self.SearchFlag and self.Editflag):
            self.DBconnection()  # Check Exception need
            user_name = self.ui.lineEdit_username.text()
            first_name = self.ui.lineEdit_firstname.text()
            last_name = self.ui.lineEdit_lastname.text()
            email_id = self.ui.lineEdit_emailid.text()
            mobile_no = int(self.ui.lineEdit_mobileno.text())
            picPath=self.CurrentProfilePic

            UpdateUserQuery ="UPDATE user  SET first_name ='%s',last_name='%s',user_name='%s',email_id='%s',mobile_no='%d',profile_pic='%s' " \
                             "WHERE user_id='%d' "%(first_name,last_name,user_name,email_id,mobile_no,picPath,self.CurrentUserId)


            print(UpdateUserQuery)

            try:
                # Execute the SQL command
                self.db_Cursor.execute(UpdateUserQuery)
                # Commit your changes in the database
                self.db_Object.commit()
                msg = QtWidgets.QMessageBox()
                msg.about(self, "Success", "User Updated SuccessFully")
                self.ClearData()

            except:
                # Rollback in case there is any error
                self.db_Object.rollback()
                msg = QtWidgets.QMessageBox()
                msg.about(self, "Error", "User Update  Failed")
                self.ClearData()
            self.DBDisconnect()

        if not (self.SearchFlag):
            msg = QtWidgets.QMessageBox()
            msg.about(self, "Message", "Please Search User ....")

        if(self.Editflag):
            msg = QtWidgets.QMessageBox()
            msg.about(self, "Warning", "Already Updated")






    def SearchUser(self):

        UserValidate = self.ui.comboBox_SearchBy.currentText()
        print(UserValidate)
        if (UserValidate == self.SearchByEmail):
            self.SearchEmail()
        elif (UserValidate == self.SearchByUserName):
            self.SearchUserName()

    def SearchUserName(self):
        self.DBconnection()  # Check Exception need

        user_name = self.ui.lineEdit_SearchText.text()

        searchUserQuery = "select user_id,first_name,last_name,user_name,email_id,mobile_no,profile_pic from user where user_name=\""+user_name+"\""
        print(searchUserQuery)

        self.db_Cursor.execute(searchUserQuery)
        results = self.db_Cursor.fetchall()


        if not results:
            msg =QtWidgets.QMessageBox()
            msg.about(self, "Error","User Not Found")
            self.SearchFlag=False
        else:
            for row in results:
                self.CurrentUserId=row[0]
                #print(self.CurrentUserId)
                self.ui.lineEdit_UserIdText.setText(str(row[0]))    #user_id in string to interger
                self.ui.lineEdit_firstname.setText(row[1])
                self.ui.lineEdit_lastname.setText(row[2])
                self.ui.lineEdit_username.setText(row[3])
                self.ui.lineEdit_emailid.setText(row[4])
                self.ui.lineEdit_mobileno.setText(str(row[5]))
                imagepath =row[6]
                self.CurrentProfilePic=imagepath
                #print(imagepath)
                self.ui.label_propic_img.setPixmap(QtGui.QPixmap(imagepath))
                self.EditEnableFalse()

            self.SearchFlag=True;

        self.DBDisconnect()

    def SearchEmail(self):
        self.DBconnection()  # Check Exception need

        email_id = self.ui.lineEdit_SearchText.text()

        searchUserQuery = "select user_id,first_name,last_name,user_name,email_id,mobile_no,profile_pic from user where email_id=\"" + email_id + "\""
        print(searchUserQuery)

        self.db_Cursor.execute(searchUserQuery)
        results = self.db_Cursor.fetchall()

        if not results:
            msg = QtWidgets.QMessageBox()
            msg.about(self, "Error", "User Not Found")
            self.SearchFlag=False
        else:
            for row in results:
                self.CurrentUserId = row[0]
                self.ui.lineEdit_UserIdText.setText(str(row[0]))  # user_id in string to interger
                self.ui.lineEdit_firstname.setText(row[1])
                self.ui.lineEdit_lastname.setText(row[2])
                self.ui.lineEdit_username.setText(row[3])
                self.ui.lineEdit_emailid.setText(row[4])
                self.ui.lineEdit_mobileno.setText(str(row[5]))
                imagepath = row[6]
                self.ui.label_propic_img.setPixmap(QtGui.QPixmap(imagepath))
                self.EditEnableFalse()
            self.SearchFlag=True

        self.DBDisconnect()


    def EditUser(self):
        self.EditEnableTrue()
        self.Editflag=True


    def EditEnableFalse(self):
        self.ui.lineEdit_UserIdText.setReadOnly(True)
        self.ui.lineEdit_firstname.setReadOnly(True)
        self.ui.lineEdit_lastname.setReadOnly(True)
        self.ui.lineEdit_username.setReadOnly(True)
        self.ui.lineEdit_emailid.setReadOnly(True)
        self.ui.lineEdit_mobileno.setReadOnly(True)

    def EditEnableTrue(self):
        self.ui.lineEdit_firstname.setReadOnly(False)
        self.ui.lineEdit_lastname.setReadOnly(False)
        self.ui.lineEdit_username.setReadOnly(False)
        self.ui.lineEdit_emailid.setReadOnly(False)
        self.ui.lineEdit_mobileno.setReadOnly(False)

    def ChangePic(self):
        picPath=self.getPicturePath()
        self.CurrentProfilePic=picPath

    def getPicturePath(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        picPath,_= QtWidgets.QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                                          "All Files (*);;Python Files (*.py)",
                                                                  options=options)
        if picPath:
            print(picPath)
            self.ui.label_propic_img.setPixmap(QtGui.QPixmap(picPath))
            return picPath

    def DBconnection(self):
        # Open database connection
        self.db_Object = MySQLdb.connect("localhost", "root", "root", "hawkeye") #database ip,username,password,database name
        # prepare a cursor object using cursor() method
        self.db_Cursor = self.db_Object.cursor()





    def DBDisconnect(self):
        # disconnect from server
        self.db_Object.close()


    def OpenLoginPage(self):
        from source.LoginPage import LoginMain
        self.close()
        self.objectUserMain = LoginMain()
        self.objectUserMain.show()



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_classobject =Main()  #creating the object of above class
    ui_classobject.show()   #displaying the window
    sys.exit(app.exec_())