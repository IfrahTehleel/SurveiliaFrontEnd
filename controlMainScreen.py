from surveiliaFrontEnd import Ui_surveiliaFrontEnd
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc


class ControlMainWindow(qtw.QMainWindow, Ui_surveiliaFrontEnd):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.mainStackedWidget.setCurrentIndex(0)
        self.menuStackedWidget.setCurrentIndex(0)
        ###################################################################################################
        self.login1_pushButton.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(1))
        self.logout_toolButton.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(2))
        self.loginAgain_pushButton_3.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(0))

        ####################################################################################################
        self.camera_toolButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(0))
        self.alarm_toolButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(1))
        self.storage_toolButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(2))
        self.account_toolButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(3))
        self.users_toolButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(4))
        self.help_toolButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(5))
        self.userAdd_pushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(6))


if __name__ == "__main__":
    app = qtw.QApplication([])
    widget = ControlMainWindow()
    widget.show()
    app.exec_()
