# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_titre = QLabel(self.centralwidget)
        self.label_titre.setObjectName(u"label_titre")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_titre.setFont(font)
        self.label_titre.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_titre)

        self.lineEdit_message = QLineEdit(self.centralwidget)
        self.lineEdit_message.setObjectName(u"lineEdit_message")

        self.verticalLayout.addWidget(self.lineEdit_message)

        self.pushButton_afficher = QPushButton(self.centralwidget)
        self.pushButton_afficher.setObjectName(u"pushButton_afficher")

        self.verticalLayout.addWidget(self.pushButton_afficher)

        self.label_affichage = QLabel(self.centralwidget)
        self.label_affichage.setObjectName(u"label_affichage")
        self.label_affichage.setAlignment(Qt.AlignCenter)
        self.label_affichage.setWordWrap(True)
        self.label_affichage.setMinimumSize(QSize(0, 60))

        self.verticalLayout.addWidget(self.label_affichage)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Examen PyQt6 - Partie 1", None))
        self.label_titre.setText(QCoreApplication.translate("MainWindow", u"Saisissez votre message :", None))
        self.lineEdit_message.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tapez votre message ici...", None))
        self.pushButton_afficher.setText(QCoreApplication.translate("MainWindow", u"Afficher le message", None))
        self.label_affichage.setText("")
        self.label_affichage.setStyleSheet(QCoreApplication.translate("MainWindow", u"QLabel {\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    background-color: #f0f0f0;\n"
"}", None))
    # retranslateUi

