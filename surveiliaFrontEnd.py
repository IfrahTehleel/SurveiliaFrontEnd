# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'surveiliaFrontEnd.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_surveiliaFrontEnd(object):
    def setupUi(self, surveiliaFrontEnd):
        surveiliaFrontEnd.setObjectName("surveiliaFrontEnd")
        surveiliaFrontEnd.resize(1198, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(surveiliaFrontEnd.sizePolicy().hasHeightForWidth())
        surveiliaFrontEnd.setSizePolicy(sizePolicy)
        surveiliaFrontEnd.setMinimumSize(QtCore.QSize(1000, 800))
        surveiliaFrontEnd.setMaximumSize(QtCore.QSize(16777215, 16777215))
        surveiliaFrontEnd.setSizeIncrement(QtCore.QSize(0, 0))
        surveiliaFrontEnd.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"font-size: 30px;\n"
"background-color:#1C1D25;\n"
"}\n"
"QFrame{\n"
"background: #2A2F3C ;\n"
"border-radius:10px;\n"
"\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"font-weight: bold;\n"
"}\n"
"QToolButton{\n"
"background:white;\n"
"border-radius:60px;\n"
"}\n"
"QLineEdit{\n"
"background: transparent;\n"
"border:none;\n"
"color:BLACK;\n"
"border-bottom:1px solid black;\n"
"font-size:20px;\n"
"}\n"
"QPushButton{\n"
"font-size:18px;\n"
"font-weight:bold;\n"
"color:white ;\n"
"background:#1C1D25;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"#logoLabel{\n"
"background:transparent;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(surveiliaFrontEnd)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mainStackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.mainStackedWidget.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"background-color:#1C1D25;\n"
"}\n"
"QLineEdit, QTextEdit{\n"
"background: #1C1D25;\n"
"border:#1C1D25;\n"
"color:white;\n"
"font-size:18px;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"font-size: 18px;\n"
"\n"
"}\n"
"QPushButton, QToolButton{\n"
"font-weight:bold;\n"
"color:white ;\n"
"background:#1C1D25;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"")
        self.mainStackedWidget.setObjectName("mainStackedWidget")
        self.login_page = QtWidgets.QWidget()
        self.login_page.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"font-size: 30px;\n"
"background-color:#1C1D25;\n"
"}\n"
"QFrame{\n"
"background: #2A2F3C ;\n"
"border-radius:10px;\n"
"\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"font-weight: bold;\n"
"}\n"
"QToolButton{\n"
"background:white;\n"
"border-radius:60px;\n"
"}\n"
"QLineEdit{\n"
"background: transparent;\n"
"border:none;\n"
"color:WHITE;\n"
"border-bottom:1px solid WHITE;\n"
"font-size:20px;\n"
"\n"
"}\n"
"QPushButton{\n"
"font-size:18px;\n"
"font-weight:bold;\n"
"color:white ;\n"
"background-color:#1C1D25;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"#logoLabel{\n"
"background:transparent;\n"
"}")
        self.login_page.setObjectName("login_page")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.login_page)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.login_widget = QtWidgets.QWidget(self.login_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_widget.sizePolicy().hasHeightForWidth())
        self.login_widget.setSizePolicy(sizePolicy)
        self.login_widget.setMinimumSize(QtCore.QSize(560, 600))
        self.login_widget.setObjectName("login_widget")
        self.logo1_label = QtWidgets.QLabel(self.login_widget)
        self.logo1_label.setGeometry(QtCore.QRect(200, 80, 150, 100))
        self.logo1_label.setStyleSheet("background: transparent;")
        self.logo1_label.setText("")
        self.logo1_label.setPixmap(QtGui.QPixmap(":/logo/surveilialogo.PNG"))
        self.logo1_label.setScaledContents(True)
        self.logo1_label.setObjectName("logo1_label")
        self.loginForm_frame = QtWidgets.QFrame(self.login_widget)
        self.loginForm_frame.setGeometry(QtCore.QRect(70, 130, 411, 571))
        self.loginForm_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginForm_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginForm_frame.setObjectName("loginForm_frame")
        self.title1_label = QtWidgets.QLabel(self.loginForm_frame)
        self.title1_label.setGeometry(QtCore.QRect(110, 100, 221, 71))
        self.title1_label.setStyleSheet("font-size:35px;")
        self.title1_label.setObjectName("title1_label")
        self.username1_field = QtWidgets.QLineEdit(self.loginForm_frame)
        self.username1_field.setGeometry(QtCore.QRect(50, 190, 301, 30))
        self.username1_field.setObjectName("username1_field")
        self.password1_field = QtWidgets.QLineEdit(self.loginForm_frame)
        self.password1_field.setGeometry(QtCore.QRect(50, 250, 301, 30))
        self.password1_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password1_field.setObjectName("password1_field")
        self.login1_pushButton = QtWidgets.QPushButton(self.loginForm_frame)
        self.login1_pushButton.setGeometry(QtCore.QRect(100, 440, 211, 40))
        self.login1_pushButton.setObjectName("login1_pushButton")
        self.admin1_radioButton = QtWidgets.QRadioButton(self.loginForm_frame)
        self.admin1_radioButton.setGeometry(QtCore.QRect(210, 350, 92, 16))
        self.admin1_radioButton.setStyleSheet("QRadioButton{\n"
"color:WHITE;\n"
"font-size:16px;\n"
"background:transparent;\n"
"\n"
"\n"
"}")
        self.admin1_radioButton.setObjectName("admin1_radioButton")
        self.user1_radioButton = QtWidgets.QRadioButton(self.loginForm_frame)
        self.user1_radioButton.setGeometry(QtCore.QRect(210, 320, 61, 20))
        self.user1_radioButton.setStyleSheet("QRadioButton{\n"
"color:WHITE;\n"
"font-size:16px;\n"
"background:transparent;\n"
"\n"
"}")
        self.user1_radioButton.setObjectName("user1_radioButton")
        self.loginas1_label = QtWidgets.QLabel(self.loginForm_frame)
        self.loginas1_label.setGeometry(QtCore.QRect(70, 320, 81, 41))
        self.loginas1_label.setStyleSheet("*{\n"
"background: transparent;\n"
"border:none;\n"
"color:WHITE;\n"
"font-size:18px;\n"
"font-weight:500;\n"
"\n"
"}")
        self.loginas1_label.setObjectName("loginas1_label")
        self.logo1_toolButton = QtWidgets.QToolButton(self.login_widget)
        self.logo1_toolButton.setGeometry(QtCore.QRect(210, 70, 120, 120))
        self.logo1_toolButton.setText("")
        self.logo1_toolButton.setObjectName("logo1_toolButton")
        self.loginForm_frame.raise_()
        self.logo1_toolButton.raise_()
        self.logo1_label.raise_()
        self.horizontalLayout.addWidget(self.login_widget)
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.mainStackedWidget.addWidget(self.login_page)
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.main_page)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.menuBar = QtWidgets.QWidget(self.main_page)
        self.menuBar.setMinimumSize(QtCore.QSize(80, 0))
        self.menuBar.setMaximumSize(QtCore.QSize(80, 16777215))
        self.menuBar.setStyleSheet("*{background: #1C1D25;\n"
"font-size: 16px;\n"
"}\n"
"QToolButton:hover{\n"
"     background-color:#2A2F3C;\n"
"}\n"
"QToolButton:pressed{\n"
"     background-color: #2A2F3C ;     \n"
"}")
        self.menuBar.setObjectName("menuBar")
        self.camera_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.camera_toolButton.setGeometry(QtCore.QRect(0, 100, 80, 71))
        self.camera_toolButton.setMinimumSize(QtCore.QSize(80, 0))
        self.camera_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.camera_toolButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("camera-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.camera_toolButton.setIcon(icon)
        self.camera_toolButton.setIconSize(QtCore.QSize(30, 30))
        self.camera_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.camera_toolButton.setObjectName("camera_toolButton")
        self.storage_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.storage_toolButton.setGeometry(QtCore.QRect(0, 270, 80, 71))
        self.storage_toolButton.setMinimumSize(QtCore.QSize(80, 0))
        self.storage_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.storage_toolButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("database-5-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.storage_toolButton.setIcon(icon1)
        self.storage_toolButton.setIconSize(QtCore.QSize(30, 30))
        self.storage_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.storage_toolButton.setObjectName("storage_toolButton")
        self.logout_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.logout_toolButton.setGeometry(QtCore.QRect(0, 630, 80, 71))
        self.logout_toolButton.setMinimumSize(QtCore.QSize(80, 0))
        self.logout_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.logout_toolButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("logout-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_toolButton.setIcon(icon2)
        self.logout_toolButton.setIconSize(QtCore.QSize(30, 30))
        self.logout_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.logout_toolButton.setObjectName("logout_toolButton")
        self.users_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.users_toolButton.setGeometry(QtCore.QRect(0, 450, 80, 71))
        self.users_toolButton.setMinimumSize(QtCore.QSize(80, 0))
        self.users_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.users_toolButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("group-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.users_toolButton.setIcon(icon3)
        self.users_toolButton.setIconSize(QtCore.QSize(30, 30))
        self.users_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.users_toolButton.setObjectName("users_toolButton")
        self.language_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.language_toolButton.setGeometry(QtCore.QRect(0, 540, 80, 71))
        self.language_toolButton.setMinimumSize(QtCore.QSize(80, 0))
        self.language_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.language_toolButton.setFont(font)
        self.language_toolButton.setStyleSheet("font-size:15px;\n"
"background-repeat:no-repeat;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/logo/geography-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.language_toolButton.setIcon(icon4)
        self.language_toolButton.setIconSize(QtCore.QSize(30, 30))
        self.language_toolButton.setCheckable(False)
        self.language_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.language_toolButton.setObjectName("language_toolButton")
        self.logo_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.logo_toolButton.setGeometry(QtCore.QRect(0, 10, 80, 71))
        self.logo_toolButton.setMinimumSize(QtCore.QSize(80, 0))
        self.logo_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.logo_toolButton.setFont(font)
        self.logo_toolButton.setStyleSheet("background-color:white;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/logo/surveilialogo.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logo_toolButton.setIcon(icon5)
        self.logo_toolButton.setIconSize(QtCore.QSize(90, 90))
        self.logo_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.logo_toolButton.setObjectName("logo_toolButton")
        self.alarm_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.alarm_toolButton.setGeometry(QtCore.QRect(0, 190, 80, 71))
        self.alarm_toolButton.setMinimumSize(QtCore.QSize(80, 0))
        self.alarm_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.alarm_toolButton.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("alarm-clock-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alarm_toolButton.setIcon(icon6)
        self.alarm_toolButton.setIconSize(QtCore.QSize(30, 30))
        self.alarm_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.alarm_toolButton.setObjectName("alarm_toolButton")
        self.account_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.account_toolButton.setGeometry(QtCore.QRect(0, 360, 80, 71))
        self.account_toolButton.setMinimumSize(QtCore.QSize(80, 0))
        self.account_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.account_toolButton.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("contacts-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_toolButton.setIcon(icon7)
        self.account_toolButton.setIconSize(QtCore.QSize(30, 30))
        self.account_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.account_toolButton.setObjectName("account_toolButton")
        self.camera_toolButton.raise_()
        self.storage_toolButton.raise_()
        self.users_toolButton.raise_()
        self.logout_toolButton.raise_()
        self.language_toolButton.raise_()
        self.logo_toolButton.raise_()
        self.alarm_toolButton.raise_()
        self.account_toolButton.raise_()
        self.horizontalLayout_5.addWidget(self.menuBar)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titleBar2 = QtWidgets.QWidget(self.main_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleBar2.sizePolicy().hasHeightForWidth())
        self.titleBar2.setSizePolicy(sizePolicy)
        self.titleBar2.setMinimumSize(QtCore.QSize(0, 80))
        self.titleBar2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.titleBar2.setStyleSheet("background: #1C1D25;\n"
"font-size: 24px;")
        self.titleBar2.setObjectName("titleBar2")
        self.title_label = QtWidgets.QLabel(self.titleBar2)
        self.title_label.setGeometry(QtCore.QRect(50, 20, 171, 41))
        self.title_label.setObjectName("title_label")
        self.verticalLayout_2.addWidget(self.titleBar2)
        self.menuStackedWidget = QtWidgets.QStackedWidget(self.main_page)
        self.menuStackedWidget.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"background: #2A2F3C ;\n"
"}\n"
"QLineEdit, QTextEdit{\n"
"background-color:#1C1D25;\n"
"border:#1C1D25;\n"
"color:white;\n"
"font-size:18px;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"font-size: 20px;\n"
"\n"
"}\n"
"QPushButton, QToolButton{\n"
"font-weight:bold;\n"
"color:white ;\n"
"background:#1C1D25;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"")
        self.menuStackedWidget.setObjectName("menuStackedWidget")
        self.welcome_page = QtWidgets.QWidget()
        self.welcome_page.setStyleSheet("BACKGROUND-COLOR:#2C313F;")
        self.welcome_page.setObjectName("welcome_page")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.welcome_page)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem2)
        self.frame_3 = QtWidgets.QFrame(self.welcome_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QtCore.QSize(470, 500))
        self.frame_3.setStyleSheet("QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.logo2_toolButton_2 = QtWidgets.QToolButton(self.frame_3)
        self.logo2_toolButton_2.setGeometry(QtCore.QRect(120, 50, 120, 120))
        self.logo2_toolButton_2.setStyleSheet("BACKGROUND-COLOR:WHITE;")
        self.logo2_toolButton_2.setText("")
        self.logo2_toolButton_2.setObjectName("logo2_toolButton_2")
        self.logo2_label_2 = QtWidgets.QLabel(self.frame_3)
        self.logo2_label_2.setGeometry(QtCore.QRect(110, 60, 150, 100))
        self.logo2_label_2.setStyleSheet("background: transparent;")
        self.logo2_label_2.setText("")
        self.logo2_label_2.setPixmap(QtGui.QPixmap(":/logo/surveilialogo.PNG"))
        self.logo2_label_2.setScaledContents(True)
        self.logo2_label_2.setObjectName("logo2_label_2")
        self.welcome_label = QtWidgets.QLabel(self.frame_3)
        self.welcome_label.setGeometry(QtCore.QRect(30, 210, 321, 31))
        self.welcome_label.setStyleSheet("font-size:28px;")
        self.welcome_label.setObjectName("welcome_label")
        self.getStarted_pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.getStarted_pushButton_2.setGeometry(QtCore.QRect(60, 357, 251, 41))
        self.getStarted_pushButton_2.setStyleSheet("background-color:#1C1D25;\n"
"")
        self.getStarted_pushButton_2.setObjectName("getStarted_pushButton_2")
        self.horizontalLayout_18.addWidget(self.frame_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem3)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_18)
        self.menuStackedWidget.addWidget(self.welcome_page)
        self.camera_page = QtWidgets.QWidget()
        self.camera_page.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"background: #2A2F3C ;\n"
"}\n"
"QLineEdit, QTextEdit{\n"
"background-color:#1C1D25;\n"
"background-color:#1C1D25;\n"
"color:white;\n"
"font-size:18px;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"font-size: 18px;\n"
"\n"
"}\n"
"QPushButton, QToolButton{\n"
"font-weight:bold;\n"
"color:white ;\n"
"background-color:#1C1D25;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"")
        self.camera_page.setObjectName("camera_page")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.camera_page)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.display_4 = QtWidgets.QLabel(self.camera_page)
        self.display_4.setStyleSheet("background-color:black;")
        self.display_4.setText("")
        self.display_4.setObjectName("display_4")
        self.horizontalLayout_19.addWidget(self.display_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem4)
        self.display_5 = QtWidgets.QLabel(self.camera_page)
        self.display_5.setStyleSheet("background-color:black;")
        self.display_5.setText("")
        self.display_5.setObjectName("display_5")
        self.horizontalLayout_19.addWidget(self.display_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem5)
        self.display_6 = QtWidgets.QLabel(self.camera_page)
        self.display_6.setStyleSheet("background-color:black;")
        self.display_6.setText("")
        self.display_6.setObjectName("display_6")
        self.horizontalLayout_19.addWidget(self.display_6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_19)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem6)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.display_1 = QtWidgets.QLabel(self.camera_page)
        self.display_1.setStyleSheet("background-color:black;")
        self.display_1.setText("")
        self.display_1.setObjectName("display_1")
        self.horizontalLayout_12.addWidget(self.display_1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.display_2 = QtWidgets.QLabel(self.camera_page)
        self.display_2.setStyleSheet("background-color:black;")
        self.display_2.setText("")
        self.display_2.setObjectName("display_2")
        self.horizontalLayout_12.addWidget(self.display_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem8)
        self.display_3 = QtWidgets.QLabel(self.camera_page)
        self.display_3.setStyleSheet("background-color:black;")
        self.display_3.setText("")
        self.display_3.setObjectName("display_3")
        self.horizontalLayout_12.addWidget(self.display_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_20.addLayout(self.verticalLayout_8)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem9)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem10 = QtWidgets.QSpacerItem(20, 29, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem10)
        self.widget = QtWidgets.QWidget(self.camera_page)
        self.widget.setMinimumSize(QtCore.QSize(200, 500))
        self.widget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget.setObjectName("widget")
        self.cameras_label = QtWidgets.QLabel(self.widget)
        self.cameras_label.setGeometry(QtCore.QRect(50, 10, 121, 41))
        self.cameras_label.setObjectName("cameras_label")
        self.cam01_pushButton = QtWidgets.QPushButton(self.widget)
        self.cam01_pushButton.setGeometry(QtCore.QRect(20, 60, 158, 31))
        self.cam01_pushButton.setObjectName("cam01_pushButton")
        self.cam03_pushButton = QtWidgets.QPushButton(self.widget)
        self.cam03_pushButton.setGeometry(QtCore.QRect(20, 160, 158, 31))
        self.cam03_pushButton.setObjectName("cam03_pushButton")
        self.cam02_pushButton = QtWidgets.QPushButton(self.widget)
        self.cam02_pushButton.setGeometry(QtCore.QRect(20, 110, 158, 31))
        self.cam02_pushButton.setObjectName("cam02_pushButton")
        self.cam04_pushButton = QtWidgets.QPushButton(self.widget)
        self.cam04_pushButton.setGeometry(QtCore.QRect(20, 210, 158, 31))
        self.cam04_pushButton.setObjectName("cam04_pushButton")
        self.cam05_pushButton = QtWidgets.QPushButton(self.widget)
        self.cam05_pushButton.setGeometry(QtCore.QRect(20, 260, 158, 31))
        self.cam05_pushButton.setObjectName("cam05_pushButton")
        self.cam06_pushButton = QtWidgets.QPushButton(self.widget)
        self.cam06_pushButton.setGeometry(QtCore.QRect(20, 310, 158, 31))
        self.cam06_pushButton.setObjectName("cam06_pushButton")
        self.addNew_pushButton = QtWidgets.QPushButton(self.widget)
        self.addNew_pushButton.setGeometry(QtCore.QRect(20, 400, 171, 31))
        self.addNew_pushButton.setObjectName("addNew_pushButton")
        self.showAll_pushButton = QtWidgets.QPushButton(self.widget)
        self.showAll_pushButton.setGeometry(QtCore.QRect(20, 440, 171, 31))
        self.showAll_pushButton.setObjectName("showAll_pushButton")
        self.verticalLayout_6.addWidget(self.widget)
        self.horizontalLayout_20.addLayout(self.verticalLayout_6)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem11)
        self.menuStackedWidget.addWidget(self.camera_page)
        self.alarm_page = QtWidgets.QWidget()
        self.alarm_page.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"background: #2A2F3C ;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"font-size: 18px;\n"
"}\n"
"QTableWidget{ \n"
"  width: 100%;\n"
"   padding: 10px;\n"
"  text-align: left;\n"
"color: white;\n"
" gridline-color: black;\n"
"    font-size: 14px;\n"
"}\n"
"QHeaderView::section {\n"
"background: #2A2F3C ;\n"
"color:white;\n"
"    \n"
"    padding: 2px;\n"
"    border: 1px solid black;\n"
"    font-size: 12px;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #646464;\n"
"    border: 1px solid black;\n"
"}")
        self.alarm_page.setObjectName("alarm_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.alarm_page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem12 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem12)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem13)
        self.alarmHistory_label = QtWidgets.QLabel(self.alarm_page)
        self.alarmHistory_label.setStyleSheet("FONT-WEIGHT:BOLD;\n"
"font-size:24px")
        self.alarmHistory_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.alarmHistory_label.setObjectName("alarmHistory_label")
        self.horizontalLayout_24.addWidget(self.alarmHistory_label)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem14)
        self.verticalLayout_3.addLayout(self.horizontalLayout_24)
        spacerItem15 = QtWidgets.QSpacerItem(1, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem15)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem16)
        self.alarm_tableWidget = QtWidgets.QTableWidget(self.alarm_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alarm_tableWidget.sizePolicy().hasHeightForWidth())
        self.alarm_tableWidget.setSizePolicy(sizePolicy)
        self.alarm_tableWidget.setMinimumSize(QtCore.QSize(800, 0))
        self.alarm_tableWidget.setStyleSheet("QTableWidget{ \n"
"  width: 100%;\n"
"   padding: 10px;\n"
"  text-align: left;\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"color:white;\n"
"    background-color:#1C1D25;\n"
"\n"
"    padding: 2px;\n"
"    border: 1px solid black;\n"
"    font-size: 15px;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: black;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #2A2F3C\n"
"    border: 1px solid black;\n"
"}")
        self.alarm_tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.alarm_tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.alarm_tableWidget.setObjectName("alarm_tableWidget")
        self.alarm_tableWidget.setColumnCount(4)
        self.alarm_tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.alarm_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.alarm_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.alarm_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.alarm_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.alarm_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.alarm_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.alarm_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.alarm_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.alarm_tableWidget.setHorizontalHeaderItem(3, item)
        self.alarm_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.alarm_tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.alarm_tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.alarm_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.alarm_tableWidget.verticalHeader().setVisible(False)
        self.alarm_tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.horizontalLayout_6.addWidget(self.alarm_tableWidget)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem17)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.menuStackedWidget.addWidget(self.alarm_page)
        self.storage_page = QtWidgets.QWidget()
        self.storage_page.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"background: #2A2F3C ;\n"
"}\n"
"QLineEdit, QTextEdit{\n"
"background: #201f1f;\n"
"border:#201f1f;\n"
"color:white;\n"
"font-size:18px;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"font-size: 18px;\n"
"\n"
"}\n"
"QPushButton, QToolButton{\n"
"font-weight:bold;\n"
"color:white ;\n"
"background: #2A2F3C ;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"")
        self.storage_page.setObjectName("storage_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.storage_page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem18 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem18)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem19)
        self.storage_label = QtWidgets.QLabel(self.storage_page)
        self.storage_label.setStyleSheet("FONT-WEIGHT:BOLD;\n"
"font-size:24px")
        self.storage_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.storage_label.setObjectName("storage_label")
        self.horizontalLayout_9.addWidget(self.storage_label)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem20)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        spacerItem21 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem21)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.show_label = QtWidgets.QLabel(self.storage_page)
        self.show_label.setObjectName("show_label")
        self.horizontalLayout_8.addWidget(self.show_label)
        spacerItem22 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem22)
        self.anomalyClip_checkBox = QtWidgets.QCheckBox(self.storage_page)
        self.anomalyClip_checkBox.setStyleSheet("\n"
"font-size:16px;\n"
"color:white;")
        self.anomalyClip_checkBox.setObjectName("anomalyClip_checkBox")
        self.horizontalLayout_8.addWidget(self.anomalyClip_checkBox)
        self.cameraFeed_checkBox = QtWidgets.QCheckBox(self.storage_page)
        self.cameraFeed_checkBox.setStyleSheet("\n"
"font-size:16px;\n"
"color:white;")
        self.cameraFeed_checkBox.setIconSize(QtCore.QSize(30, 30))
        self.cameraFeed_checkBox.setChecked(False)
        self.cameraFeed_checkBox.setAutoRepeat(False)
        self.cameraFeed_checkBox.setAutoExclusive(False)
        self.cameraFeed_checkBox.setTristate(False)
        self.cameraFeed_checkBox.setObjectName("cameraFeed_checkBox")
        self.horizontalLayout_8.addWidget(self.cameraFeed_checkBox)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem23)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem24)
        self.storage_tableWidget = QtWidgets.QTableWidget(self.storage_page)
        self.storage_tableWidget.setMinimumSize(QtCore.QSize(700, 0))
        self.storage_tableWidget.setStyleSheet("QTableWidget{ \n"
"  width: 100%;\n"
"   padding: 10px;\n"
"  text-align: left;\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"color:white;\n"
"    background-color:#1C1D25;\n"
"\n"
"    padding: 2px;\n"
"    border: 1px solid black;\n"
"    font-size: 12px;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: black;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #2A2F3C\n"
"    border: 1px solid black;\n"
"}")
        self.storage_tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.storage_tableWidget.setObjectName("storage_tableWidget")
        self.storage_tableWidget.setColumnCount(3)
        self.storage_tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.storage_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.storage_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.storage_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.storage_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.storage_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.storage_tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.storage_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.storage_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.storage_tableWidget.setHorizontalHeaderItem(2, item)
        self.storage_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.storage_tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.storage_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.storage_tableWidget.verticalHeader().setVisible(False)
        self.storage_tableWidget.verticalHeader().setHighlightSections(False)
        self.horizontalLayout_7.addWidget(self.storage_tableWidget)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem25)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.menuStackedWidget.addWidget(self.storage_page)
        self.accountInfo_page = QtWidgets.QWidget()
        self.accountInfo_page.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"background: #2A2F3C ;\n"
"}\n"
"QLineEdit, QTextEdit{\n"
"background-color:#1C1D25;\n"
"background-color:#1C1D25;\n"
"color:white;\n"
"font-size:18px;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"font-size: 18px;\n"
"\n"
"}\n"
"QPushButton, QToolButton{\n"
"font-weight:bold;\n"
"color:white ;\n"
"background-color:#1C1D25;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"")
        self.accountInfo_page.setObjectName("accountInfo_page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.accountInfo_page)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem26 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem26)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem27)
        self.account_form = QtWidgets.QFormLayout()
        self.account_form.setObjectName("account_form")
        self.accountInfo_label = QtWidgets.QLabel(self.accountInfo_page)
        self.accountInfo_label.setStyleSheet("FONT-WEIGHT:BOLD;\n"
"font-size:24px;")
        self.accountInfo_label.setObjectName("accountInfo_label")
        self.account_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.accountInfo_label)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.account_form.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem28)
        self.username_label = QtWidgets.QLabel(self.accountInfo_page)
        self.username_label.setObjectName("username_label")
        self.account_form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.username_label)
        self.username_lineEdit = QtWidgets.QLineEdit(self.accountInfo_page)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.account_form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.username_lineEdit)
        self.password_label = QtWidgets.QLabel(self.accountInfo_page)
        self.password_label.setObjectName("password_label")
        self.account_form.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.password_label)
        self.password_lineEdit = QtWidgets.QLineEdit(self.accountInfo_page)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.account_form.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.password_lineEdit)
        self.contactInfo_label = QtWidgets.QLabel(self.accountInfo_page)
        self.contactInfo_label.setObjectName("contactInfo_label")
        self.account_form.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.contactInfo_label)
        self.contactInfo_lineEdit = QtWidgets.QLineEdit(self.accountInfo_page)
        self.contactInfo_lineEdit.setObjectName("contactInfo_lineEdit")
        self.account_form.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.contactInfo_lineEdit)
        self.address_label = QtWidgets.QLabel(self.accountInfo_page)
        self.address_label.setObjectName("address_label")
        self.account_form.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.address_label)
        self.address_lineEdit = QtWidgets.QTextEdit(self.accountInfo_page)
        self.address_lineEdit.setStyleSheet("border-radius: 0px;")
        self.address_lineEdit.setObjectName("address_lineEdit")
        self.account_form.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.address_lineEdit)
        spacerItem29 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.account_form.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem29)
        self.edit_pushButton = QtWidgets.QPushButton(self.accountInfo_page)
        self.edit_pushButton.setStyleSheet("FONT-SIZE: 18PX;")
        self.edit_pushButton.setObjectName("edit_pushButton")
        self.account_form.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.edit_pushButton)
        self.horizontalLayout_10.addLayout(self.account_form)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem30)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.menuStackedWidget.addWidget(self.accountInfo_page)
        self.usersInfo_page = QtWidgets.QWidget()
        self.usersInfo_page.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"background: #2A2F3C ;\n"
"}\n"
"QLineEdit, QTextEdit{\n"
"background-color:#1C1D25;\n"
"background-color:#1C1D25;\n"
"color:white;\n"
"font-size:18px;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"font-size: 18px;\n"
"\n"
"}\n"
"QPushButton, QToolButton{\n"
"font-weight:bold;\n"
"color:white ;\n"
"background-color:#1C1D25;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"")
        self.usersInfo_page.setObjectName("usersInfo_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.usersInfo_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem31 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem31)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem32)
        self.userInfo_label = QtWidgets.QLabel(self.usersInfo_page)
        self.userInfo_label.setStyleSheet("FONT-WEIGHT:BOLD;\n"
"font-size:24px;FONT-WEIGHT:BOLD;")
        self.userInfo_label.setObjectName("userInfo_label")
        self.horizontalLayout_16.addWidget(self.userInfo_label)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem33)
        self.verticalLayout_5.addLayout(self.horizontalLayout_16)
        spacerItem34 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem34)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem35 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem35)
        self.userAdd_pushButton = QtWidgets.QPushButton(self.usersInfo_page)
        self.userAdd_pushButton.setObjectName("userAdd_pushButton")
        self.horizontalLayout_15.addWidget(self.userAdd_pushButton)
        self.userDelete_pushButton = QtWidgets.QPushButton(self.usersInfo_page)
        self.userDelete_pushButton.setObjectName("userDelete_pushButton")
        self.horizontalLayout_15.addWidget(self.userDelete_pushButton)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem36)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem37)
        self.user_tableWidget = QtWidgets.QTableWidget(self.usersInfo_page)
        self.user_tableWidget.setMinimumSize(QtCore.QSize(800, 0))
        self.user_tableWidget.setStyleSheet("QTableWidget{ \n"
"  width: 100%;\n"
"   padding: 10px;\n"
"  text-align: left;\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"color:white;\n"
"    background-color:#1C1D25;\n"
"    padding: 2px;\n"
"    border: 1px solid black;\n"
"    font-size: 12px;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: black;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color:#1C1D25;\n"
"    border: 1px solid black;\n"
"}")
        self.user_tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.user_tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.user_tableWidget.setObjectName("user_tableWidget")
        self.user_tableWidget.setColumnCount(4)
        self.user_tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.user_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_tableWidget.setHorizontalHeaderItem(3, item)
        self.user_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.user_tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.user_tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.user_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.user_tableWidget.verticalHeader().setVisible(False)
        self.horizontalLayout_13.addWidget(self.user_tableWidget)
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem38)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.menuStackedWidget.addWidget(self.usersInfo_page)
        self.addNewUser_page = QtWidgets.QWidget()
        self.addNewUser_page.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"background: #2A2F3C ;\n"
"}\n"
"QLineEdit, QTextEdit{\n"
"background-color:#1C1D25;\n"
"border:#1C1D25;\n"
"\n"
"color:white;\n"
"font-size:18px;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"font-size: 18px;\n"
"\n"
"}\n"
"QPushButton, QToolButton{\n"
"font-weight:bold;\n"
"color:white ;\n"
"background-color:#1C1D25;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"")
        self.addNewUser_page.setObjectName("addNewUser_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.addNewUser_page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem39 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem39)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem40)
        self.addUser_form = QtWidgets.QFormLayout()
        self.addUser_form.setObjectName("addUser_form")
        self.addUser_label = QtWidgets.QLabel(self.addNewUser_page)
        self.addUser_label.setStyleSheet("FONT-WEIGHT:BOLD;\n"
"font-size:24px;")
        self.addUser_label.setObjectName("addUser_label")
        self.addUser_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.addUser_label)
        spacerItem41 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.addUser_form.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem41)
        self.aUsername_label = QtWidgets.QLabel(self.addNewUser_page)
        self.aUsername_label.setObjectName("aUsername_label")
        self.addUser_form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.aUsername_label)
        self.aUsername_lineEdit = QtWidgets.QLineEdit(self.addNewUser_page)
        self.aUsername_lineEdit.setText("")
        self.aUsername_lineEdit.setObjectName("aUsername_lineEdit")
        self.addUser_form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.aUsername_lineEdit)
        self.aPassword_label = QtWidgets.QLabel(self.addNewUser_page)
        self.aPassword_label.setObjectName("aPassword_label")
        self.addUser_form.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.aPassword_label)
        self.aPassword_lineEdit = QtWidgets.QLineEdit(self.addNewUser_page)
        self.aPassword_lineEdit.setText("")
        self.aPassword_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.aPassword_lineEdit.setObjectName("aPassword_lineEdit")
        self.addUser_form.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.aPassword_lineEdit)
        self.aContactInfo_label = QtWidgets.QLabel(self.addNewUser_page)
        self.aContactInfo_label.setObjectName("aContactInfo_label")
        self.addUser_form.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.aContactInfo_label)
        self.aContactInfo_lineEdit = QtWidgets.QLineEdit(self.addNewUser_page)
        self.aContactInfo_lineEdit.setText("")
        self.aContactInfo_lineEdit.setObjectName("aContactInfo_lineEdit")
        self.addUser_form.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.aContactInfo_lineEdit)
        self.aAddress_label = QtWidgets.QLabel(self.addNewUser_page)
        self.aAddress_label.setObjectName("aAddress_label")
        self.addUser_form.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.aAddress_label)
        self.aAddress_lineEdit = QtWidgets.QTextEdit(self.addNewUser_page)
        self.aAddress_lineEdit.setStyleSheet("border-radius:0px;")
        self.aAddress_lineEdit.setObjectName("aAddress_lineEdit")
        self.addUser_form.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.aAddress_lineEdit)
        spacerItem42 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.addUser_form.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem42)
        self.aEdit_pushButton = QtWidgets.QPushButton(self.addNewUser_page)
        self.aEdit_pushButton.setStyleSheet("FONT-SIZE: 18PX;")
        self.aEdit_pushButton.setObjectName("aEdit_pushButton")
        self.addUser_form.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.aEdit_pushButton)
        self.horizontalLayout_11.addLayout(self.addUser_form)
        spacerItem43 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem43)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.menuStackedWidget.addWidget(self.addNewUser_page)
        self.dialog_page = QtWidgets.QWidget()
        self.dialog_page.setObjectName("dialog_page")
        self.frame = QtWidgets.QFrame(self.dialog_page)
        self.frame.setGeometry(QtCore.QRect(180, 110, 601, 451))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label)
        self.addIPCam_field = QtWidgets.QLineEdit(self.frame)
        self.addIPCam_field.setObjectName("addIPCam_field")
        self.verticalLayout_9.addWidget(self.addIPCam_field)
        self.addIPCam_pushButton = QtWidgets.QPushButton(self.frame)
        self.addIPCam_pushButton.setObjectName("addIPCam_pushButton")
        self.verticalLayout_9.addWidget(self.addIPCam_pushButton)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2)
        self.openDir_pushButton = QtWidgets.QPushButton(self.frame)
        self.openDir_pushButton.setObjectName("openDir_pushButton")
        self.verticalLayout_9.addWidget(self.openDir_pushButton)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3)
        self.openWebcam_pushButton = QtWidgets.QPushButton(self.frame)
        self.openWebcam_pushButton.setObjectName("openWebcam_pushButton")
        self.verticalLayout_9.addWidget(self.openWebcam_pushButton)
        self.cancel_PushButton = QtWidgets.QPushButton(self.frame)
        self.cancel_PushButton.setObjectName("cancel_PushButton")
        self.verticalLayout_9.addWidget(self.cancel_PushButton)
        self.menuStackedWidget.addWidget(self.dialog_page)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.english_radioButton = QtWidgets.QRadioButton(self.page)
        self.english_radioButton.setGeometry(QtCore.QRect(230, 170, 141, 31))
        self.english_radioButton.setStyleSheet("font-size:21px;\n"
"COLOR:WHITE;")
        self.english_radioButton.setObjectName("english_radioButton")
        self.chooseLanguage_label = QtWidgets.QLabel(self.page)
        self.chooseLanguage_label.setGeometry(QtCore.QRect(100, 100, 191, 31))
        self.chooseLanguage_label.setObjectName("chooseLanguage_label")
        self.urdu_radioButton = QtWidgets.QRadioButton(self.page)
        self.urdu_radioButton.setGeometry(QtCore.QRect(230, 220, 111, 31))
        self.urdu_radioButton.setStyleSheet("font-size:21px;\n"
"COLOR:WHITE;")
        self.urdu_radioButton.setObjectName("urdu_radioButton")
        self.menuStackedWidget.addWidget(self.page)
        self.verticalLayout_2.addWidget(self.menuStackedWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.mainStackedWidget.addWidget(self.main_page)
        self.loggedOut_page = QtWidgets.QWidget()
        self.loggedOut_page.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"font-size: 30px;\n"
"background-color:#1C1D25;\n"
"}\n"
"QFrame{\n"
"\n"
"background: #2A2F3C ;\n"
"border-radius:10px;\n"
"\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"font-weight: bold;\n"
"}\n"
"QToolButton{\n"
"background:white;\n"
"border-radius:60px;\n"
"}\n"
"QLineEdit{\n"
"background: transparent;\n"
"border:none;\n"
"color:BLACK;\n"
"border-bottom:1px solid black;\n"
"font-size:20px;\n"
"}\n"
"QPushButton{\n"
"font-size:18px;\n"
"font-weight:bold;\n"
"color:white ;\n"
"background-color:#1C1D25;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"#logoLabel{\n"
"background:transparent;\n"
"}")
        self.loggedOut_page.setObjectName("loggedOut_page")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.loggedOut_page)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        spacerItem44 = QtWidgets.QSpacerItem(240, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem44)
        self.loggedOut_widget = QtWidgets.QWidget(self.loggedOut_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loggedOut_widget.sizePolicy().hasHeightForWidth())
        self.loggedOut_widget.setSizePolicy(sizePolicy)
        self.loggedOut_widget.setMinimumSize(QtCore.QSize(560, 600))
        self.loggedOut_widget.setObjectName("loggedOut_widget")
        self.logo3_label = QtWidgets.QLabel(self.loggedOut_widget)
        self.logo3_label.setGeometry(QtCore.QRect(200, 80, 150, 100))
        self.logo3_label.setStyleSheet("background: transparent;")
        self.logo3_label.setText("")
        self.logo3_label.setPixmap(QtGui.QPixmap(":/logo/surveilialogo.PNG"))
        self.logo3_label.setScaledContents(True)
        self.logo3_label.setObjectName("logo3_label")
        self.loggedOut_frame = QtWidgets.QFrame(self.loggedOut_widget)
        self.loggedOut_frame.setGeometry(QtCore.QRect(70, 130, 411, 571))
        self.loggedOut_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loggedOut_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loggedOut_frame.setObjectName("loggedOut_frame")
        self.title3_label = QtWidgets.QLabel(self.loggedOut_frame)
        self.title3_label.setGeometry(QtCore.QRect(110, 110, 231, 61))
        self.title3_label.setStyleSheet("font-size:35px;")
        self.title3_label.setObjectName("title3_label")
        self.cancel_pushButton_3 = QtWidgets.QPushButton(self.loggedOut_frame)
        self.cancel_pushButton_3.setGeometry(QtCore.QRect(100, 420, 211, 40))
        self.cancel_pushButton_3.setObjectName("cancel_pushButton_3")
        self.loginAgain_pushButton_3 = QtWidgets.QPushButton(self.loggedOut_frame)
        self.loginAgain_pushButton_3.setGeometry(QtCore.QRect(100, 350, 211, 40))
        self.loginAgain_pushButton_3.setObjectName("loginAgain_pushButton_3")
        self.loggedOut_label_3 = QtWidgets.QLabel(self.loggedOut_frame)
        self.loggedOut_label_3.setGeometry(QtCore.QRect(80, 230, 281, 51))
        self.loggedOut_label_3.setStyleSheet("font-size:18px;")
        self.loggedOut_label_3.setObjectName("loggedOut_label_3")
        self.logo3_toolButton = QtWidgets.QToolButton(self.loggedOut_widget)
        self.logo3_toolButton.setGeometry(QtCore.QRect(210, 70, 120, 120))
        self.logo3_toolButton.setText("")
        self.logo3_toolButton.setObjectName("logo3_toolButton")
        self.loggedOut_frame.raise_()
        self.logo3_toolButton.raise_()
        self.logo3_label.raise_()
        self.horizontalLayout_27.addWidget(self.loggedOut_widget)
        spacerItem45 = QtWidgets.QSpacerItem(240, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem45)
        self.mainStackedWidget.addWidget(self.loggedOut_page)
        self.horizontalLayout_4.addWidget(self.mainStackedWidget)
        surveiliaFrontEnd.setCentralWidget(self.centralwidget)

        self.retranslateUi(surveiliaFrontEnd)
        self.mainStackedWidget.setCurrentIndex(1)
        self.menuStackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(surveiliaFrontEnd)

    def retranslateUi(self, surveiliaFrontEnd):
        _translate = QtCore.QCoreApplication.translate
        surveiliaFrontEnd.setWindowTitle(_translate("surveiliaFrontEnd", "MainWindow"))
        self.title1_label.setText(_translate("surveiliaFrontEnd", "SURVEILIA"))
        self.username1_field.setPlaceholderText(_translate("surveiliaFrontEnd", "Username"))
        self.password1_field.setPlaceholderText(_translate("surveiliaFrontEnd", "Password"))
        self.login1_pushButton.setText(_translate("surveiliaFrontEnd", "LOGIN"))
        self.admin1_radioButton.setText(_translate("surveiliaFrontEnd", "Admin"))
        self.user1_radioButton.setText(_translate("surveiliaFrontEnd", "User"))
        self.loginas1_label.setText(_translate("surveiliaFrontEnd", "Login as:"))
        self.camera_toolButton.setText(_translate("surveiliaFrontEnd", "Camera"))
        self.storage_toolButton.setText(_translate("surveiliaFrontEnd", "Storage"))
        self.logout_toolButton.setText(_translate("surveiliaFrontEnd", "Logout"))
        self.users_toolButton.setText(_translate("surveiliaFrontEnd", "Users"))
        self.language_toolButton.setText(_translate("surveiliaFrontEnd", "Language"))
        self.logo_toolButton.setText(_translate("surveiliaFrontEnd", "Logout"))
        self.alarm_toolButton.setText(_translate("surveiliaFrontEnd", "Alarm Log"))
        self.account_toolButton.setText(_translate("surveiliaFrontEnd", "Account"))
        self.title_label.setText(_translate("surveiliaFrontEnd", "SURVEILIA"))
        self.welcome_label.setText(_translate("surveiliaFrontEnd", "Welcome to SURVEILIA"))
        self.getStarted_pushButton_2.setText(_translate("surveiliaFrontEnd", "GET STARTED"))
        self.cameras_label.setText(_translate("surveiliaFrontEnd", "CAMERAS"))
        self.cam01_pushButton.setText(_translate("surveiliaFrontEnd", "CAMERA_01"))
        self.cam03_pushButton.setText(_translate("surveiliaFrontEnd", "CAMERA_03"))
        self.cam02_pushButton.setText(_translate("surveiliaFrontEnd", "CAMERA_02"))
        self.cam04_pushButton.setText(_translate("surveiliaFrontEnd", "CAMERA_04"))
        self.cam05_pushButton.setText(_translate("surveiliaFrontEnd", "CAMERA_05"))
        self.cam06_pushButton.setText(_translate("surveiliaFrontEnd", "CAMERA_06"))
        self.addNew_pushButton.setText(_translate("surveiliaFrontEnd", "ADD NEW"))
        self.showAll_pushButton.setText(_translate("surveiliaFrontEnd", "SHOW ALL"))
        self.alarmHistory_label.setText(_translate("surveiliaFrontEnd", "ALARM HISTORY"))
        self.alarm_tableWidget.setSortingEnabled(True)
        item = self.alarm_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("surveiliaFrontEnd", "1"))
        item = self.alarm_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("surveiliaFrontEnd", "2"))
        item = self.alarm_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("surveiliaFrontEnd", "3"))
        item = self.alarm_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("surveiliaFrontEnd", "4"))
        item = self.alarm_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("surveiliaFrontEnd", "5"))
        item = self.alarm_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("surveiliaFrontEnd", "Camera ID"))
        item = self.alarm_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("surveiliaFrontEnd", "Event"))
        item = self.alarm_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("surveiliaFrontEnd", "Date"))
        item = self.alarm_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("surveiliaFrontEnd", "Time"))
        self.storage_label.setText(_translate("surveiliaFrontEnd", "STORAGE"))
        self.show_label.setText(_translate("surveiliaFrontEnd", "           Show:"))
        self.anomalyClip_checkBox.setText(_translate("surveiliaFrontEnd", "Anomaly Clip"))
        self.cameraFeed_checkBox.setText(_translate("surveiliaFrontEnd", "Camera Feed"))
        item = self.storage_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("surveiliaFrontEnd", "1"))
        item = self.storage_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("surveiliaFrontEnd", "2"))
        item = self.storage_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("surveiliaFrontEnd", "3"))
        item = self.storage_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("surveiliaFrontEnd", "4"))
        item = self.storage_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("surveiliaFrontEnd", "5"))
        item = self.storage_tableWidget.verticalHeaderItem(5)
        item.setText(_translate("surveiliaFrontEnd", "6"))
        item = self.storage_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("surveiliaFrontEnd", "Filename"))
        item = self.storage_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("surveiliaFrontEnd", "Date"))
        item = self.storage_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("surveiliaFrontEnd", "Size"))
        self.accountInfo_label.setText(_translate("surveiliaFrontEnd", "ACCOUNT INFORMATION"))
        self.username_label.setText(_translate("surveiliaFrontEnd", "Username:"))
        self.username_lineEdit.setText(_translate("surveiliaFrontEnd", "Ifrah Tehleel"))
        self.password_label.setText(_translate("surveiliaFrontEnd", "Password:"))
        self.password_lineEdit.setText(_translate("surveiliaFrontEnd", "Ifrah"))
        self.contactInfo_label.setText(_translate("surveiliaFrontEnd", "Contact Info:"))
        self.contactInfo_lineEdit.setText(_translate("surveiliaFrontEnd", "+923014474797"))
        self.address_label.setText(_translate("surveiliaFrontEnd", "Address:"))
        self.address_lineEdit.setHtml(_translate("surveiliaFrontEnd", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'century gothic\'; font-size:18px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.21053pt;\">49-A , Wapda Town, Lahore</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.21053pt;\"><br /></p></body></html>"))
        self.edit_pushButton.setText(_translate("surveiliaFrontEnd", "EDIT"))
        self.userInfo_label.setText(_translate("surveiliaFrontEnd", "  USERS INFORMATION"))
        self.userAdd_pushButton.setText(_translate("surveiliaFrontEnd", "ADD"))
        self.userDelete_pushButton.setText(_translate("surveiliaFrontEnd", "DELETE"))
        item = self.user_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("surveiliaFrontEnd", "1"))
        item = self.user_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("surveiliaFrontEnd", "2"))
        item = self.user_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("surveiliaFrontEnd", "3"))
        item = self.user_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("surveiliaFrontEnd", "4"))
        item = self.user_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("surveiliaFrontEnd", "5"))
        item = self.user_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("surveiliaFrontEnd", "Name"))
        item = self.user_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("surveiliaFrontEnd", "Password"))
        item = self.user_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("surveiliaFrontEnd", "Contact Info"))
        item = self.user_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("surveiliaFrontEnd", "Address"))
        self.addUser_label.setText(_translate("surveiliaFrontEnd", "ADD NEW USER"))
        self.aUsername_label.setText(_translate("surveiliaFrontEnd", "Username:"))
        self.aPassword_label.setText(_translate("surveiliaFrontEnd", "Password:"))
        self.aContactInfo_label.setText(_translate("surveiliaFrontEnd", "Contact Info:"))
        self.aAddress_label.setText(_translate("surveiliaFrontEnd", "Address:"))
        self.aAddress_lineEdit.setHtml(_translate("surveiliaFrontEnd", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'century gothic\'; font-size:18px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.21053pt;\"><br /></p></body></html>"))
        self.aEdit_pushButton.setText(_translate("surveiliaFrontEnd", "ADD USER"))
        self.label.setText(_translate("surveiliaFrontEnd", "Add camera using IP Address"))
        self.addIPCam_field.setText(_translate("surveiliaFrontEnd", "ENTER IP ADDRESS HERE"))
        self.addIPCam_pushButton.setText(_translate("surveiliaFrontEnd", "ADD"))
        self.label_2.setText(_translate("surveiliaFrontEnd", "Add video by file from Directory"))
        self.openDir_pushButton.setText(_translate("surveiliaFrontEnd", "OPEN"))
        self.label_3.setText(_translate("surveiliaFrontEnd", "Add using Webcam"))
        self.openWebcam_pushButton.setText(_translate("surveiliaFrontEnd", "OPEN WEBCAM"))
        self.cancel_PushButton.setText(_translate("surveiliaFrontEnd", "CANCEL"))
        self.english_radioButton.setText(_translate("surveiliaFrontEnd", "English"))
        self.chooseLanguage_label.setText(_translate("surveiliaFrontEnd", "Choose Language:"))
        self.urdu_radioButton.setText(_translate("surveiliaFrontEnd", "Urdu"))
        self.title3_label.setText(_translate("surveiliaFrontEnd", "SURVEILIA"))
        self.cancel_pushButton_3.setText(_translate("surveiliaFrontEnd", "CANCEL"))
        self.loginAgain_pushButton_3.setText(_translate("surveiliaFrontEnd", "LOGIN AGAIN"))
        self.loggedOut_label_3.setText(_translate("surveiliaFrontEnd", "You have been logged out!"))


import resource01_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    surveiliaFrontEnd = QtWidgets.QMainWindow()
    ui = Ui_surveiliaFrontEnd()
    ui.setupUi(surveiliaFrontEnd)
    surveiliaFrontEnd.show()
    sys.exit(app.exec_())
