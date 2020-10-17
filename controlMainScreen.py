import datetime

from PyQt5.QtCore import QUrl, QDir, QTimer, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QStyle

from surveiliaFrontEnd import Ui_surveiliaFrontEnd
from PyQt5 import QtWidgets as qtw, QtWidgets, QtCore
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import sys
import os
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QPushButton
from dialogg import Ui_Dialog

import urllib.request
import cv2
import numpy as np

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


class ControlMainWindow(qtw.QMainWindow, Ui_surveiliaFrontEnd, Ui_Dialog):

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
        self.camera_toolButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(0))
        self.alarm_toolButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(1))
        self.storage_toolButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(2))
        self.account_toolButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(3))
        self.users_toolButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(4))
        self.help_toolButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(5))
        self.userAdd_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(6))
        # self.showAll_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(8))

        ############################################################################################
        self.cam02_pushButton.hide()
        self.cam03_pushButton.hide()
        self.cam04_pushButton.hide()
        self.cam05_pushButton.hide()
        self.cam06_pushButton.hide()

        self.videoDisplay_widget2.hide()
        self.addNew_pushButton.clicked.connect(self.addNewCamera)

        ######################## OPEN AND PLAY VIDEO ###############################################

        # create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer2 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer3 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer4 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        # self.mediaPlayer5 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        # self.mediaPlayer6 = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # pass the widget where the video will be displayed
        self.mediaPlayer.setVideoOutput(self.videoDisplay_widget1)
        self.mediaPlayer2.setVideoOutput(self.videoDisplay_widget2)
        self.mediaPlayer3.setVideoOutput(self.videoDisplay_widget3)
        # self.mediaPlayer4.setVideoOutput(self.videoDisplay_widget4)
        # self.mediaPlayer4.setVideoOutput(self.videoDisplay_widget5)
        # self.mediaPlayer4.setVideoOutput(self.videoDisplay_widget6)
        self.cancel_pushButton_3.clicked.connect(self.close)

        self.cam01_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(8))
        self.openDir_pushButton.clicked.connect(self.openFile)
        self.addIPCam_pushButton.clicked.connect(self.openIPcam)
        self.openWebcam_pushButton.clicked.connect(self.openWebcam)

    def openIPcam(self):
        url = self.addIPCam_field.text()
        self.menuStackedWidget.setCurrentIndex(0)
        while True:
            imgResp = urllib.request.urlopen(url)
            imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
            img = cv2.imdecode(imgNp, -1)
            # # cv2.imwrite("yes", img)
            # dim = (241, 221)
            # img1 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            # height, width, bytesPerComponent = img1.shape
            # bytesPerLine = 3 * width
            # img1 = qtg.QImage(img1.data, width, height, bytesPerLine, qtg.QImage.Format_RGB888).rgbSwapped()
            # self.opencvlabel.setPixmap(qtg.QPixmap.fromImage(img1))
            # # cv2.imshow('test', img)
            # # cv2.waitKey(10)
            # self.menuStackedWidget.setCurrentIndex(0)

    @pyqtSlot()
    def openWebcam(self):
        self.logic = 1
        cap = cv2.VideoCapture("D:/SurveiliaFrontEnd/video.wmv")
        date = datetime.datetime.now()
        out = cv2.VideoWriter('D:/Video/Video_%s%s%sT%s%s%s.mp4' % (
            date.year, date.month, date.day, date.hour, date.minute, date.second), -1, 20.2, (640, 480))
        print('here')

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

        self.opencvlabel.setPixmap(pix)
        self.menuStackedWidget.setCurrentIndex(0)

        #     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #     img = qtg.QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        #     pix = qtg.QPixmap.fromImage(img)
        #     pix = pix.scale(241, 221, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        #     self.opencvlabel.setPixmap(qtg.QPixmap.fromImage(pix))
        #
        #     #self.ui.frame = pix  # or img depending what `ui.frame` needs
        #
        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         break
        #
        # cap.release()
        #
        #

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

    def addNewCamera(self):
        if self.cam02_pushButton.isHidden():
            self.cam02_pushButton.show()
        elif self.cam03_pushButton.isHidden():
            self.cam03_pushButton.show()
        elif self.cam04_pushButton.isHidden():
            self.cam04_pushButton.show()
        elif self.cam05_pushButton.isHidden():
            self.cam05_pushButton.show()
        elif self.cam06_pushButton.isHidden():
            self.cam06_pushButton.show()
        else:
            self.addNew_pushButton.setEnabled(False)
            self.addNew_pushButton.setStyleSheet("background-color: light grey ;\n")

        # self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        # self.mediaPlayer.setVideoOutput(self.videoDisplay_widget1)
        # self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('video.mov')))

        # if self.cam02_pushButton.
        #     self.videoDisplay_widget2.show()
        #     self.videoDisplay_widget2.setStyleSheet("background-color : black")

        # def camm(self):
        #     self.Dialog = QtWidgets.QDialog()
        #     self.ui = Ui_Dialog()
        #     self.ui.setupUi(self.Dialog)
        #     self.Dialog.show()
        #
        #
        #

        # self.play_pushButton.clicked.connect(self.playVideo)
        # self.cam01_pushButton.clicked.connect(self.openFile)
        # self.cam02_pushButton.clicked.connect(self.openFile2)
        # self.cam03_pushButton.clicked.connect(self.openFile3)
        # self.cam04_pushButton.clicked.connect(self.openFile4)

        # if self.cam02_pushButton.isHidden():
        #     self.videoDisplay_widget2.

        # self.cam03_pushButton.clicked.connect(self.openFile3)
        # self.cam04_pushButton.clicked.connect(self.openFile)
        # self.cam05_pushButton.clicked.connect(self.openFile)
        # self.cam06_pushButton.clicked.connect(self.openFile)

        # self.openVideo_pushButton_2.clicked.connect(self.openFile2)
        # self.addNew_pushButton.clicked.connect(self.AddNewButton)

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

    #
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

    # def openFile2(self):
    #
    #
    #         fileName, _ = QFileDialog.getOpenFileName(self, "Open Video", "",
    #                                                   "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.wmv)")
    #         if fileName != '':
    #             self.mediaPlayer2.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
    #         else:
    #             print("NO FILE FOUND")
    #         if self.mediaPlayer2.state() == QMediaPlayer.PlayingState:
    #             self.mediaPlayer2.pause()
    #         else:
    #             self.mediaPlayer2.play()
    #
    # def openFile3(self):
    #
    #
    #         fileName, _ = QFileDialog.getOpenFileName(self, "Open Video", "",
    #                                                   "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.wmv)")
    #         if fileName != '':
    #             self.mediaPlayer3.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
    #         else:
    #             print("NO FILE FOUND")
    #         if self.mediaPlayer3.state() == QMediaPlayer.PlayingState:
    #             self.mediaPlayer3.pause()
    #         else:
    #             self.mediaPlayer3.play()

    # def openFile4(self):
    #
    #
    #         fileName, _ = QFileDialog.getOpenFileName(self, "Open Video", "",
    #                                                   "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.wmv)")
    #         if fileName != '':
    #             self.mediaPlayer4.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
    #         else:
    #             print("NO FILE FOUND")
    #         if self.mediaPlayer4.state() == QMediaPlayer.PlayingState:
    #             self.mediaPlayer4.pause()
    #         else:
    #             self.mediaPlayer4.play()

    # def openFile2(self):
    #      fileName2, _ = QFileDialog.getOpenFileName(self, "Open Video", "",
    #                                                "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.wmv)")
    #
    #      if fileName2 != '':
    #          self.mediaPlayer2.setMedia(QMediaContent(QUrl.fromLocalFile(fileName2)))
    #          self.play_pushButton.setEnabled(True)
    #      if self.mediaPlayer2.state() == QMediaPlayer.PlayingState:
    #          self.mediaPlayer2.pause()
    #      else:
    #          self.mediaPlayer2.play()
    #
    # def openFile3(self):
    #     fileName3, _ = QFileDialog.getOpenFileName(self, "Open Video", "",
    #                                                "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.wmv)")
    #
    #     if fileName3 != '':
    #         self.mediaPlayer3.setMedia(QMediaContent(QUrl.fromLocalFile(fileName3)))
    #         self.play_pushButton.setEnabled(True)
    #     if self.mediaPlayer3.state() == QMediaPlayer.PlayingState:
    #         self.mediaPlayer3.pause()
    #     else:
    #         self.mediaPlayer3.play()

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


# except:

if __name__ == "__main__":
    app = qtw.QApplication([])
    widget = ControlMainWindow()
    widget.show()
    try:
        app.exec_()

    except:
        print("EXITING")
