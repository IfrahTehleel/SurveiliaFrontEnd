from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtWidgets import QFileDialog, QStyle

from surveiliaFrontEnd import Ui_surveiliaFrontEnd
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import sys
import os
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QPushButton
#import pyrebase
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

class ControlMainWindow(qtw.QMainWindow, Ui_surveiliaFrontEnd):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

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

        ######################## OPEN AND PLAY VIDEO ###############################################

        # create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer2 = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # pass the widget where the video will be displayed
        self.mediaPlayer.setVideoOutput(self.videoDisplay_widget_1)
        self.mediaPlayer2.setVideoOutput(self.videoDisplay_widget_2)

        #self.play_pushButton.clicked.connect(self.playVideo)
        self.openVideo_pushButton_1.clicked.connect(self.openFile)
        self.openVideo_pushButton_2.clicked.connect(self.openFile2)
        self.cancel_pushButton_3.clicked.connect(self.close)

        # self.mediaPlayer.stateChanged.connect(self.mediastate_changed)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Video", "",  "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.wmv)")

        if fileName != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.play_pushButton.setEnabled(True)
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
    def openFile2(self):
        fileName2, _ = QFileDialog.getOpenFileName(self, "Open Video", "",
                                                  "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.wmv)")

        if fileName2 != '':
            self.mediaPlayer2.setMedia(QMediaContent(QUrl.fromLocalFile(fileName2)))
            self.play_pushButton.setEnabled(True)
        if self.mediaPlayer2.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer2.pause()
        else:
            self.mediaPlayer2.play()





    # def mediastate_changed(self):
    #     if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
    #         self.play_pushButton.setIcon(
    #             self.style().standardIcon(QStyle.SP_MediaPause)
    #         )
    #     else:
    #         self.play_pushButton.setIcon(
    #             self.style().standardIcon(QStyle.SP_MediaPlay)
    #         )
    #def loginFunction(self):
    #	email = self.username1_field.text()
    #	password = self.password1_field.text()
    #	try:
    #	   auth.sign_in_with_email_and_password(email,password)
	#except:
if __name__ == "__main__":
    app = qtw.QApplication([])
    widget = ControlMainWindow()
    widget.show()
    app.exec_()
