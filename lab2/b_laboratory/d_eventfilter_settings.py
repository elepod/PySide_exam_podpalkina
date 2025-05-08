"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings_form.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QLCDNumber

from lab2.b_laboratory.ui.d_eventfilter_settings_form import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.settings = QtCore.QSettings("MyData")
        self.lsd_mode = {
            "oct": QLCDNumber.Mode.Oct,
            "hex": QLCDNumber.Mode.Hex,
            "bin": QLCDNumber.Mode.Bin,
            "dec": QLCDNumber.Mode.Dec,
        }
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.lcdNumber.setDigitCount(8)
        self.ui.comboBox.addItem('oct')
        self.ui.comboBox.addItem('hex')
        self.ui.comboBox.addItem('bin')
        self.ui.comboBox.addItem('dec')

        self.loadData()

        self.initSignals()

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui.comboBox.currentTextChanged.connect(self.set_lcd_mode)
        self.ui.dial.valueChanged.connect(self.ui.lcdNumber.display)
        self.ui.horizontalSlider.valueChanged.connect(self.ui.lcdNumber.display)
        self.ui.dial.valueChanged.connect(self.ui.horizontalSlider.setValue)
        self.ui.horizontalSlider.valueChanged.connect(self.ui.dial.setValue)

    @Slot()
    def set_lcd_mode(self):
        current_value = self.ui.lcdNumber.value()
        self.ui.lcdNumber.setMode(self.lsd_mode[self.ui.comboBox.currentText()])
        self.ui.lcdNumber.display(current_value)
        self.setFocus()


    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        Событие нажатия на клавиатуру

        :param event: QtGui.QKeyEvent
        :return: None
        """
        if event.key() == Qt.Key.Key_Plus:
            self.ui.dial.setValue(self.ui.dial.value() + 1)
            print("#:", event.key(), "-------> text:", self.ui.dial.value())
        if event.key() == Qt.Key.Key_Minus:
            self.ui.dial.setValue(self.ui.dial.value() - 1)
            print("#:", event.key(), "-------> text:", self.ui.dial.value())


    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Событие закрытия окна

        :param event: QtGui.QCloseEvent
        :return: None
        """
        self.settings.setValue("combo_box_value", self.ui.comboBox.currentText())
        self.settings.setValue("lcd_number_value", self.ui.lcdNumber.value())
        self.settings.setValue("slider_value", self.ui.horizontalSlider.value())
        self.settings.setValue("dial_value", self.ui.dial.value())

    def loadData(self) -> None:
        """
        Загрузка данных в Ui

        :return: None
        """
        mode = self.settings.value("combo_box_value", "oct")
        self.ui.lcdNumber.setMode(self.lsd_mode[mode])
        lcd_value = float(self.settings.value("lcd_number_value", 0))
        self.ui.lcdNumber.display(lcd_value)
        self.ui.comboBox.setCurrentText(mode)
        self.ui.horizontalSlider.setValue(self.settings.value("slider_value", 0))
        self.ui.dial.setValue(self.settings.value("dial_value", 0))



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
