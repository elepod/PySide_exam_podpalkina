"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""

from PySide6 import QtWidgets, QtCore

from lab3.b_laboratory.a_threads import WeatherHandler


class WeatherApiWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()
        self.__initSignals()

    def __initUi(self):
        self.setStyleSheet("font-size: 20px")
        self.lat = '59.9311'
        self.lon = '30.3609'
        self.thread = None  # Пока поток не создан

        self.lineEditTime = QtWidgets.QLineEdit("10")  # Задержка по умолчанию 10 сек
        self.lineEditTime.setPlaceholderText("Введите время задержки (сек)")

        self.lineEditLatitude = QtWidgets.QLineEdit(self.lat)
        self.lineEditLongitude = QtWidgets.QLineEdit(self.lon)

        self.pushButtonHandle = QtWidgets.QPushButton("Результат")
        self.pushButtonHandle.setCheckable(True)
        self.outputText = QtWidgets.QPlainTextEdit()
        self.outputText.setReadOnly(True)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lineEditTime)
        layout.addWidget(self.lineEditLatitude)
        layout.addWidget(self.lineEditLongitude)
        layout.addWidget(self.outputText)
        layout.addWidget(self.pushButtonHandle)
        self.setLayout(layout)

    def __initSignals(self):
        self.pushButtonHandle.setChecked(False)
        self.pushButtonHandle.clicked.connect(self.__handleInfoThread)
        self.lineEditLatitude.textChanged.connect(self.setLatitude)
        self.lineEditLongitude.textChanged.connect(self.setLongitude)
        self.lineEditTime.textChanged.connect(self.setDelay)

    def __handleInfoThread(self, status):
        if status:
            self.thread = WeatherHandler(lat=self.lat, lon=self.lon)
            self.thread.started.connect(lambda: print("Поток запущен"))
            self.thread.weatherHandler.connect(lambda data: self.appendInfo(data))
            self.thread.finished.connect(lambda: print("Поток остановлен"))
            self.thread.finished.connect(lambda: self.pushButtonHandle.setChecked(False))
            self.thread.finished.connect(lambda: self.outputText.clear())
            self.thread.start()
        else:
            self.thread.stop()


    def appendInfo(self, data):
        print(f'App: {data}')
        self.outputText.setPlainText(data)

    def setDelay(self, text):
        if not self.thread:
            return

        if not text:
            self.thread.setDelay(10)
        else:
            self.thread.setDelay(int(text))

    def setLatitude(self, text):
        if not text:
            self.lat = '59.9311'
        else:
            self.lat = text


    def setLongitude(self, text):
        if not text:
            self.lon = '30.3609'
        else:
            self.lon = text


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = WeatherApiWindow()
    window.show()

    app.exec()



