# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(660, 501)
        Dialog.setStyleSheet(u"background-color: qlineargradient(\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0 #1a1a2e,\n"
"    stop:1 #16213e\n"
");")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBox_1 = QComboBox(Dialog)
        self.comboBox_1.setObjectName(u"comboBox_1")
        self.comboBox_1.setStyleSheet(u"background-color: white;\n"
"border: 1px solid gray;\n"
"border-radius: 8px;\n"
"padding: 5px;")

        self.verticalLayout_4.addWidget(self.comboBox_1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"border: 1px solid gray;\n"
"border-radius: 10px;\n"
"padding: 10px;\n"
"font-size: 14px;\n"
"")

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_next = QPushButton(Dialog)
        self.pushButton_next.setObjectName(u"pushButton_next")
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setBold(True)
        self.pushButton_next.setFont(font)
        self.pushButton_next.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    cursor: pointer;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1c5980;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_next, 0, 1, 1, 1)

        self.pushButton_Author = QPushButton(Dialog)
        self.pushButton_Author.setObjectName(u"pushButton_Author")
        self.pushButton_Author.setFont(font)
        self.pushButton_Author.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    cursor: pointer;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1c5980;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_Author, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.pushButton_next.setText(QCoreApplication.translate("Dialog", u"Next sentence\U0001f504", None))
        self.pushButton_Author.setText(QCoreApplication.translate("Dialog", u"Author\u270d", None))
    # retranslateUi

