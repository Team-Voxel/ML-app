# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSplitter, QTabWidget, QVBoxLayout,
    QWidget)

from src.ui.terminal import terminal_widget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"#central_widget{\n"
"	border:none;\n"
"	background-color: #24292e;\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#title_frame{\n"
"	border:none;\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	background-color: #24292e;\n"
"}\n"
"\n"
"#title_frame QLabel{\n"
"	color: #fff;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#title_frame QPushButton {\n"
"	width: 50px;\n"
"	height: 35px;\n"
"	border: none;\n"
"}\n"
"\n"
"#maximize_btn:hover, #minimize_btn:hover {\n"
"	background-color: #41464a;\n"
"}\n"
"\n"
"#close_btn:hover {\n"
"	background-color: #e81123;\n"
"}\n"
"\n"
"#title_frame #close_btn {\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"\n"
"#logo_frame{\n"
"	border:none;\n"
"}\n"
"\n"
"\n"
"#main_frame QFrame, #main_frame QTabWidget {\n"
"	border: none;\n"
"	background-color: #1f2428;\n"
"}\n"
"\n"
"\n"
"#footer_frame QFrame  {\n"
"	border: none;\n"
"	background-col"
                        "or: #24292e;\n"
"	border-bottom-right-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#footer_btn_frame QPushButton  {\n"
"	width: 60px;\n"
"	height: 25px;\n"
"	border: none;\n"
"}\n"
"\n"
"#footer_btn_frame QPushButton:hover  {\n"
"	background-color: #41464a;\n"
"}\n"
"\n"
"#main_frame #side_bar {\n"
"	background-color: #24292e;\n"
"}\n"
"\n"
"#side_bar QPushButton {\n"
"	height: 50px;\n"
"	border: none;\n"
"}\n"
"\n"
"#side_bar QPushButton:hover {\n"
"	background-color: #41464a;\n"
"}\n"
"\n"
"\n"
"#terminal_hide_btn{\n"
"	width: 60px;\n"
"	height: 20px;\n"
"	border: none;\n"
"}\n"
"\n"
"#terminal_hide_btn:hover{\n"
"	background-color: #41464a;\n"
"}\n"
"\n"
"#terminal_frame #terminal_header{\n"
"	background-color: #1f2428;\n"
"}\n"
" \n"
"\n"
"\n"
"#file_menu_btn {\n"
"	width: 60px;\n"
"	height: 30px;\n"
"	border:none;\n"
"}\n"
"\n"
"#file_menu_btn:hover {\n"
"	background-color: #41464a;\n"
"}\n"
"\n"
"\n"
"\n"
"QTabBar::tab {\n"
"	background-color: #1f2428;\n"
"\n"
"	width: 140px;\n"
"}\n"
""
                        "\n"
"QTabBar::tab:selected {\n"
"	margin-top: 1.5px;\n"
"	border-top: 1.5px solid #f97a62;\n"
"	background: #1e1e1e; \n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.verticalLayout = QVBoxLayout(self.central_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_frame = QFrame(self.central_widget)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setMaximumSize(QSize(16777215, 25))
        self.title_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_bar_frame = QFrame(self.title_frame)
        self.menu_bar_frame.setObjectName(u"menu_bar_frame")
        self.menu_bar_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.menu_bar_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.menu_bar_frame)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, -1, 0)
        self.logo_frame = QFrame(self.menu_bar_frame)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.logo_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.logo_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 5, 0, 1)
        self.logo = QLabel(self.logo_frame)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(105, 18))
        self.logo.setPixmap(QPixmap(u"icons/Asset 1@4x.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.logo)


        self.horizontalLayout_2.addWidget(self.logo_frame)

        self.file_menu_btn = QPushButton(self.menu_bar_frame)
        self.file_menu_btn.setObjectName(u"file_menu_btn")

        self.horizontalLayout_2.addWidget(self.file_menu_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.horizontalLayout.addWidget(self.menu_bar_frame, 0, Qt.AlignmentFlag.AlignVCenter)

        self.window_ctrl_btn_frame = QFrame(self.title_frame)
        self.window_ctrl_btn_frame.setObjectName(u"window_ctrl_btn_frame")
        self.window_ctrl_btn_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.window_ctrl_btn_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.window_ctrl_btn_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimize_btn = QPushButton(self.window_ctrl_btn_frame)
        self.minimize_btn.setObjectName(u"minimize_btn")
        icon = QIcon()
        icon.addFile(u"icons/minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_btn.setIcon(icon)
        self.minimize_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.minimize_btn)

        self.maximize_btn = QPushButton(self.window_ctrl_btn_frame)
        self.maximize_btn.setObjectName(u"maximize_btn")
        icon1 = QIcon()
        icon1.addFile(u"icons/square.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u"icons/restore.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.maximize_btn.setIcon(icon1)
        self.maximize_btn.setIconSize(QSize(12, 12))

        self.horizontalLayout_3.addWidget(self.maximize_btn)

        self.close_btn = QPushButton(self.window_ctrl_btn_frame)
        self.close_btn.setObjectName(u"close_btn")
        icon2 = QIcon()
        icon2.addFile(u"icons/x.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon2)
        self.close_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.close_btn)


        self.horizontalLayout.addWidget(self.window_ctrl_btn_frame)


        self.verticalLayout.addWidget(self.title_frame)

        self.main_frame = QFrame(self.central_widget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.main_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.side_bar = QFrame(self.main_frame)
        self.side_bar.setObjectName(u"side_bar")
        self.side_bar.setMaximumSize(QSize(50, 16777215))
        self.side_bar.setFrameShape(QFrame.Shape.StyledPanel)
        self.side_bar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.side_bar)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.explorer_btn = QPushButton(self.side_bar)
        self.explorer_btn.setObjectName(u"explorer_btn")
        icon3 = QIcon()
        icon3.addFile(u"icons/folders.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.explorer_btn.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.explorer_btn)

        self.import_btn = QPushButton(self.side_bar)
        self.import_btn.setObjectName(u"import_btn")
        icon4 = QIcon()
        icon4.addFile(u"icons/folder-input.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.import_btn.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.import_btn)

        self.play_btn = QPushButton(self.side_bar)
        self.play_btn.setObjectName(u"play_btn")
        icon5 = QIcon()
        icon5.addFile(u"icons/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play_btn.setIcon(icon5)

        self.verticalLayout_3.addWidget(self.play_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.settings_btn = QPushButton(self.side_bar)
        self.settings_btn.setObjectName(u"settings_btn")
        icon6 = QIcon()
        icon6.addFile(u"icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_btn.setIcon(icon6)
        self.settings_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.settings_btn)


        self.horizontalLayout_7.addWidget(self.side_bar)

        self.main_body_frame = QFrame(self.main_frame)
        self.main_body_frame.setObjectName(u"main_body_frame")
        self.main_body_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_body_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_body_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.main_body_frame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.splitter.setChildrenCollapsible(True)
        self.body_frame = QFrame(self.splitter)
        self.body_frame.setObjectName(u"body_frame")
        self.body_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.body_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.body_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.body_frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setMovable(False)
        self.data_importer = QWidget()
        self.data_importer.setObjectName(u"data_importer")
        self.tabWidget.addTab(self.data_importer, "")
        self.data_preprocesser = QWidget()
        self.data_preprocesser.setObjectName(u"data_preprocesser")
        self.verticalLayout_6 = QVBoxLayout(self.data_preprocesser)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.data_preprocesser)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 748, 247))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_6.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.data_preprocesser, "")
        self.processed_data = QWidget()
        self.processed_data.setObjectName(u"processed_data")
        self.tabWidget.addTab(self.processed_data, "")

        self.verticalLayout_4.addWidget(self.tabWidget)

        self.splitter.addWidget(self.body_frame)
        self.terminal_frame = QFrame(self.splitter)
        self.terminal_frame.setObjectName(u"terminal_frame")
        self.terminal_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.terminal_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.terminal_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.terminal_header = QFrame(self.terminal_frame)
        self.terminal_header.setObjectName(u"terminal_header")
        self.terminal_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.terminal_header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.terminal_header)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(15, 5, 0, 5)
        self.terminal_label = QLabel(self.terminal_header)
        self.terminal_label.setObjectName(u"terminal_label")
        self.terminal_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.terminal_label.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.terminal_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.terminal_hide_btn = QPushButton(self.terminal_header)
        self.terminal_hide_btn.setObjectName(u"terminal_hide_btn")
        icon7 = QIcon()
        icon7.addFile(u"icons/chevron-down.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.terminal_hide_btn.setIcon(icon7)
        self.terminal_hide_btn.setIconSize(QSize(14, 14))

        self.horizontalLayout_8.addWidget(self.terminal_hide_btn)


        self.verticalLayout_5.addWidget(self.terminal_header)

        # self.term_widget = QWidget(self.terminal_frame)
        # self.term_widget.setObjectName(u"terminal_widget")
        
        self.terminal = terminal_widget()
        self.verticalLayout_5.addWidget(self.terminal)

        self.splitter.addWidget(self.terminal_frame)

        self.verticalLayout_2.addWidget(self.splitter)


        self.horizontalLayout_7.addWidget(self.main_body_frame)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.central_widget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setMaximumSize(QSize(16777215, 25))
        self.footer_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.footer_left_frame = QFrame(self.footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(20, 0, 0, 0)
        self.copyright_label = QLabel(self.footer_left_frame)
        self.copyright_label.setObjectName(u"copyright_label")
        self.copyright_label.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_5.addWidget(self.copyright_label)


        self.horizontalLayout_4.addWidget(self.footer_left_frame, 0, Qt.AlignmentFlag.AlignLeft)

        self.footer_btn_frame = QFrame(self.footer_frame)
        self.footer_btn_frame.setObjectName(u"footer_btn_frame")
        self.footer_btn_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer_btn_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_btn_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(20, 0, 0, 0)
        self.terminal_btn = QPushButton(self.footer_btn_frame)
        self.terminal_btn.setObjectName(u"terminal_btn")
        font = QFont()
        font.setPointSize(10)
        self.terminal_btn.setFont(font)

        self.horizontalLayout_6.addWidget(self.terminal_btn)

        self.footer_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.footer_spacer)


        self.horizontalLayout_4.addWidget(self.footer_btn_frame)


        self.verticalLayout.addWidget(self.footer_frame)

        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.file_menu_btn.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.minimize_btn.setText("")
        self.maximize_btn.setText("")
        self.close_btn.setText("")
        self.explorer_btn.setText("")
        self.explorer_btn.actions()
        self.import_btn.setText("")
        self.play_btn.setText("")
        self.settings_btn.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.data_importer), QCoreApplication.translate("MainWindow", u"Data Importer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.data_preprocesser), QCoreApplication.translate("MainWindow", u"Data Preprocessor", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.processed_data), QCoreApplication.translate("MainWindow", u"Processed Data", None))
        self.terminal_label.setText(QCoreApplication.translate("MainWindow", u"Terminal", None))
        self.terminal_hide_btn.setText("")
        self.copyright_label.setText(QCoreApplication.translate("MainWindow", u"neuroline.inc", None))
        self.terminal_btn.setText(QCoreApplication.translate("MainWindow", u"Terminal", None))
    # retranslateUi

