# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(350, 240)
        Dialog.setMinimumSize(QSize(350, 240))
        Dialog.setMaximumSize(QSize(350, 240))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.login = QLabel(Dialog)
        self.login.setObjectName(u"login")
        self.login.setMinimumSize(QSize(160, 24))
        self.login.setMaximumSize(QSize(160, 24))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        self.login.setFont(font)

        self.horizontalLayout.addWidget(self.login)

        self.loginField = QLineEdit(Dialog)
        self.loginField.setObjectName(u"loginField")
        self.loginField.setMinimumSize(QSize(160, 24))
        self.loginField.setMaximumSize(QSize(160, 24))

        self.horizontalLayout.addWidget(self.loginField)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.password = QLabel(Dialog)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(160, 24))
        self.password.setMaximumSize(QSize(160, 24))
        self.password.setFont(font)

        self.horizontalLayout_2.addWidget(self.password)

        self.passwordField = QLineEdit(Dialog)
        self.passwordField.setObjectName(u"passwordField")
        self.passwordField.setMinimumSize(QSize(160, 24))
        self.passwordField.setMaximumSize(QSize(160, 24))
        self.passwordField.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_2.addWidget(self.passwordField)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 119, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pressOk = QPushButton(Dialog)
        self.pressOk.setObjectName(u"pressOk")
        self.pressOk.setMinimumSize(QSize(320, 30))
        self.pressOk.setMaximumSize(QSize(320, 30))

        self.verticalLayout.addWidget(self.pressOk)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.login.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.loginField.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d", None))
        self.password.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.passwordField.setText("")
        self.passwordField.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.pressOk.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

