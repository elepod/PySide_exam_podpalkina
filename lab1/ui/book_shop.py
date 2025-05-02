# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'book_shop.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(623, 474)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 0, 602, 472))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(500, 50))
        self.label_3.setMaximumSize(QSize(500, 50))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(170, 0, 127);")

        self.verticalLayout_2.addWidget(self.label_3)

        self.listWidget = QListWidget(self.widget)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setFont(font1);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setFont(font1);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setFont(font1);
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_2.addWidget(self.listWidget)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(500, 50))
        self.label_2.setMaximumSize(QSize(500, 50))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(170, 0, 127);")

        self.verticalLayout_2.addWidget(self.label_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(160, 30))
        self.radioButton.setMaximumSize(QSize(160, 30))
        font2 = QFont()
        font2.setPointSize(14)
        self.radioButton.setFont(font2)

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMinimumSize(QSize(160, 30))
        self.radioButton_2.setMaximumSize(QSize(160, 30))
        self.radioButton_2.setFont(font2)

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.widget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setMinimumSize(QSize(160, 30))
        self.radioButton_3.setMaximumSize(QSize(160, 30))
        self.radioButton_3.setFont(font2)

        self.verticalLayout.addWidget(self.radioButton_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(600, 50))
        self.pushButton.setMaximumSize(QSize(600, 50))
        font3 = QFont()
        font3.setPointSize(16)
        self.pushButton.setFont(font3)

        self.verticalLayout_2.addWidget(self.pushButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043d\u0438\u0433\u0443", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"\u0413\u0430\u0440\u0440\u0438 \u041f\u043e\u0442\u0442\u0435\u0440", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"\u0423\u043d\u0435\u0441\u0435\u043d\u043d\u044b\u0435 \u0432\u0435\u0442\u0440\u043e\u043c", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0439\u043d\u0430 \u0438 \u043c\u0438\u0440", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043f\u043e\u0441\u043e\u0431 \u043e\u043f\u043b\u0430\u0442\u044b", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u041f\u043e \u043a\u0430\u0440\u0442\u0435", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u041f\u043e QR", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u043b\u0438\u0447\u043d\u044b\u043c\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041e\u043f\u043b\u0430\u0442\u0438\u0442\u044c", None))
    # retranslateUi

