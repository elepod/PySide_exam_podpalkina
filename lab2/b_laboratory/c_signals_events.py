"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""
import time

from PySide6 import QtWidgets, QtGui, QtCore
from lab2.b_laboratory.ui.c_signals_events_form import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui.pushButtonMoveCoords.clicked.connect(self.onPushButtonMoveCoordsClicked)
        self.ui.pushButtonGetData.clicked.connect(self.onPushButtonGetDataClicked)


    def onPushButtonMoveCoordsClicked(self):
        self.move(self.ui.spinBoxX.value(), self.ui.spinBoxY.value())

    def onPushButtonGetDataClicked(self):
        screen = QtGui.QGuiApplication.primaryScreen()
        self.ui.plainTextEdit.setPlainText("Time: " + str(time.ctime()))
        self.ui.plainTextEdit.appendPlainText("Кол-во экранов: " + str(len(QtGui.QGuiApplication.screens())))
        self.ui.plainTextEdit.appendPlainText("Текущее основное окно: " + str(screen.name()))
        self.ui.plainTextEdit.appendPlainText("Разрешение экрана: " +
                                              str(screen.size().width())+ "X" + str(screen.size().height()))
        self.ui.plainTextEdit.appendPlainText("На каком экране окно находится: " + str(self.windowHandle().screen().name()))
        self.ui.plainTextEdit.appendPlainText("Минимальные размеры окна: " +
                                              str(self.minimumSize().width()) + "X" + str(self.minimumSize().height()))
        self.ui.plainTextEdit.appendPlainText("Текущее положение (координаты) окна: " + "x: " +
                                              str(self.geometry().x()) + ", y: " + str(self.geometry().y()))
        self.ui.plainTextEdit.appendPlainText("Координаты центра приложения: " + "x: " +
                                              str(self.geometry().center().x()) + ", y: " +
                                              str(self.geometry().center().y()))
        self.ui.plainTextEdit.appendPlainText("Состояние Cвернуто: " + str(self.isHidden()))
        self.ui.plainTextEdit.appendPlainText("Состояние Развёрнуто: " + str(self.isFullScreen()))
        self.ui.plainTextEdit.appendPlainText("Состояние Активно: " + str(self.isActiveWindow()))
        self.ui.plainTextEdit.appendPlainText("Состояние Отображено: " + str(self.isVisible()))


    def event(self, event: QtCore.QEvent):
        if event.type() == QtCore.QEvent.Type.Move:
            print(time.ctime(), "---->", " x:", self.window().x(), " y: ", self.window().y())
        if event.type() == QtCore.QEvent.Type.Resize:
            print(time.ctime(), "---->", " width:", self.window().width(), " height: ", self.window().height())

        return super().event(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
