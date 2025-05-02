# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'engine_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(730, 254)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(700, 220))
        self.groupBox.setMaximumSize(QSize(700, 220))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(118, 27, 102, 168))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSlider_2 = QSlider(self.layoutWidget)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setMinimumSize(QSize(18, 140))
        self.verticalSlider_2.setMaximumSize(QSize(18, 140))
        self.verticalSlider_2.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_2.addWidget(self.verticalSlider_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 20))
        self.label_2.setMaximumSize(QSize(100, 20))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(226, 27, 102, 168))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSlider_5 = QSlider(self.layoutWidget1)
        self.verticalSlider_5.setObjectName(u"verticalSlider_5")
        self.verticalSlider_5.setMinimumSize(QSize(18, 140))
        self.verticalSlider_5.setMaximumSize(QSize(18, 140))
        self.verticalSlider_5.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_3.addWidget(self.verticalSlider_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 20))
        self.label_3.setMaximumSize(QSize(100, 20))
        self.label_3.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_3)

        self.layoutWidget2 = QWidget(self.groupBox)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(334, 27, 102, 168))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSlider_4 = QSlider(self.layoutWidget2)
        self.verticalSlider_4.setObjectName(u"verticalSlider_4")
        self.verticalSlider_4.setMinimumSize(QSize(18, 140))
        self.verticalSlider_4.setMaximumSize(QSize(18, 140))
        self.verticalSlider_4.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_4.addWidget(self.verticalSlider_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 20))
        self.label_5.setMaximumSize(QSize(100, 20))
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.layoutWidget3 = QWidget(self.groupBox)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(442, 27, 228, 170))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(118, 28, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSlider = QSlider(self.layoutWidget3)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMinimumSize(QSize(18, 140))
        self.verticalSlider.setMaximumSize(QSize(18, 140))
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_5.addWidget(self.verticalSlider, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_4 = QLabel(self.layoutWidget3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 20))
        self.label_4.setMaximumSize(QSize(100, 20))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.layoutWidget4 = QWidget(self.groupBox)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(11, 30, 102, 168))
        self.verticalLayout = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSlider_3 = QSlider(self.layoutWidget4)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        self.verticalSlider_3.setMinimumSize(QSize(18, 140))
        self.verticalSlider_3.setMaximumSize(QSize(18, 140))
        self.verticalSlider_3.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout.addWidget(self.verticalSlider_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel(self.layoutWidget4)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 20))
        self.label.setMaximumSize(QSize(100, 20))
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u043c\u0438 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21162", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21163", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21164", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0449\u0430\u044f \u0442\u044f\u0433\u0430", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21161", None))
    # retranslateUi

