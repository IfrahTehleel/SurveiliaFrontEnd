from loginscreen import Ui_loginscreen
from adminMain import Ui_adminMain
from userMain import Ui_userMain
from loggedoutscreen import Ui_loggedoutscreen
from addNewUser import Ui_addNewUser
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import sys


class otherWindow(qtw.QMainWindow, Ui_loginscreen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self.login_pushButton.clicked.connect(lambda: self.authenticate())

    def authenticate(self):
        username = self.username_field.text()
        password = self.password_field.text()

        if username == 'ifrah' and password == 'password':
            print("LOGIN")


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    widget = otherWindow(windowTitle='Surveilia')
    widget.show()
    sys.exit(app.exec_())
