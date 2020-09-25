from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_surveiliaFrontEnd(object):
    def setupUi(self, surveiliaFrontEnd):
        surveiliaFrontEnd.setObjectName("surveiliaFrontEnd")
        surveiliaFrontEnd.resize(1100, 800)
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
                                        "background-color:#201f1f;\n"
                                        "}\n"
                                        "QFrame{\n"
                                        "background: #605E5C ;\n"
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
                                        "background:#201f1f;\n"
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
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.mainStackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.mainStackedWidget.setStyleSheet("*{\n"
                                             "font-family: century gothic;\n"
                                             "background-color:#201f1f;\n"
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
                                             "background:#201f1f;\n"
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
                                      "background-color:#201f1f;\n"
                                      "}\n"
                                      "QFrame{\n"
                                      "background: #605E5C ;\n"
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
                                      "background:#201f1f;\n"
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
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Minimum)
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
        self.title1_label.setGeometry(QtCore.QRect(120, 80, 171, 40))
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
                                              "color:#302F2E;\n"
                                              "font-size:16px;\n"
                                              "background:transparent;\n"
                                              "\n"
                                              "\n"
                                              "}")
        self.admin1_radioButton.setObjectName("admin1_radioButton")
        self.user1_radioButton = QtWidgets.QRadioButton(self.loginForm_frame)
        self.user1_radioButton.setGeometry(QtCore.QRect(210, 320, 61, 20))
        self.user1_radioButton.setStyleSheet("QRadioButton{\n"
                                             "color:#302F2E;\n"
                                             "font-size:16px;\n"
                                             "background:transparent;\n"
                                             "\n"
                                             "}")
        self.user1_radioButton.setObjectName("user1_radioButton")
        self.loginas1_label = QtWidgets.QLabel(self.loginForm_frame)
        self.loginas1_label.setGeometry(QtCore.QRect(70, 320, 81, 31))
        self.loginas1_label.setStyleSheet("*{\n"
                                          "background: transparent;\n"
                                          "border:none;\n"
                                          "color:#302F2E;\n"
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
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
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
        self.menuBar.setStyleSheet("*{background: #201f1f;\n"
                                   "font-size: 16px;\n"
                                   "}\n"
                                   "QToolButton:hover{\n"
                                   "     background-color:#3b3a3a;\n"
                                   "}\n"
                                   "QToolButton:pressed{\n"
                                   "     background-color: #605E5C ;     \n"
                                   "}")
        self.menuBar.setObjectName("menuBar")
        self.camera_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.camera_toolButton.setGeometry(QtCore.QRect(0, 10, 80, 71))
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
        self.alarm_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.alarm_toolButton.setGeometry(QtCore.QRect(0, 90, 80, 71))
        self.alarm_toolButton.setMinimumSize(QtCore.QSize(80, 0))
        self.alarm_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.alarm_toolButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("alarm-clock-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alarm_toolButton.setIcon(icon1)
        self.alarm_toolButton.setIconSize(QtCore.QSize(30, 30))
        self.alarm_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.alarm_toolButton.setObjectName("alarm_toolButton")
        self.storage_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.storage_toolButton.setGeometry(QtCore.QRect(0, 170, 80, 71))
        self.storage_toolButton.setMinimumSize(QtCore.QSize(80, 0))
        self.storage_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.storage_toolButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("database-5-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.storage_toolButton.setIcon(icon2)
        self.storage_toolButton.setIconSize(QtCore.QSize(30, 30))
        self.storage_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.storage_toolButton.setObjectName("storage_toolButton")
        self.account_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.account_toolButton.setGeometry(QtCore.QRect(0, 250, 80, 71))
        self.account_toolButton.setMinimumSize(QtCore.QSize(80, 0))
        self.account_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.account_toolButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("contacts-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_toolButton.setIcon(icon3)
        self.account_toolButton.setIconSize(QtCore.QSize(30, 30))
        self.account_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.account_toolButton.setObjectName("account_toolButton")
        self.help_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.help_toolButton.setGeometry(QtCore.QRect(0, 410, 80, 71))
        self.help_toolButton.setMinimumSize(QtCore.QSize(80, 0))
        self.help_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.help_toolButton.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("question-mark-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help_toolButton.setIcon(icon4)
        self.help_toolButton.setIconSize(QtCore.QSize(30, 30))
        self.help_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.help_toolButton.setObjectName("help_toolButton")
        self.logout_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.logout_toolButton.setGeometry(QtCore.QRect(0, 490, 80, 71))
        self.logout_toolButton.setMinimumSize(QtCore.QSize(80, 0))
        self.logout_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.logout_toolButton.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("logout-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_toolButton.setIcon(icon5)
        self.logout_toolButton.setIconSize(QtCore.QSize(30, 30))
        self.logout_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.logout_toolButton.setObjectName("logout_toolButton")
        self.users_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.users_toolButton.setGeometry(QtCore.QRect(0, 330, 80, 71))
        self.users_toolButton.setMinimumSize(QtCore.QSize(80, 0))
        self.users_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.users_toolButton.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("group-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.users_toolButton.setIcon(icon6)
        self.users_toolButton.setIconSize(QtCore.QSize(30, 30))
        self.users_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.users_toolButton.setObjectName("users_toolButton")
        self.camera_toolButton.raise_()
        self.alarm_toolButton.raise_()
        self.storage_toolButton.raise_()
        self.account_toolButton.raise_()
        self.users_toolButton.raise_()
        self.help_toolButton.raise_()
        self.logout_toolButton.raise_()
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
        self.titleBar2.setMinimumSize(QtCore.QSize(0, 70))
        self.titleBar2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.titleBar2.setStyleSheet("background: #201f1f;\n"
                                     "font-size: 24px;")
        self.titleBar2.setObjectName("titleBar2")
        self.title_label = QtWidgets.QLabel(self.titleBar2)
        self.title_label.setGeometry(QtCore.QRect(60, 30, 121, 21))
        self.title_label.setObjectName("title_label")
        self.verticalLayout_2.addWidget(self.titleBar2)
        self.menuStackedWidget = QtWidgets.QStackedWidget(self.main_page)
        self.menuStackedWidget.setStyleSheet("*{background-color:#484644;}\n"
                                             "QLineEdit, QTextEdit {\n"
                                             "background: #201f1f;\n"
                                             "border:#201f1f;\n"
                                             "color:white;\n"
                                             "font-size:18px;\n"
                                             "}\n"
                                             "QLabel{\n"
                                             "color: white;\n"
                                             "font-size: 18px;\n"
                                             "}\n"
                                             "QPushButton{\n"
                                             "\n"
                                             "background:#201f1f;\n"
                                             "}")
        self.menuStackedWidget.setObjectName("menuStackedWidget")
        self.camera_page = QtWidgets.QWidget()
        self.camera_page.setObjectName("camera_page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.camera_page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.video_label = QtWidgets.QLabel(self.camera_page)
        self.video_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.video_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.video_label.setLineWidth(1)
        self.video_label.setMidLineWidth(1)
        self.video_label.setText("")
        self.video_label.setObjectName("video_label")
        self.verticalLayout.addWidget(self.video_label)
        self.camera_pushButton = QtWidgets.QPushButton(self.camera_page)
        self.camera_pushButton.setObjectName("camera_pushButton")
        self.verticalLayout.addWidget(self.camera_pushButton)
        self.menuStackedWidget.addWidget(self.camera_page)
        self.alarm_page = QtWidgets.QWidget()
        self.alarm_page.setObjectName("alarm_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.alarm_page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        spacerItem3 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem3)
        self.alarmHistory_label = QtWidgets.QLabel(self.alarm_page)
        self.alarmHistory_label.setStyleSheet("FONT-WEIGHT:BOLD;\n"
                                              "font-size:24px")
        self.alarmHistory_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.alarmHistory_label.setObjectName("alarmHistory_label")
        self.horizontalLayout_24.addWidget(self.alarmHistory_label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.alarm_tableWidget = QtWidgets.QTableWidget(self.alarm_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alarm_tableWidget.sizePolicy().hasHeightForWidth())
        self.alarm_tableWidget.setSizePolicy(sizePolicy)
        self.alarm_tableWidget.setMinimumSize(QtCore.QSize(800, 0))
        self.alarm_tableWidget.setStyleSheet("QTableWidget{ \n"
                                             "  width: 100%;\n"
                                             "   padding: 15px;\n"
                                             "  text-align: left;\n"
                                             "color: white;\n"
                                             "}\n"
                                             "\n"
                                             "\n"
                                             "QHeaderView::section {\n"
                                             "color:white;\n"
                                             "    background-color: #646464;\n"
                                             "    padding: 4px;\n"
                                             "    border: 1px solid black;\n"
                                             "    font-size: 16px;\n"
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
                                             "    background-color: #646464;\n"
                                             "    border: 1px solid black;\n"
                                             "}")
        self.alarm_tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.alarm_tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.alarm_tableWidget.setObjectName("alarm_tableWidget")
        self.alarm_tableWidget.setColumnCount(5)
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
        item = QtWidgets.QTableWidgetItem()
        self.alarm_tableWidget.setHorizontalHeaderItem(4, item)
        self.alarm_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.alarm_tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.alarm_tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.alarm_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.alarm_tableWidget.verticalHeader().setVisible(False)
        self.alarm_tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.horizontalLayout_6.addWidget(self.alarm_tableWidget)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.menuStackedWidget.addWidget(self.alarm_page)
        self.storage_page = QtWidgets.QWidget()
        self.storage_page.setObjectName("storage_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.storage_page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem8 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.storage_label = QtWidgets.QLabel(self.storage_page)
        self.storage_label.setStyleSheet("FONT-WEIGHT:BOLD;\n"
                                         "font-size:24px")
        self.storage_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.storage_label.setObjectName("storage_label")
        self.horizontalLayout_9.addWidget(self.storage_label)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.show_label = QtWidgets.QLabel(self.storage_page)
        self.show_label.setObjectName("show_label")
        self.horizontalLayout_8.addWidget(self.show_label)
        spacerItem10 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
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
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem11)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem12 = QtWidgets.QSpacerItem(44, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.storage_tableWidget = QtWidgets.QTableWidget(self.storage_page)
        self.storage_tableWidget.setMinimumSize(QtCore.QSize(700, 0))
        self.storage_tableWidget.setStyleSheet("QTableWidget{ \n"
                                               "  width: 100%;\n"
                                               "   padding: 15px;\n"
                                               "  text-align: left;\n"
                                               "color: white;\n"
                                               "}\n"
                                               "\n"
                                               "\n"
                                               "QHeaderView::section {\n"
                                               "color:white;\n"
                                               "    background-color: #646464;\n"
                                               "    padding: 4px;\n"
                                               "    border: 1px solid black;\n"
                                               "    font-size: 16px;\n"
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
                                               "    background-color: #646464;\n"
                                               "    border: 1px solid black;\n"
                                               "}")
        self.storage_tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.storage_tableWidget.setObjectName("storage_tableWidget")
        self.storage_tableWidget.setColumnCount(4)
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
        item = QtWidgets.QTableWidgetItem()
        self.storage_tableWidget.setHorizontalHeaderItem(3, item)
        self.storage_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.storage_tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.storage_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.storage_tableWidget.verticalHeader().setVisible(False)
        self.storage_tableWidget.verticalHeader().setHighlightSections(False)
        self.horizontalLayout_7.addWidget(self.storage_tableWidget)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.menuStackedWidget.addWidget(self.storage_page)
        self.accountInfo_page = QtWidgets.QWidget()
        self.accountInfo_page.setObjectName("accountInfo_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.accountInfo_page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem14 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem14)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem15 = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem15)
        self.account_form = QtWidgets.QFormLayout()
        self.account_form.setObjectName("account_form")
        self.accountInfo_label = QtWidgets.QLabel(self.accountInfo_page)
        self.accountInfo_label.setStyleSheet("FONT-WEIGHT:BOLD;\n"
                                             "font-size:24px;")
        self.accountInfo_label.setObjectName("accountInfo_label")
        self.account_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.accountInfo_label)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.account_form.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem16)
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
        self.address_lineEdit.setObjectName("address_lineEdit")
        self.account_form.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.address_lineEdit)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.account_form.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem17)
        self.edit_pushButton = QtWidgets.QPushButton(self.accountInfo_page)
        self.edit_pushButton.setStyleSheet("FONT-SIZE: 18PX;")
        self.edit_pushButton.setObjectName("edit_pushButton")
        self.account_form.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.edit_pushButton)
        self.horizontalLayout_4.addLayout(self.account_form)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem18)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.menuStackedWidget.addWidget(self.accountInfo_page)
        self.usersInfo_page = QtWidgets.QWidget()
        self.usersInfo_page.setObjectName("usersInfo_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.usersInfo_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem19 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem19)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem20)
        self.userInfo_label = QtWidgets.QLabel(self.usersInfo_page)
        self.userInfo_label.setStyleSheet("FONT-WEIGHT:BOLD;\n"
                                          "font-size:24px;FONT-WEIGHT:BOLD;")
        self.userInfo_label.setObjectName("userInfo_label")
        self.horizontalLayout_16.addWidget(self.userInfo_label)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem21)
        self.verticalLayout_5.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem22 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem22)
        self.userAdd_pushButton = QtWidgets.QPushButton(self.usersInfo_page)
        self.userAdd_pushButton.setObjectName("userAdd_pushButton")
        self.horizontalLayout_15.addWidget(self.userAdd_pushButton)
        self.userDelete_pushButton = QtWidgets.QPushButton(self.usersInfo_page)
        self.userDelete_pushButton.setObjectName("userDelete_pushButton")
        self.horizontalLayout_15.addWidget(self.userDelete_pushButton)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem23)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem24)
        self.user_tableWidget = QtWidgets.QTableWidget(self.usersInfo_page)
        self.user_tableWidget.setMinimumSize(QtCore.QSize(800, 0))
        self.user_tableWidget.setStyleSheet("QTableWidget{ \n"
                                            "  width: 100%;\n"
                                            "   padding: 15px;\n"
                                            "  text-align: left;\n"
                                            "color: white;\n"
                                            "}\n"
                                            "\n"
                                            "\n"
                                            "QHeaderView::section {\n"
                                            "color:white;\n"
                                            "    background-color: #646464;\n"
                                            "    padding: 4px;\n"
                                            "    border: 1px solid black;\n"
                                            "    font-size: 16px;\n"
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
                                            "    background-color: #646464;\n"
                                            "    border: 1px solid black;\n"
                                            "}")
        self.user_tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.user_tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.user_tableWidget.setObjectName("user_tableWidget")
        self.user_tableWidget.setColumnCount(5)
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
        item = QtWidgets.QTableWidgetItem()
        self.user_tableWidget.setHorizontalHeaderItem(4, item)
        self.user_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.user_tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.user_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.user_tableWidget.verticalHeader().setVisible(False)
        self.horizontalLayout_13.addWidget(self.user_tableWidget)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem25)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.menuStackedWidget.addWidget(self.usersInfo_page)
        self.help_page = QtWidgets.QWidget()
        self.help_page.setObjectName("help_page")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.help_page)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        spacerItem26 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_12.addItem(spacerItem26)
        self.help_label = QtWidgets.QLabel(self.help_page)
        self.help_label.setObjectName("help_label")
        self.verticalLayout_12.addWidget(self.help_label)
        self.menuStackedWidget.addWidget(self.help_page)
        self.addNewUser_page = QtWidgets.QWidget()
        self.addNewUser_page.setObjectName("addNewUser_page")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.addNewUser_page)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem27 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem27)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        spacerItem28 = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem28)
        self.addUser_form = QtWidgets.QFormLayout()
        self.addUser_form.setObjectName("addUser_form")
        self.addUser_label = QtWidgets.QLabel(self.addNewUser_page)
        self.addUser_label.setStyleSheet("FONT-WEIGHT:BOLD;\n"
                                         "font-size:24px;")
        self.addUser_label.setObjectName("addUser_label")
        self.addUser_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.addUser_label)
        spacerItem29 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.addUser_form.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem29)
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
        self.aAddress_lineEdit.setObjectName("aAddress_lineEdit")
        self.addUser_form.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.aAddress_lineEdit)
        spacerItem30 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.addUser_form.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem30)
        self.aEdit_pushButton = QtWidgets.QPushButton(self.addNewUser_page)
        self.aEdit_pushButton.setStyleSheet("FONT-SIZE: 18PX;")
        self.aEdit_pushButton.setObjectName("aEdit_pushButton")
        self.addUser_form.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.aEdit_pushButton)
        self.horizontalLayout_25.addLayout(self.addUser_form)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem31)
        self.verticalLayout_8.addLayout(self.horizontalLayout_25)
        self.menuStackedWidget.addWidget(self.addNewUser_page)
        self.verticalLayout_2.addWidget(self.menuStackedWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.mainStackedWidget.addWidget(self.main_page)
        self.loggedOut_page = QtWidgets.QWidget()
        self.loggedOut_page.setStyleSheet("*{\n"
                                          "font-family: century gothic;\n"
                                          "font-size: 30px;\n"
                                          "background-color:#201f1f;\n"
                                          "}\n"
                                          "QFrame{\n"
                                          "background: #605E5C ;\n"
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
                                          "background:#201f1f;\n"
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
        spacerItem32 = QtWidgets.QSpacerItem(240, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem32)
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
        self.title3_label.setGeometry(QtCore.QRect(120, 100, 171, 40))
        self.title3_label.setStyleSheet("font-size:35px;")
        self.title3_label.setObjectName("title3_label")
        self.cancel_pushButton_3 = QtWidgets.QPushButton(self.loggedOut_frame)
        self.cancel_pushButton_3.setGeometry(QtCore.QRect(100, 420, 211, 40))
        self.cancel_pushButton_3.setObjectName("cancel_pushButton_3")
        self.loginAgain_pushButton_3 = QtWidgets.QPushButton(self.loggedOut_frame)
        self.loginAgain_pushButton_3.setGeometry(QtCore.QRect(100, 350, 211, 40))
        self.loginAgain_pushButton_3.setObjectName("loginAgain_pushButton_3")
        self.loggedOut_label_3 = QtWidgets.QLabel(self.loggedOut_frame)
        self.loggedOut_label_3.setGeometry(QtCore.QRect(70, 220, 281, 51))
        self.loggedOut_label_3.setStyleSheet("font-size:20px;")
        self.loggedOut_label_3.setObjectName("loggedOut_label_3")
        self.logo3_toolButton = QtWidgets.QToolButton(self.loggedOut_widget)
        self.logo3_toolButton.setGeometry(QtCore.QRect(210, 70, 120, 120))
        self.logo3_toolButton.setText("")
        self.logo3_toolButton.setObjectName("logo3_toolButton")
        self.loggedOut_frame.raise_()
        self.logo3_toolButton.raise_()
        self.logo3_label.raise_()
        self.horizontalLayout_27.addWidget(self.loggedOut_widget)
        spacerItem33 = QtWidgets.QSpacerItem(240, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem33)
        self.mainStackedWidget.addWidget(self.loggedOut_page)
        self.verticalLayout_6.addWidget(self.mainStackedWidget)
        surveiliaFrontEnd.setCentralWidget(self.centralwidget)

        self.retranslateUi(surveiliaFrontEnd)
        self.mainStackedWidget.setCurrentIndex(0)
        self.menuStackedWidget.setCurrentIndex(0)
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
        self.alarm_toolButton.setText(_translate("surveiliaFrontEnd", "Alarm"))
        self.storage_toolButton.setText(_translate("surveiliaFrontEnd", "Storage"))
        self.account_toolButton.setText(_translate("surveiliaFrontEnd", "Account"))
        self.help_toolButton.setText(_translate("surveiliaFrontEnd", "Help"))
        self.logout_toolButton.setText(_translate("surveiliaFrontEnd", "Logout"))
        self.users_toolButton.setText(_translate("surveiliaFrontEnd", "Users"))
        self.title_label.setText(_translate("surveiliaFrontEnd", "SURVEILIA"))
        self.camera_pushButton.setText(_translate("surveiliaFrontEnd", "Video/Image"))
        self.alarmHistory_label.setText(_translate("surveiliaFrontEnd", "ALARM HISTORY"))
        self.alarm_tableWidget.setSortingEnabled(True)
        item = self.alarm_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("surveiliaFrontEnd", "New Row"))
        item = self.alarm_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("surveiliaFrontEnd", "New Row"))
        item = self.alarm_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("surveiliaFrontEnd", "New Row"))
        item = self.alarm_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("surveiliaFrontEnd", "New Row"))
        item = self.alarm_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("surveiliaFrontEnd", "New Row"))
        item = self.alarm_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("surveiliaFrontEnd", "ID"))
        item = self.alarm_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("surveiliaFrontEnd", "Camera ID"))
        item = self.alarm_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("surveiliaFrontEnd", "Time"))
        item = self.alarm_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("surveiliaFrontEnd", "Alarm Description"))
        item = self.alarm_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("surveiliaFrontEnd", "Anomaly Clip"))
        self.storage_label.setText(_translate("surveiliaFrontEnd", "STORAGE"))
        self.show_label.setText(_translate("surveiliaFrontEnd", "             Show:"))
        self.anomalyClip_checkBox.setText(_translate("surveiliaFrontEnd", "Anomaly Clip"))
        self.cameraFeed_checkBox.setText(_translate("surveiliaFrontEnd", "Camera Feed"))
        item = self.storage_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("surveiliaFrontEnd", "New Row"))
        item = self.storage_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("surveiliaFrontEnd", "New Row"))
        item = self.storage_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("surveiliaFrontEnd", "New Row"))
        item = self.storage_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("surveiliaFrontEnd", "New Row"))
        item = self.storage_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("surveiliaFrontEnd", "New Row"))
        item = self.storage_tableWidget.verticalHeaderItem(5)
        item.setText(_translate("surveiliaFrontEnd", "New Row"))
        item = self.storage_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("surveiliaFrontEnd", "ID"))
        item = self.storage_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("surveiliaFrontEnd", "Filename"))
        item = self.storage_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("surveiliaFrontEnd", "Date"))
        item = self.storage_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("surveiliaFrontEnd", "Size"))
        self.accountInfo_label.setText(_translate("surveiliaFrontEnd", "ACCOUNT INFORMATION"))
        self.username_label.setText(_translate("surveiliaFrontEnd", "Username:"))
        self.username_lineEdit.setText(_translate("surveiliaFrontEnd", "Ifrah Tehleel"))
        self.password_label.setText(_translate("surveiliaFrontEnd", "Password:"))
        self.password_lineEdit.setText(_translate("surveiliaFrontEnd", "Ifrah"))
        self.contactInfo_label.setText(_translate("surveiliaFrontEnd", "Contact Info:"))
        self.contactInfo_lineEdit.setText(_translate("surveiliaFrontEnd", "+923014474797"))
        self.address_label.setText(_translate("surveiliaFrontEnd", "Address:"))
        self.address_lineEdit.setHtml(_translate("surveiliaFrontEnd",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
        item.setText(_translate("surveiliaFrontEnd", "New Row"))
        item = self.user_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("surveiliaFrontEnd", "New Row"))
        item = self.user_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("surveiliaFrontEnd", "New Row"))
        item = self.user_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("surveiliaFrontEnd", "New Row"))
        item = self.user_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("surveiliaFrontEnd", "New Row"))
        item = self.user_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("surveiliaFrontEnd", "ID"))
        item = self.user_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("surveiliaFrontEnd", "Name"))
        item = self.user_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("surveiliaFrontEnd", "Password"))
        item = self.user_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("surveiliaFrontEnd", "Contact Info"))
        item = self.user_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("surveiliaFrontEnd", "Address"))
        self.help_label.setText(_translate("surveiliaFrontEnd",
                                           "                                                                               HELP SECTION"))
        self.addUser_label.setText(_translate("surveiliaFrontEnd", "ADD NEW USER"))
        self.aUsername_label.setText(_translate("surveiliaFrontEnd", "Username:"))
        self.aPassword_label.setText(_translate("surveiliaFrontEnd", "Password:"))
        self.aContactInfo_label.setText(_translate("surveiliaFrontEnd", "Contact Info:"))
        self.aAddress_label.setText(_translate("surveiliaFrontEnd", "Address:"))
        self.aAddress_lineEdit.setHtml(_translate("surveiliaFrontEnd",
                                                  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'century gothic\'; font-size:18px; font-weight:400; font-style:normal;\">\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.21053pt;\"><br /></p></body></html>"))
        self.aEdit_pushButton.setText(_translate("surveiliaFrontEnd", "ADD USER"))
        self.title3_label.setText(_translate("surveiliaFrontEnd", "SURVEILIA"))
        self.cancel_pushButton_3.setText(_translate("surveiliaFrontEnd", "CANCEL"))
        self.loginAgain_pushButton_3.setText(_translate("surveiliaFrontEnd", "LOGIN AGAIN"))
        self.loggedOut_label_3.setText(_translate("surveiliaFrontEnd", "You have been logged out!"))


import resource01

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    surveiliaFrontEnd = QtWidgets.QMainWindow()
    ui = Ui_surveiliaFrontEnd()
    ui.setupUi(surveiliaFrontEnd)
    surveiliaFrontEnd.show()
    sys.exit(app.exec_())
