class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.player = QMediaPlayer()
        self.player.error.connect(self.erroralert)
   # Connect control buttons/slides for media player.
            self.playButton.pressed.connect(self.player.play)
            self.pauseButton.pressed.connect(self.player.pause)
            self.stopButton.pressed.connect(self.player.stop)
