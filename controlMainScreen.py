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

        ########################OPEN AND PLAY VIDEO###############################################

        # create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        # pass the widget where the video will be displayed
        self.mediaPlayer.setVideoOutput(self.videoDisplay_widget)

        self.play_pushButton.clicked.connect(self.playVideo)
        self.openVideo_pushButton.clicked.connect(self.openFile)

        # self.mediaPlayer.stateChanged.connect(self.mediastate_changed)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if fileName != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.play_pushButton.setEnabled(True)

    def playVideo(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

        else:
            self.mediaPlayer.play()

    # def mediastate_changed(self):
    #     if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
    #         self.play_pushButton.setIcon(
    #             self.style().standardIcon(QStyle.SP_MediaPause)
    #         )
    #     else:
    #         self.play_pushButton.setIcon(
    #             self.style().standardIcon(QStyle.SP_MediaPlay)
    #         )
    #


if __name__ == "__main__":
    app = qtw.QApplication([])
    widget = ControlMainWindow()
    widget.show()
    app.exec_()
