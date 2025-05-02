# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(729, 518)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 30))
        self.label.setMaximumSize(QSize(99, 30))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(318, 28, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(200, 30))
        self.lineEdit.setMaximumSize(QSize(200, 30))
        self.lineEdit.setPlaceholderText(u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0435\u0440\u0432\u043e\u0435 \u0447\u0438\u0441\u043b\u043e")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 30))
        self.label_2.setMaximumSize(QSize(100, 30))
        self.label_2.setBaseSize(QSize(100, 30))
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(318, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(200, 30))
        self.lineEdit_2.setMaximumSize(QSize(200, 30))
        self.lineEdit_2.setPlaceholderText(u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0442\u043e\u0440\u043e\u0435 \u0447\u0438\u0441\u043b\u043e")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(150, 30))
        self.pushButton_2.setMaximumSize(QSize(150, 30))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        self.pushButton_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setMaximumSize(QSize(150, 30))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.pushButton.setFont(font2)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(150, 30))
        self.pushButton_3.setMaximumSize(QSize(150, 30))
        self.pushButton_3.setFont(font2)

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(150, 30))
        self.pushButton_4.setMaximumSize(QSize(150, 30))
        self.pushButton_4.setFont(font2)

        self.horizontalLayout_3.addWidget(self.pushButton_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setPointSize(72)
        font3.setBold(False)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0432\u043e\u0435 \u0447\u0438\u0441\u043b\u043e", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0412\u0442\u043e\u0440\u043e\u0435 \u0447\u0438\u0441\u043b\u043e", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"*", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"/", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"0", None))
    # retranslateUi

