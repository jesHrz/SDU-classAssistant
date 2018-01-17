# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1185, 650)
        MainWindow.setMinimumSize(QtCore.QSize(1185, 650))
        MainWindow.setMaximumSize(QtCore.QSize(1185, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 370, 350))
        self.groupBox.setObjectName("groupBox")
        self.label_dd = QtWidgets.QLabel(self.groupBox)
        self.label_dd.setGeometry(QtCore.QRect(60, 235, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(11)
        self.label_dd.setFont(font)
        self.label_dd.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_dd.setTextFormat(QtCore.Qt.AutoText)
        self.label_dd.setObjectName("label_dd")
        self.label_jsm = QtWidgets.QLabel(self.groupBox)
        self.label_jsm.setGeometry(QtCore.QRect(40, 70, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(11)
        self.label_jsm.setFont(font)
        self.label_jsm.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_jsm.setTextFormat(QtCore.Qt.AutoText)
        self.label_jsm.setObjectName("label_jsm")
        self.label_xy = QtWidgets.QLabel(self.groupBox)
        self.label_xy.setGeometry(QtCore.QRect(20, 110, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(11)
        self.label_xy.setFont(font)
        self.label_xy.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_xy.setTextFormat(QtCore.Qt.AutoText)
        self.label_xy.setObjectName("label_xy")
        self.label_xq = QtWidgets.QLabel(self.groupBox)
        self.label_xq.setGeometry(QtCore.QRect(20, 150, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(11)
        self.label_xq.setFont(font)
        self.label_xq.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_xq.setTextFormat(QtCore.Qt.AutoText)
        self.label_xq.setObjectName("label_xq")
        self.label_jc = QtWidgets.QLabel(self.groupBox)
        self.label_jc.setGeometry(QtCore.QRect(20, 190, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(11)
        self.label_jc.setFont(font)
        self.label_jc.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_jc.setTextFormat(QtCore.Qt.AutoText)
        self.label_jc.setObjectName("label_jc")
        self.label_kch = QtWidgets.QLabel(self.groupBox)
        self.label_kch.setGeometry(QtCore.QRect(40, 30, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(11)
        self.label_kch.setFont(font)
        self.label_kch.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_kch.setTextFormat(QtCore.Qt.AutoText)
        self.label_kch.setObjectName("label_kch")
        self.button_search = QtWidgets.QPushButton(self.groupBox)
        self.button_search.setEnabled(True)
        self.button_search.setGeometry(QtCore.QRect(250, 280, 90, 35))
        self.button_search.setObjectName("button_search")
        self.comboBox_xq = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_xq.setGeometry(QtCore.QRect(120, 150, 220, 30))
        self.comboBox_xq.setObjectName("comboBox_xq")
        self.comboBox_xq.addItem("")
        self.comboBox_xq.setItemText(0, "")
        self.comboBox_xq.addItem("")
        self.comboBox_xq.addItem("")
        self.comboBox_xq.addItem("")
        self.comboBox_xq.addItem("")
        self.comboBox_xq.addItem("")
        self.comboBox_xq.addItem("")
        self.comboBox_xq.addItem("")
        self.comboBox_jc = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_jc.setGeometry(QtCore.QRect(120, 190, 220, 30))
        self.comboBox_jc.setObjectName("comboBox_jc")
        self.comboBox_jc.addItem("")
        self.comboBox_jc.setItemText(0, "")
        self.comboBox_jc.addItem("")
        self.comboBox_jc.addItem("")
        self.comboBox_jc.addItem("")
        self.comboBox_jc.addItem("")
        self.comboBox_jc.addItem("")
        self.comboBox_dd = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_dd.setGeometry(QtCore.QRect(120, 230, 220, 30))
        self.comboBox_dd.setObjectName("comboBox_dd")
        self.comboBox_dd.addItem("")
        self.comboBox_dd.setItemText(0, "")
        self.comboBox_dd.addItem("")
        self.comboBox_dd.addItem("")
        self.comboBox_dd.addItem("")
        self.comboBox_dd.addItem("")
        self.comboBox_dd.addItem("")
        self.comboBox_dd.addItem("")
        self.comboBox_dd.addItem("")
        self.line_kch = QtWidgets.QLineEdit(self.groupBox)
        self.line_kch.setGeometry(QtCore.QRect(120, 30, 220, 30))
        self.line_kch.setObjectName("line_kch")
        self.line_jsm = QtWidgets.QLineEdit(self.groupBox)
        self.line_jsm.setGeometry(QtCore.QRect(120, 70, 220, 30))
        self.line_jsm.setObjectName("line_jsm")
        self.line_xy = QtWidgets.QLineEdit(self.groupBox)
        self.line_xy.setGeometry(QtCore.QRect(120, 110, 220, 30))
        self.line_xy.setObjectName("line_xy")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 370, 370, 120))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_time = QtWidgets.QLabel(self.groupBox_2)
        self.label_time.setGeometry(QtCore.QRect(20, 30, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(11)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_time")
        self.button_start = QtWidgets.QPushButton(self.groupBox_2)
        self.button_start.setGeometry(QtCore.QRect(250, 30, 90, 35))
        self.button_start.setObjectName("button_start")
        self.button_stop = QtWidgets.QPushButton(self.groupBox_2)
        self.button_stop.setGeometry(QtCore.QRect(250, 70, 90, 35))
        self.button_stop.setObjectName("button_stop")
        self.line_time = QtWidgets.QLineEdit(self.groupBox_2)
        self.line_time.setGeometry(QtCore.QRect(120, 30, 100, 30))
        self.line_time.setObjectName("line_time")
        self.table_info = QtWidgets.QTableWidget(self.centralwidget)
        self.table_info.setGeometry(QtCore.QRect(410, 10, 755, 570))
        self.table_info.setRowCount(0)
        self.table_info.setColumnCount(5)
        self.table_info.setObjectName("table_info")
        self.table_info.setHorizontalHeaderLabels(['课程号', '课序号','课程名称', '教师', '课余量'])
        self.table_info.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.table_info.setAlternatingRowColors(True)
        self.table_info.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_info.setColumnWidth(1, 80)
        self.table_info.setColumnWidth(2, 280)
        self.table_info.setColumnWidth(4, 80)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1050, 30))
        self.menubar.setObjectName("menubar")
        self.menu_option = QtWidgets.QMenu(self.menubar)
        self.menu_option.setObjectName("menu_option")
        self.menu_other = QtWidgets.QMenu(self.menubar)
        self.menu_other.setObjectName(("menu_other"))
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setToolTipDuration(-1)
        self.statusbar.setStatusTip("")
        self.statusbar.setWhatsThis("")
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage("未登录")
        MainWindow.setStatusBar(self.statusbar)
        self.action_login = QtWidgets.QAction(MainWindow)
        self.action_login.setObjectName("action_login")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_check = QtWidgets.QAction(MainWindow)
        self.action_check.setObjectName("action_check")
        self.menu_option.addAction(self.action_login)
        self.menu_option.addAction(self.action_check)
        self.menu_option.addSeparator()
        self.menu_option.addAction(self.action_exit)
        MainWindow.setMenuBar(self.menubar)
        self.action_update = QtWidgets.QAction(MainWindow)
        self.action_update.setObjectName("action_update")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.menu_other.addAction(self.action_update)
        self.menu_other.addAction(self.action_about)
        self.menubar.addAction(self.menu_option.menuAction())
        self.menubar.addAction(self.menu_other.menuAction())
        self.timer = QtCore.QTimer()
        #   没登陆前将所有组件设为disable
        self.setEnable(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "山东大学选课助手"))
        self.groupBox.setTitle(_translate("MainWindow", "查询条件"))
        self.label_dd.setText(_translate("MainWindow", "校区"))
        self.label_jsm.setText(_translate("MainWindow", "教师名"))
        self.label_xy.setText(_translate("MainWindow", "开课学院"))
        self.label_xq.setText(_translate("MainWindow", "上课星期"))
        self.label_jc.setText(_translate("MainWindow", "上课节次"))
        self.label_kch.setText(_translate("MainWindow", "课程名"))
        self.button_search.setText(_translate("MainWindow", "查询"))
        self.comboBox_xq.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_xq.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_xq.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_xq.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_xq.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_xq.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_xq.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_jc.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_jc.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_jc.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_jc.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_jc.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_dd.setItemText(1, _translate("MainWindow", "中心校区"))
        self.comboBox_dd.setItemText(2, _translate("MainWindow", "洪家楼校区"))
        self.comboBox_dd.setItemText(3, _translate("MainWindow", "趵突泉校区"))
        self.comboBox_dd.setItemText(4, _translate("MainWindow", "兴隆山校区"))
        self.comboBox_dd.setItemText(5, _translate("MainWindow", "软件园校区"))
        self.comboBox_dd.setItemText(6, _translate("MainWindow", "千佛山校区"))
        self.comboBox_dd.setItemText(7, _translate("MainWindow", "青岛校区"))
        self.groupBox_2.setTitle(_translate("MainWindow", "监视"))
        self.label_time.setText(_translate("MainWindow", "刷新间隔"))
        self.button_start.setText(_translate("MainWindow", "开始监视"))
        self.button_stop.setText(_translate("MainWindow", "停止监视"))
        self.menu_option.setTitle(_translate("MainWindow", "选项"))
        self.menu_other.setTitle(_translate("MainWindow", "其他"))
        self.action_login.setText(_translate("MainWindow", "登录"))
        self.action_exit.setText(_translate("MainWindow", "退出"))
        self.action_update.setText(_translate("MainWindow", "更新"))
        self.action_about.setText(_translate("MainWindow", "关于"))
        self.action_check.setText(_translate("MainWindow", "查看课程"))

    def setEnable(self, status):
        self.line_time.setEnabled(status)
        self.line_xy.setEnabled(status)
        self.line_jsm.setEnabled(status)
        self.line_kch.setEnabled(status)
        self.button_search.setEnabled(status)
        self.button_start.setEnabled(status)
        self.button_stop.setEnabled(status)
        self.comboBox_dd.setEnabled(status)
        self.comboBox_xq.setEnabled(status)
        self.comboBox_jc.setEnabled(status)
        self.action_check.setEnabled(status)