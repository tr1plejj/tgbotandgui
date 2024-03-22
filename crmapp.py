# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crmapp.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 666)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: rgb(242, 239, 229);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(135, 151, 178);\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(109, 138, 150);\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: rgb(52, 52, 74);\n"
"    border: none;\n"
"    color: rgb(247, 247, 247);\n"
"}\n"
"QPushButton:pressed {\n"
"    border: none;\n"
"    background-color: rgb(93, 112, 127);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_2.setContentsMargins(6, 0, 0, 6)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 6, -1, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.product_btn1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.product_btn1.setEnabled(True)
        self.product_btn1.setMinimumSize(QtCore.QSize(0, 0))
        self.product_btn1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/product-64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icons/product-64-pressed.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.product_btn1.setIcon(icon)
        self.product_btn1.setIconSize(QtCore.QSize(20, 20))
        self.product_btn1.setCheckable(True)
        self.product_btn1.setAutoExclusive(True)
        self.product_btn1.setFlat(False)
        self.product_btn1.setObjectName("product_btn1")
        self.verticalLayout.addWidget(self.product_btn1)
        self.offers_btn1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.offers_btn1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/activity-feed-64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icons/activity-feed-64-pressed.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.offers_btn1.setIcon(icon1)
        self.offers_btn1.setIconSize(QtCore.QSize(20, 20))
        self.offers_btn1.setCheckable(True)
        self.offers_btn1.setAutoExclusive(True)
        self.offers_btn1.setFlat(False)
        self.offers_btn1.setObjectName("offers_btn1")
        self.verticalLayout.addWidget(self.offers_btn1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 520, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.exit_btn1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.exit_btn1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/close-window-64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn1.setIcon(icon2)
        self.exit_btn1.setIconSize(QtCore.QSize(20, 20))
        self.exit_btn1.setFlat(False)
        self.exit_btn1.setObjectName("exit_btn1")
        self.verticalLayout_2.addWidget(self.exit_btn1)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.full_menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_5.setContentsMargins(6, 0, 0, 6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 6, -1, -1)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.product_btn2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.product_btn2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/product-64.ico"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/icons/product-64-pressed.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.product_btn2.setIcon(icon3)
        self.product_btn2.setIconSize(QtCore.QSize(20, 20))
        self.product_btn2.setCheckable(True)
        self.product_btn2.setAutoExclusive(True)
        self.product_btn2.setFlat(False)
        self.product_btn2.setObjectName("product_btn2")
        self.verticalLayout_3.addWidget(self.product_btn2)
        self.offers_btn2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.offers_btn2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.offers_btn2.setIcon(icon1)
        self.offers_btn2.setIconSize(QtCore.QSize(20, 20))
        self.offers_btn2.setCheckable(True)
        self.offers_btn2.setAutoExclusive(True)
        self.offers_btn2.setFlat(False)
        self.offers_btn2.setObjectName("offers_btn2")
        self.verticalLayout_3.addWidget(self.offers_btn2)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 520, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.exit_btn2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.exit_btn2.setIcon(icon2)
        self.exit_btn2.setIconSize(QtCore.QSize(20, 20))
        self.exit_btn2.setFlat(False)
        self.exit_btn2.setObjectName("exit_btn2")
        self.verticalLayout_5.addWidget(self.exit_btn2)
        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sidebar_hide_btn = QtWidgets.QPushButton(self.widget_2)
        self.sidebar_hide_btn.setAutoFillBackground(False)
        self.sidebar_hide_btn.setStyleSheet("QPushButton:checked {\n"
"    background-color: rgb(135, 151, 178);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(135, 151, 178);\n"
"}")
        self.sidebar_hide_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/menu-4-64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sidebar_hide_btn.setIcon(icon4)
        self.sidebar_hide_btn.setIconSize(QtCore.QSize(20, 20))
        self.sidebar_hide_btn.setCheckable(True)
        self.sidebar_hide_btn.setChecked(False)
        self.sidebar_hide_btn.setAutoExclusive(False)
        self.sidebar_hide_btn.setFlat(False)
        self.sidebar_hide_btn.setObjectName("sidebar_hide_btn")
        self.horizontalLayout.addWidget(self.sidebar_hide_btn)
        spacerItem2 = QtWidgets.QSpacerItem(493, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.user_btn = QtWidgets.QPushButton(self.widget_2)
        self.user_btn.setMouseTracking(False)
        self.user_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.user_btn.setAcceptDrops(False)
        self.user_btn.setStyleSheet("")
        self.user_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/user-64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(":/icons/user-64-pressed.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.user_btn.setIcon(icon5)
        self.user_btn.setIconSize(QtCore.QSize(20, 20))
        self.user_btn.setCheckable(True)
        self.user_btn.setChecked(False)
        self.user_btn.setAutoRepeat(False)
        self.user_btn.setAutoExclusive(False)
        self.user_btn.setAutoDefault(False)
        self.user_btn.setDefault(False)
        self.user_btn.setFlat(False)
        self.user_btn.setObjectName("user_btn")
        self.horizontalLayout.addWidget(self.user_btn)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.auth_page = QtWidgets.QWidget()
        self.auth_page.setObjectName("auth_page")
        self.username_login = QtWidgets.QLineEdit(self.auth_page)
        self.username_login.setGeometry(QtCore.QRect(240, 240, 121, 20))
        self.username_login.setObjectName("username_login")
        self.password_login = QtWidgets.QLineEdit(self.auth_page)
        self.password_login.setGeometry(QtCore.QRect(240, 290, 121, 20))
        self.password_login.setObjectName("password_login")
        self.login_btn = QtWidgets.QPushButton(self.auth_page)
        self.login_btn.setGeometry(QtCore.QRect(260, 340, 75, 23))
        self.login_btn.setObjectName("login_btn")
        self.switch_register_btn = QtWidgets.QPushButton(self.auth_page)
        self.switch_register_btn.setGeometry(QtCore.QRect(260, 390, 75, 23))
        self.switch_register_btn.setObjectName("switch_register_btn")
        self.stackedWidget.addWidget(self.auth_page)
        self.register_page = QtWidgets.QWidget()
        self.register_page.setObjectName("register_page")
        self.username_register = QtWidgets.QLineEdit(self.register_page)
        self.username_register.setGeometry(QtCore.QRect(200, 230, 231, 21))
        self.username_register.setObjectName("username_register")
        self.password_register = QtWidgets.QLineEdit(self.register_page)
        self.password_register.setGeometry(QtCore.QRect(200, 280, 231, 21))
        self.password_register.setObjectName("password_register")
        self.create_user_btn = QtWidgets.QPushButton(self.register_page)
        self.create_user_btn.setGeometry(QtCore.QRect(310, 370, 75, 23))
        self.create_user_btn.setObjectName("create_user_btn")
        self.switch_login_btn = QtWidgets.QPushButton(self.register_page)
        self.switch_login_btn.setGeometry(QtCore.QRect(390, 440, 75, 23))
        self.switch_login_btn.setObjectName("switch_login_btn")
        self.email = QtWidgets.QLineEdit(self.register_page)
        self.email.setGeometry(QtCore.QRect(280, 170, 113, 20))
        self.email.setObjectName("email")
        self.stackedWidget.addWidget(self.register_page)
        self.user_page = QtWidgets.QWidget()
        self.user_page.setObjectName("user_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.user_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.user_page)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.user_page)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.user_page)
        self.product_page = QtWidgets.QWidget()
        self.product_page.setObjectName("product_page")
        self.layoutWidget = QtWidgets.QWidget(self.product_page)
        self.layoutWidget.setGeometry(QtCore.QRect(370, 300, 135, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pic_path = QtWidgets.QLineEdit(self.layoutWidget)
        self.pic_path.setObjectName("pic_path")
        self.verticalLayout_7.addWidget(self.pic_path)
        self.upload_photo_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.upload_photo_btn.setFlat(True)
        self.upload_photo_btn.setObjectName("upload_photo_btn")
        self.verticalLayout_7.addWidget(self.upload_photo_btn)
        self.layoutWidget1 = QtWidgets.QWidget(self.product_page)
        self.layoutWidget1.setGeometry(QtCore.QRect(370, 400, 135, 149))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.name = QtWidgets.QLineEdit(self.layoutWidget1)
        self.name.setObjectName("name")
        self.verticalLayout_6.addWidget(self.name)
        self.price = QtWidgets.QLineEdit(self.layoutWidget1)
        self.price.setObjectName("price")
        self.verticalLayout_6.addWidget(self.price)
        self.description = QtWidgets.QLineEdit(self.layoutWidget1)
        self.description.setObjectName("description")
        self.verticalLayout_6.addWidget(self.description)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.send_product_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.send_product_btn.setFlat(True)
        self.send_product_btn.setObjectName("send_product_btn")
        self.verticalLayout_6.addWidget(self.send_product_btn)
        self.label = QtWidgets.QLabel(self.product_page)
        self.label.setGeometry(QtCore.QRect(200, 10, 491, 271))
        self.label.setStyleSheet("image: url(default_photo.png);")
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.product_page)
        self.offers_page = QtWidgets.QWidget()
        self.offers_page.setObjectName("offers_page")
        self.offers_table_widget = QtWidgets.QTableWidget(self.offers_page)
        self.offers_table_widget.setGeometry(QtCore.QRect(70, 40, 621, 451))
        self.offers_table_widget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.offers_table_widget.setAutoFillBackground(False)
        self.offers_table_widget.setStyleSheet("QTableWidget {\n"
"    background-color: transparent;\n"
"    border: 1px solid #000;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QHeaderView:section {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-bottom: 1px solid;\n"
"    padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QTableWidget:item {\n"
"    border-bottom: 1px solid;\n"
"}\n"
"\n"
"QTableWidget:item:selected {\n"
"    background-color: rgb(208, 205, 197);\n"
"} \n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    width: 15px;\n"
"    background-color: rgb(227, 224, 215);\n"
"    margin: 2px 0 2px 0;\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    max-height: 10px;\n"
"    background-color: rgb(218, 211, 200);\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:hover {\n"
"    background-color: rgb(211, 204, 194);\n"
"}\n"
"\n"
"QScrollBar::handle:pressed {\n"
"    background-color: rgb(198, 191, 182);\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    border-top-right-radius: 7px;\n"
"    border-top-left-radius: 7px;\n"
"    background-color: transparent;\n"
"    height: 10 px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    background-color: rgb(218, 211, 200);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"    background-color: rgb(198, 191, 182);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border-bottom-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    background-color: transparent;\n"
"    height: 10 px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"    background-color: rgb(218, 211, 200);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"    background-color: rgb(198, 191, 182);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.offers_table_widget.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.offers_table_widget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.offers_table_widget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.offers_table_widget.setShowGrid(False)
        self.offers_table_widget.setWordWrap(True)
        self.offers_table_widget.setObjectName("offers_table_widget")
        self.offers_table_widget.setColumnCount(4)
        self.offers_table_widget.setRowCount(18)
        item = QtWidgets.QTableWidgetItem()
        self.offers_table_widget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_table_widget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_table_widget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_table_widget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_table_widget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_table_widget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_table_widget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_table_widget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_table_widget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_table_widget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_table_widget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_table_widget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_table_widget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_table_widget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_table_widget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_table_widget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_table_widget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_table_widget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.offers_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.offers_table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.offers_table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.offers_table_widget.setHorizontalHeaderItem(3, item)
        self.offers_table_widget.horizontalHeader().setCascadingSectionResizes(True)
        self.offers_table_widget.horizontalHeader().setDefaultSectionSize(140)
        self.offers_table_widget.horizontalHeader().setHighlightSections(False)
        self.offers_table_widget.horizontalHeader().setMinimumSectionSize(40)
        self.offers_table_widget.horizontalHeader().setSortIndicatorShown(False)
        self.offers_table_widget.horizontalHeader().setStretchLastSection(True)
        self.offers_table_widget.verticalHeader().setVisible(False)
        self.offers_table_widget.verticalHeader().setCascadingSectionResizes(False)
        self.offers_table_widget.verticalHeader().setDefaultSectionSize(30)
        self.offers_table_widget.verticalHeader().setMinimumSectionSize(25)
        self.send_current_offer_btn = QtWidgets.QPushButton(self.offers_page)
        self.send_current_offer_btn.setGeometry(QtCore.QRect(580, 510, 111, 51))
        self.send_current_offer_btn.setFlat(True)
        self.send_current_offer_btn.setObjectName("send_current_offer_btn")
        self.stackedWidget.addWidget(self.offers_page)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.sidebar_hide_btn.toggled['bool'].connect(self.full_menu_widget.setHidden) # type: ignore
        self.sidebar_hide_btn.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.product_btn1.toggled['bool'].connect(self.product_btn2.setChecked) # type: ignore
        self.offers_btn1.toggled['bool'].connect(self.offers_btn2.setChecked) # type: ignore
        self.product_btn2.toggled['bool'].connect(self.product_btn1.setChecked) # type: ignore
        self.offers_btn2.toggled['bool'].connect(self.offers_btn1.setChecked) # type: ignore
        self.exit_btn1.clicked.connect(MainWindow.close) # type: ignore
        self.exit_btn2.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.product_btn2.setText(_translate("MainWindow", "Product"))
        self.offers_btn2.setText(_translate("MainWindow", "Offers"))
        self.exit_btn2.setText(_translate("MainWindow", "Exit"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.switch_register_btn.setText(_translate("MainWindow", "Register"))
        self.create_user_btn.setText(_translate("MainWindow", "PushButton"))
        self.switch_login_btn.setText(_translate("MainWindow", "PushButton"))
        self.label_3.setText(_translate("MainWindow", "Total offers:"))
        self.label_2.setText(_translate("MainWindow", "Username:"))
        self.upload_photo_btn.setText(_translate("MainWindow", "Upload Photo"))
        self.send_product_btn.setText(_translate("MainWindow", "Send product"))
        self.offers_table_widget.setSortingEnabled(False)
        item = self.offers_table_widget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.offers_table_widget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.offers_table_widget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.offers_table_widget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.offers_table_widget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.offers_table_widget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.offers_table_widget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.offers_table_widget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.offers_table_widget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.offers_table_widget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.offers_table_widget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.offers_table_widget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.offers_table_widget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.offers_table_widget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.offers_table_widget.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.offers_table_widget.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.offers_table_widget.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.offers_table_widget.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.offers_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название"))
        item = self.offers_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID"))
        item = self.offers_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Адрес доставки"))
        item = self.offers_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ID заказа"))
        self.send_current_offer_btn.setText(_translate("MainWindow", "Send current offer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
