import datetime
import sys
import os
import urllib.request
import cv2
import numpy as np
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
        self.mainStackedWidget.setCurrentIndex(0)
        self.menuStackedWidget.setCurrentIndex(0)

        ####################### MAIN STACKED WIDGET ###############################################
        self.login1_pushButton.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(1))
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

        self.cam01_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7))
        self.cam02_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7))
        self.cam03_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7))
        self.cam04_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7))
        self.cam05_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7))
        self.cam06_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(7))

        ##########################PAGE 7####################################################
        self.openDir_pushButton.clicked.connect(self.openFile)
        self.addIPCam_pushButton.clicked.connect(self.openIPcam)
        self.openWebcam_pushButton.clicked.connect(self.openWebcam)
        self.cancel_PushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(1))

        ######################## OPEN AND PLAY VIDEO ###############################################
        # create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        # pass the widget where the video will be displayed
        #self.mediaPlayer.setVideoOutput(self.videoDisplay_widget1)

    # METHOD TO OPEN THE IP CAM THROUGH IP ADDRESS
    def openIPcam(self):
        url = str(self.addIPCam_field.text())
        self.menuStackedWidget.setCurrentIndex(0)
        while True:
            imgResp = urllib.request.urlopen(url)
            imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
            img = cv2.imdecode(imgNp, -1)
            dim = (241, 221)
            img1 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            height, width, _ = img1.shape
            bytesPerLine = 3 * width
            img1 = qtg.QImage(img1.data, width, height, bytesPerLine, qtg.QImage.Format_RGB888).rgbSwapped()

            self.display1.setPixmap(qtg.QPixmap.fromImage(img1))
            self.menuStackedWidget.setCurrentIndex(0)
            cv2.waitKey(10)

    # METHOD TO OPEN WEBCAM
    @pyqtSlot()
    def openWebcam(self):
        self.logic = 1
        cap = cv2.VideoCapture(0)
        date = datetime.datetime.now()
        out = cv2.VideoWriter('D:/Video/Video_%s%s%sT%s%s%s.mp4' % (
            date.year, date.month, date.day, date.hour, date.minute, date.second), -1, 20.2, (640, 480))

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
        pix = pix.scaled(241, 221, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)

        self.display2.setPixmap(pix)
        self.menuStackedWidget.setCurrentIndex(0)

    # METHOD TO OPEN FILE DIALOG
    def openFile(self):

        fileName, _ = QFileDialog.getOpenFileName(self, "Open Video", "",
                                                  "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.wmv)")
        if fileName != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
        else:
            print("NO FILE FOUND")
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
        self.menuStackedWidget.setCurrentIndex(0)

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
