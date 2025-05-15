"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
import time

from PySide6 import QtWidgets, QtCore

from lab3.b_laboratory.a_threads import SystemInfo


class SystemInfoWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()

    def __initUi(self):
        self.setStyleSheet("font-size: 20px")

        self.lineEditTime = QtWidgets.QLineEdit("1")
        self.lineEditTime.setPlaceholderText("Введите время задержки")
        self.lineEditTime.textChanged.connect(self.setDelay)

        self.lineEditCPU = QtWidgets.QLineEdit()
        self.lineEditCPU.setReadOnly(True)
        self.lineEditRAM = QtWidgets.QLineEdit()
        self.lineEditRAM.setReadOnly(True)

        l = QtWidgets.QVBoxLayout()
        l.addWidget(self.lineEditTime)
        l.addWidget(self.lineEditCPU)
        l.addWidget(self.lineEditRAM)

        self.setLayout(l)
        self.__handleInfoThread()

    def __handleInfoThread(self):
        self.thread = SystemInfo()
        self.thread.started.connect(lambda: print("Поток запущен"))
        self.thread.systemInfoReceived.connect(lambda data: self.appenInfo(data))
        self.thread.finished.connect(lambda: print("Поток остановлен"))
        self.thread.start()

    def appenInfo(self, data):
        print(data)
        self.lineEditCPU.setText(str(data[0]))
        self.lineEditRAM.setText(str(data[1]))

    def setDelay(self, text):
        if not text:
            self.thread.delay = 1
        else:
            self.thread.delay = int(text)




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = SystemInfoWindow()
    window.show()

    app.exec()

