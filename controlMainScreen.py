import datetime
import sys
import os
import urllib.request
import cv2
import numpy as np
import xlrd
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw, QtWidgets, QtCore
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import QUrl, QDir, QTimer, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QStyle
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from surveiliaFrontEnd import Ui_surveiliaFrontEnd
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QPushButton

# import pyrebase
# firebaseConfig={
#     'apiKey': "AIzaSyCie_t3hdNbn6zTLmO0NPgJs2nm-jFxxR8",
#     'authDomain': "surveiliadatabase.firebaseapp.com",
#     'databaseURL': "https://surveiliadatabase.firebaseio.com",
#     'projectId': "surveiliadatabase",
#     'storageBucket': "surveiliadatabase.appspot.com",
#     'messagingSenderId': "950425588555",
#     'appId': "1:950425588555:web:597ccb15159a91b739cece",
#     'measurementId': "G-RG2D1HGXKS"
# }
# firebase = pyrebase.initialize_app(firebaseConfig)
# auth= firebase.auth()

count = 1


class ControlMainWindow(qtw.QMainWindow, Ui_surveiliaFrontEnd):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.logic = 0
        self.camSignal = 0
        self.mainStackedWidget.setCurrentIndex(0)
        self.menuStackedWidget.setCurrentIndex(0)

        ####################### MAIN STACKED WIDGET ###############################################
        #self.login1_pushButton.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(1))
        self.logout_toolButton.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(2))
        self.loginAgain_pushButton_3.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(0))

        ######################## MENU STACKED WIDGET ##############################################
        self.logo_toolButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(0))
        self.getStarted_pushButton_2.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(1))
        self.camera_toolButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(1))
        self.alarm_toolButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(2))
        self.storage_toolButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(3))
        self.account_toolButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(4))
        self.users_toolButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(5))
        self.userAdd_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(6))
        self.language_toolButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(8))

        ##########################CAMERA PAGE####################################################
        self.cam02_pushButton.hide()
        self.cam03_pushButton.hide()
        self.cam04_pushButton.hide()
        self.cam05_pushButton.hide()
        self.cam06_pushButton.hide()

        self.display_2.hide()
        self.display_3.hide()
        self.display_4.hide()
        self.display_5.hide()
        self.display_6.hide()

        self.addNew_pushButton.clicked.connect(self.addNewCamera)
        self.cancel_pushButton_3.clicked.connect(self.close)
        self.flag = 0

        self.cam01_pushButton.clicked.connect(self.cam1clicked)
        self.cam02_pushButton.clicked.connect(self.cam2clicked)
        self.cam03_pushButton.clicked.connect(self.cam3clicked)
        self.cam04_pushButton.clicked.connect(self.cam4clicked)
        self.cam05_pushButton.clicked.connect(self.cam5clicked)
        self.cam06_pushButton.clicked.connect(self.cam6clicked)

        """
        self.cam01_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7))
        self.cam02_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7))
        self.cam03_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7))
        self.cam04_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7))
        self.cam05_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7))
        self.cam06_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7))
        """

        # self.cam01_pushButton.clicked.connect(self.funct)
        # self.cam02_pushButton.clicked.connect(self.funct)
        # self.cam03_pushButton.clicked.connect(self.cam01_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7))funct)
        #
        # if self.cam01_pushButton.clicked:
        #     self.flag = 1
        #     print("STILL HERE")
        # elif self.cam02_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7)):
        #     self.flag = 2
        #     print("EEEE")
        # elif self.cam03_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7)):
        #     self.flag = 3
        #
        # elif self.cam04_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7)):
        #     self.flag = 4
        #
        # elif self.cam05_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7)):
        #     self.flag = 5
        #
        # elif self.cam06_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7)):
        #     self.flag = 6

        ##########################PAGE 7####################################################
        self.openDir_pushButton.clicked.connect(self.openFile)
        self.addIPCam_pushButton.clicked.connect(self.openIPcam)
        self.openWebcam_pushButton.clicked.connect(self.openWebcam)
        self.cancel_PushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(1))

        self.english_radioButton.toggled.connect(self.changeLanguagetoEnglish)
        self.urdu_radioButton.toggled.connect(self.changeLanguagetoUrdu)
        self.logout_toolButton.clicked.connect(self.changeLanguagetoEnglish)
        ######################## OPEN AND PLAY VIDEO ###############################################
        # create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        # pass the widget where the video will be displayed
        # self.mediaPlayer.setVideoOutput(self.videoDisplay_widget1)

        #######################LOGIN###########################################
        self.login1_pushButton.clicked.connect(self.Login)

    def Login(self):

        self.excel = xlrd.open_workbook('UsersList.xlsx')
        self.sheet1 = self.excel.sheet_by_index(0)

        for row in range(self.sheet1.nrows):
            #for id, username and password from excel

            cellID = str(self.sheet1.cell(row, 0))
            cellID = cellID.lstrip(":\'text") #to get data before text
            cellID = cellID.rstrip("\'")

            cellUserName = str(self.sheet1.cell(row, 1))
            cellUserName = cellUserName.lstrip(":\'text")
            cellUserName = cellUserName.rstrip("\'")
            """
            cellEmail = (self.sheet1.cell_value(row, 1))
            cellEmail = cellEmail.lstrip(":\'text")
            cellEmail = cellEmail.rstrip("\'")
            """
            cellPassword = str(self.sheet1.cell_value(row, 2))
            cellPassword = cellPassword.lstrip(":\'text")
            cellPassword = cellPassword.rstrip("\'")

            #to get values from gui
            # print(cellPassword)
            # print(cellUserName)
            #Name = str(self.username1_field.toPlainText())
            #Password = str(self.password1_field.toPlainText())
            Name = str(self.username1_field.text())
            Password = str(self.password1_field.text())
            # print(Name)
            # print(Password)
            # print(cellUserName)
            # print(cellPassword)
            if cellUserName == Name:
                print("HERE")
                if Password == cellPassword:
                    print("login successful")
                    self.mainStackedWidget.setCurrentIndex(1)
                    break
                else:
                    print("INVALID USERNAME OR PASSWORD")

            else:
                print("still in else")
            """
            else:
                if (cellEmail == Name):
                    if (Password == cellPassword):
                        print("Login Successful")

                        break
            """
    """
    def funct(self):
        if self.cam01_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7)):
            self.flag = 1
            print("STILL HERE")
        elif self.cam02_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7)):
            self.flag = 2
            print("EEEE")
        elif self.cam03_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7)):
            self.flag = 3

        elif self.cam04_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7)):
            self.flag = 4

        elif self.cam05_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7)):
            self.flag = 5

        elif self.cam06_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7)):
            self.flag = 6
    """

    def cam1clicked(self):
        self.camSignal = 1
        self.menuStackedWidget.setCurrentIndex(7)

    def cam2clicked(self):
        self.camSignal = 2
        self.menuStackedWidget.setCurrentIndex(7)

    def cam3clicked(self):
        self.camSignal = 3
        self.menuStackedWidget.setCurrentIndex(7)

    def cam4clicked(self):
        self.camSignal = 4
        self.menuStackedWidget.setCurrentIndex(7)

    def cam5clicked(self):
        self.camSignal = 5
        self.menuStackedWidget.setCurrentIndex(7)

    def cam6clicked(self):
        self.camSignal = 6
        self.menuStackedWidget.setCurrentIndex(7)

    # METHOD TO OPEN THE IP CAM THROUGH IP ADDRESS
    def openIPcam(self):

        url = str(self.addIPCam_field.text())
        self.menuStackedWidget.setCurrentIndex(1)
        while True:
            imgResp = urllib.request.urlopen(url)
            imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
            img = cv2.imdecode(imgNp, -1)

            if (self.camSignal == 1):
                dim = (self.display_1.width(), self.display_1.height())
                img1 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                height, width, _ = img1.shape
                bytesPerLine = 3 * width
                img1 = qtg.QImage(img1.data, width, height, bytesPerLine, qtg.QImage.Format_RGB888).rgbSwapped()
                self.display_1.setPixmap(qtg.QPixmap.fromImage(img1))
                # self.camSignal = 0

            elif (self.camSignal == 2):
                dim = (self.display_2.width(), self.display_2.height())
                img2 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                height, width, _ = img2.shape
                bytesPerLine = 3 * width
                img2 = qtg.QImage(img2.data, width, height, bytesPerLine, qtg.QImage.Format_RGB888).rgbSwapped()
                self.display_2.setPixmap(qtg.QPixmap.fromImage(img2))
                # self.camSignal = 0

            elif (self.camSignal == 3):
                dim = (self.display_3.width(), self.display_3.height())
                img3 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                height, width, _ = img3.shape
                bytesPerLine = 3 * width
                img3 = qtg.QImage(img3.data, width, height, bytesPerLine, qtg.QImage.Format_RGB888).rgbSwapped()
                self.display_3.setPixmap(qtg.QPixmap.fromImage(img3))
                # self.camSignal = 0

            elif (self.camSignal == 4):
                dim = (self.display_4.width(), self.display_4.height())
                img4 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                height, width, _ = img4.shape
                bytesPerLine = 3 * width
                img4 = qtg.QImage(img4.data, width, height, bytesPerLine, qtg.QImage.Format_RGB888).rgbSwapped()
                self.display_4.setPixmap(qtg.QPixmap.fromImage(img4))
                # self.camSignal = 0

            elif (self.camSignal == 5):
                dim = (self.display_5.width(), self.display_5.height())
                img5 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                height, width, _ = img5.shape
                bytesPerLine = 3 * width
                img5 = qtg.QImage(img5.data, width, height, bytesPerLine, qtg.QImage.Format_RGB888).rgbSwapped()
                self.display_5.setPixmap(qtg.QPixmap.fromImage(img5))
                # self.camSignal = 0

            elif (self.camSignal == 6):
                dim = (self.display_6.width(), self.display_6.height())
                img6 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                height, width, _ = img6.shape
                bytesPerLine = 3 * width
                img6 = qtg.QImage(img6.data, width, height, bytesPerLine, qtg.QImage.Format_RGB888).rgbSwapped()
                self.display_6.setPixmap(qtg.QPixmap.fromImage(img6))
                # self.camSignal = 0

            cv2.waitKey(10)

            # switcher = {
            #      1:  self.display_1.setPixmap(qtg.QPixmap.fromImage(img1)),
            #      2:  self.display_2.setPixmap(qtg.QPixmap.fromImage(img1)),
            #      3:  self.display_3.setPixmap(qtg.QPixmap.fromImage(img1)),
            #      4:  self.display_4.setPixmap(qtg.QPixmap.fromImage(img1)),
            #      5:  self.display_5.setPixmap(qtg.QPixmap.fromImage(img1)),
            #      6:  self.display_6.setPixmap(qtg.QPixmap.fromImage(img1))
            #  }
            """

            if self.flag == 1:
                self.display_1.setPixmap(qtg.QPixmap.fromImage(img1))
            elif self.flag == 2:
                self.display_2.setPixmap(qtg.QPixmap.fromImage(img1))
            elif self.flag == 3:
                self.display_3.setPixmap(qtg.QPixmap.fromImage(img1))
            elif self.flag == 4:
                self.display_4.setPixmap(qtg.QPixmap.fromImage(img1))
            elif self.flag == 5:
                self.display_5.setPixmap(qtg.QPixmap.fromImage(img1))
            elif self.flag == 6:
                self.display_6.setPixmap(qtg.QPixmap.fromImage(img1))

            cv2.waitKey(10)
            """

    # METHOD TO OPEN WEB CAM
    @pyqtSlot()
    def openWebcam(self):
        self.logic = 1
        cap = cv2.VideoCapture(0)
        date = datetime.datetime.now()
        out = cv2.VideoWriter('D:/Video/Video_%s%s%sT%s%s%s.mp4' % (
            date.year, date.month, date.day, date.hour, date.minute, date.second), -1, 20.2, (640, 480))
        self.menuStackedWidget.setCurrentIndex(1)

        while cap.isOpened():
            # capture video frame by frame
            ret, frame = cap.read()
            print(frame)
            if ret == True:
                self.displayImage(frame, 1)
                cv2.waitKey()

                if (self.logic == 1):
                    out.write(frame)
                    print("Camera Opened")

                if (self.logic == 0):
                    break
            else:
                print("Else not found")
        # release everything when job is finished
        cap.release()
        out.release()
        cv2.destroyAllWindows()

    # METHOD TO DISPLAY VIDEO(IMAGE BY IMAGE) IN THE BOX
    def displayImage(self, img, window=1):
        qformat = QImage.Format_Indexed8

        if len(img.shape) == 3:
            if (img.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        pix = qtg.QPixmap.fromImage(img)
        # pix = pix.scaled(self.display_1.width(), self.display_1.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        pix = pix.scaled(600, 450, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        if (self.camSignal == 1):

            self.display_1.setPixmap(pix)
            # self.camSignal = 0

        elif (self.camSignal == 2):
            self.display_2.setPixmap(pix)
            # self.camSignal = 0

        elif (self.camSignal == 3):
            # pix = pix.scaled(self.display_3.width(), self.display_3.height(), QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation)
            self.display_3.setPixmap(pix)
            # self.camSignal = 0

        elif (self.camSignal == 4):
            # pix = pix.scaled(self.display_4.width(), self.display_4.height(), QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation)
            self.display_4.setPixmap(pix)
            # self.camSignal = 0

        elif (self.camSignal == 5):
            # pix = pix.scaled(self.display_5.width(), self.display_5.height(), QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation)
            self.display_5.setPixmap(pix)
            # self.camSignal = 0

        elif (self.camSignal == 6):
            # pix = pix.scaled(self.display_6.width(), self.display_6.height(), QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation)
            self.display_6.setPixmap(pix)
            # self.camSignal = 0

        """
        print(self.flag)
        if self.flag == 1:
            self.display_1.setPixmap(pix)
            self.funct()
        elif self.flag == 2:
            self.display_2.setPixmap(pix)
            self.funct()
        elif self.flag == 3:
            self.display_3.setPixmap(pix)
            self.funct()
        elif self.flag == 4:
            self.display_4.setPixmap(pix)
            self.funct()
        elif self.flag == 5:
            self.display_5.setPixmap(pix)
            self.funct()
        elif self.flag == 6:
            self.display_6.setPixmap(pix)
            self.funct()
        else:
            print("NO")
        """

    # self.display_1.setPixmap(pix)

    # METHOD TO OPEN FILE DIALOG
    def openFile(self):

        fileName, _ = QFileDialog.getOpenFileName(self, "Open Video", "",
                                                  "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.wmv)")
        if fileName != '':
            self.displayImage(fileName, 1)
        else:
            print("NO FILE FOUND")
        display_1.play()
        self.menuStackedWidget.setCurrentIndex(1)

    # METHOD TO ADD NEW CAMERAS
    def addNewCamera(self):
        if self.cam02_pushButton.isHidden():
            self.cam02_pushButton.show()
            self.display_2.show()
        elif self.cam03_pushButton.isHidden():
            self.cam03_pushButton.show()
            self.display_3.show()
        elif self.cam04_pushButton.isHidden():
            self.cam04_pushButton.show()
            self.display_4.show()
        elif self.cam05_pushButton.isHidden():
            self.cam05_pushButton.show()
            self.display_5.show()
        elif self.cam06_pushButton.isHidden():
            self.cam06_pushButton.show()
            self.display_6.show()
        else:
            self.addNew_pushButton.setEnabled(False)
            self.addNew_pushButton.setStyleSheet("background-color: light grey ;\n")

            ############################TRANSLATE INTO URDU######################################
            # METHOD TO CHANGE LANGUAGE

    def changeLanguagetoUrdu(self):
        # self.title1_label.setText("سرویلیا")
        self.title_label.setText("سرویلیا")
        # self.title3_label.setText("سرویلیا")
        # self.username1_field.setPlaceholderText("صارف کا نام")
        # self.password1_field.setPlaceholderText("پاس ورڈ")
        # self.login1_pushButton.setText("لاگ ان کریں")
        # self.admin1_radioButton.setText("ایڈمن")
        # self.user1_radioButton.setText("صارف")
        # self.loginas1_label.setText("لاگ ان کے طور پر:")

        self.camera_toolButton.setText("کیمرہ")
        self.storage_toolButton.setText("اسٹوریج")
        self.logout_toolButton.setText("لاگ آوٹ")
        self.users_toolButton.setText("صارفین")
        self.language_toolButton.setText("زبان")
        self.logo_toolButton.setText("لاگ آوٹ")
        self.alarm_toolButton.setText("الارم لاگ")
        self.account_toolButton.setText("اکاؤنٹ")
        self.title_label.setText("سرویلیا")
        self.welcome_label.setText("سرویلیا میں خوش آمدید")
        self.getStarted_pushButton_2.setText("آو شروع کریں")
        self.cameras_label.setText("کیمرے")
        self.cam01_pushButton.setText("کیمرہ_01")
        self.cam03_pushButton.setText("کیمرہ_03")
        self.cam02_pushButton.setText("کیمرہ_02")
        self.cam04_pushButton.setText("کیمرہ_04")
        self.cam05_pushButton.setText("کیمرہ_05")
        self.cam06_pushButton.setText("کیمرہ_06")
        self.addNew_pushButton.setText("نیا شامل کریں")
        self.showAll_pushButton.setText("سب دکھائیں")
        self.alarmHistory_label.setText("الارم کی حسٹری")

        self.alarm_tableWidget.horizontalHeaderItem(0).setText(" ID کیمرہ ")
        self.alarm_tableWidget.horizontalHeaderItem(1).setText("وقت")
        self.alarm_tableWidget.horizontalHeaderItem(2).setText("الارم کی تفصیل")
        self.alarm_tableWidget.horizontalHeaderItem(3).setText("اناملی کلپ")
        self.storage_label.setText("اسٹوریج")
        self.show_label.setText("دکھائیں        ")
        self.anomalyClip_checkBox.setText("اناملی کلپ")
        self.cameraFeed_checkBox.setText("کیمرا فیڈ")

        self.storage_tableWidget.horizontalHeaderItem(0).setText("فائل کا نام")
        self.storage_tableWidget.horizontalHeaderItem(1).setText("تاریخ")
        self.storage_tableWidget.horizontalHeaderItem(2).setText("سائز")
        self.accountInfo_label.setText("اکاؤنٹ کی معلومات")
        self.username_label.setText("صارف نام")
        self.username_lineEdit.setText("Ifrah Tehleel")
        self.password_label.setText("پاس ورڈ")
        self.password_lineEdit.setText("Ifrah")
        self.contactInfo_label.setText("رابطہ کی معلومات")
        self.contactInfo_lineEdit.setText("+923014474797")
        self.address_label.setText("پتہ")
        self.edit_pushButton.setText("ترمیم کریں")
        self.userInfo_label.setText("صارفین کی معلومات")
        self.userAdd_pushButton.setText("شامل کریں")
        self.userDelete_pushButton.setText("حذف کریں")

        self.user_tableWidget.horizontalHeaderItem(0).setText("نام")
        self.user_tableWidget.horizontalHeaderItem(1).setText("پاس ورڈ")
        self.user_tableWidget.horizontalHeaderItem(2).setText("رابطہ کی معلومات")
        self.user_tableWidget.horizontalHeaderItem(3).setText("پتہ")
        self.addUser_label.setText("نیا صارف شامل کریں")
        self.aUsername_label.setText("صارف نام")
        self.aPassword_label.setText("پاس ورڈ")
        self.aContactInfo_label.setText("رابطہ کی معلومات")
        self.aAddress_label.setText("پتہ")
        self.aEdit_pushButton.setText("نیا صارف شامل کریں")
        """
        self.label.setText("IP ایڈریس کا استعمال کرتے ہوئے کیمرا شامل کریں")
        self.addIPCam_field.setText("IP ایڈریس یہاں داخل کریں")
        self.addIPCam_pushButton.setText("شامل کریں")
        self.label_2.setText("ڈائریکٹری سے فائل کے ذریعہ ویڈیو شامل کریں")
        self.openDir_pushButton.setText("کھولیں")
        self.label_3.setText("ویب کیم کا استعمال کرتے ہوئے شامل کریں")
        self.openWebcam_pushButton.setText("ویب کیم کھولیں")
        self.cancel_PushButton.setText("منسوخ کریں")
        """
        self.english_radioButton.setText("English")
        self.chooseLanguage_label.setText("زبان کا انتخاب کریں:")
        self.urdu_radioButton.setText("Urdu")
        self.title3_label.setText("سرویلیا")
        self.cancel_pushButton_3.setText("منسوخ کریں")
        self.loginAgain_pushButton_3.setText("دوبارہ لاگ ان")
        self.loggedOut_label_3.setText("آپ لاگ آؤٹ ہوچکے ہیں")

        ##########################TRANSLATE INTO ENGLISH###################################

    def changeLanguagetoEnglish(self):
        # self.title1_label.setText("SURVEILIA")
        # self.username1_field.setPlaceholderText("Username")
        # self.password1_field.setPlaceholderText("Password")
        # self.login1_pushButton.setText("LOGIN")
        # self.admin1_radioButton.setText("Admin")
        # self.user1_radioButton.setText("User")
        # self.loginas1_label.setText("Login as:")
        self.camera_toolButton.setText("Camera")
        self.storage_toolButton.setText("Storage")
        self.logout_toolButton.setText("Logout")
        self.users_toolButton.setText("Users")
        self.language_toolButton.setText("Language")
        self.logo_toolButton.setText("Logout")
        self.alarm_toolButton.setText("Alarm Log")
        self.account_toolButton.setText("Account")
        self.title_label.setText("SURVEILIA")
        self.welcome_label.setText("Welcome to SURVEILIA")
        self.getStarted_pushButton_2.setText("GET STARTED")
        self.cameras_label.setText("CAMERAS")
        self.cam01_pushButton.setText("CAMERA_01")
        self.cam03_pushButton.setText("CAMERA_03")
        self.cam02_pushButton.setText("CAMERA_02")
        self.cam04_pushButton.setText("CAMERA_04")
        self.cam05_pushButton.setText("CAMERA_05")
        self.cam06_pushButton.setText("CAMERA_06")
        self.addNew_pushButton.setText("ADD NEW")
        self.showAll_pushButton.setText("SHOW ALL")
        self.alarmHistory_label.setText("ALARM HISTORY")

        self.alarm_tableWidget.horizontalHeaderItem(0).setText("Camera ID")
        self.alarm_tableWidget.horizontalHeaderItem(1).setText("Time")
        self.alarm_tableWidget.horizontalHeaderItem(2).setText("Alarm Description")
        self.alarm_tableWidget.horizontalHeaderItem(3).setText("Anomaly Clip")
        self.storage_label.setText("STORAGE")
        self.show_label.setText("           Show:")
        self.anomalyClip_checkBox.setText("Anomaly Clip")
        self.cameraFeed_checkBox.setText("Camera Feed")

        self.storage_tableWidget.horizontalHeaderItem(0).setText("Filename")
        self.storage_tableWidget.horizontalHeaderItem(1).setText("Date")
        self.storage_tableWidget.horizontalHeaderItem(2).setText("Size")
        self.accountInfo_label.setText("ACCOUNT INFORMATION")
        self.username_label.setText("Username:")
        self.username_lineEdit.setText("Ifrah Tehleel")
        self.password_label.setText("Password:")
        self.password_lineEdit.setText("Ifrah")
        self.contactInfo_label.setText("Contact Info:")
        self.contactInfo_lineEdit.setText("+923014474797")
        self.address_label.setText("Address:")
        self.edit_pushButton.setText("EDIT")
        self.userInfo_label.setText("  USERS INFORMATION")
        self.userAdd_pushButton.setText("ADD")
        self.userDelete_pushButton.setText("DELETE")

        self.user_tableWidget.horizontalHeaderItem(0).setText("Name")
        self.user_tableWidget.horizontalHeaderItem(1).setText("Password")
        self.user_tableWidget.horizontalHeaderItem(2).setText("Contact Info")
        self.user_tableWidget.horizontalHeaderItem(3).setText("Address")
        self.addUser_label.setText("ADD NEW USER")
        self.aUsername_label.setText("Username:")
        self.aPassword_label.setText("Password:")
        self.aContactInfo_label.setText("Contact Info:")
        self.aAddress_label.setText("Address:")
        self.aEdit_pushButton.setText("ADD USER")
        """
        self.label.setText("Add camera using IP Address")
        self.addIPCam_field.setText("ENTER IP ADDRESS HERE")
        self.addIPCam_pushButton.setText("ADD")
        self.label_2.setText("Add video by file from Directory")
        self.openDir_pushButton.setText("OPEN")
        self.label_3.setText("Add using Webcam")
        self.openWebcam_pushButton.setText("OPEN WEBCAM")
        self.cancel_PushButton.setText("CANCEL")
        """
        self.english_radioButton.setText("English")
        self.chooseLanguage_label.setText("Choose Language:")
        self.urdu_radioButton.setText("Urdu")
        self.title3_label.setText("SURVEILIA")
        self.cancel_pushButton_3.setText("CANCEL")
        self.loginAgain_pushButton_3.setText("LOGIN AGAIN")
        self.loggedOut_label_3.setText("You have been logged out!")
    #
    # # METHOD TO OPEN THE IP CAM THROUGH IP ADDRESS
    # def openIPcam(self):
    #     url = str(self.addIPCam_field.text())
    #     self.menuStackedWidget.setCurrentIndex(1)
    #
    #     while True:
    #         imgResp = urllib.request.urlopen(url)
    #         imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    #         img = cv2.imdecode(imgNp, -1)
    #
    #         dim = (700, 721)
    #         img1 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    #         height, width, _ = img1.shape
    #         bytesPerLine = 3 * width
    #         img1 = qtg.QImage(img1.data, width, height, bytesPerLine, qtg.QImage.Format_RGB888).rgbSwapped()
    #
    #         self.display_1.setPixmap(qtg.QPixmap.fromImage(img1))
    #         cv2.waitKey(10)
    #
    # # METHOD TO OPEN WEBCAM
    # @pyqtSlot()
    # def openWebcam(self):
    #     self.logic = 1
    #     cap = cv2.VideoCapture(0)
    #     date = datetime.datetime.now()
    #     out = cv2.VideoWriter('D:/Video/Video_%s%s%sT%s%s%s.mp4' % (
    #         date.year, date.month, date.day, date.hour, date.minute, date.second), -1, 20.2, (640, 480))
    #
    #     while cap.isOpened():
    #         # capture video frame by frame
    #         ret, frame = cap.read()
    #         print(frame)
    #         if ret == True:
    #             self.displayImage(frame, 1)
    #             cv2.waitKey()
    #
    #             if (self.logic == 1):
    #                 out.write(frame)
    #                 print("Camera Opened")
    #
    #             if (self.logic == 0):
    #                 break
    #         else:
    #             print("Else not found")
    #     # release everything when job is finished
    #     cap.release()
    #     out.release()
    #     cv2.destroyAllWindows()
    #
    # # METHOD TO DISPLAY VIDEO(IMAGE BY IMAGE) IN THE BOX
    # def displayImage(self, img, window=1):
    #     qformat = QImage.Format_Indexed8
    #     self.menuStackedWidget.setCurrentIndex(1)
    #
    #     if len(img.shape) == 3:
    #         if (img.shape[2]) == 4:
    #             qformat = QImage.Format_RGBA8888
    #         else:
    #             qformat = QImage.Format_RGB888
    #
    #     img = QImage(img, img.shape[1], img.shape[0], qformat)
    #     img = img.rgbSwapped()
    #     pix = qtg.QPixmap.fromImage(img)
    #     pix = pix.scaled(241, 221, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
    #
    #     self.display_1.setPixmap(pix)
    #
    # # METHOD TO OPEN FILE DIALOG
    # def openFile(self):
    #
    #     fileName, _ = QFileDialog.getOpenFileName(self, "Open Video", "",
    #                                               "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.wmv)")
    #     if fileName != '':
    #         self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
    #     else:
    #         print("NO FILE FOUND")
    #     if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
    #         self.mediaPlayer.pause()
    #     else:
    #         self.mediaPlayer.play()
    #     self.menuStackedWidget.setCurrentIndex(0)

    # self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
    # # #############################################################################################
    # # Setup the playlist.
    # self.playlist = QMediaPlaylist()
    # self.player.setPlaylist(self.playlist)
    # self.model = PlaylistModel(self.playlist)
    # self.cameraList.setModel(self.model)
    # self.playlist.currentIndexChanged.connect(self.playlist_position_changed)
    # selection_model = self.playlistView.selectionModel()
    # selection_model.selectionChanged.connect(self.playlist_selection_changed)

    # METHOD TO ADD BUTTONS DYNAMICALLY
    # def AddNewButton(self):
    #     global count
    #     b = QtWidgets.QPushButton("CAMERA_0" + str(count+1), self.camera_page)
    #     self.gridLayout.addWidget(b, count, 0)
    #     #b.setAccessibleName("CAMERA_0" + str(count+1))
    #     b.clicked.connect(self.Button)
    #     count += 1
    #
    # def Button(self):
    #     sender = self.sender()
    #     print(str(sender.text()))
    #     sender.clicked.connect(self.openFile())

    # def mediastate_changed(self):
    #     if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
    #         self.play_pushButton.setIcon(
    #             self.style().standardIcon(QStyle.SP_MediaPause)
    #         )
    #     else:
    #         self.play_pushButton.setIcon(
    #             self.style().standardIcon(QStyle.SP_MediaPlay)
    #         )

    # def loginFunction(self):
    #	email = self.username1_field.text()
    #	password = self.password1_field.text()
    #	try:
    #	   auth.sign_in_with_email_and_password(email,password)


if __name__ == "__main__":
    app = qtw.QApplication([])
    widget = ControlMainWindow()
    widget.show()
    try:
        app.exec_()

    except:
        print("EXITING")
