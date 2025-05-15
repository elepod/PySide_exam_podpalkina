"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets
from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout

from lab3.b_laboratory.b_systeminfo_widget import SystemInfoWindow
from lab3.b_laboratory.c_weatherapi_widget import WeatherApiWindow


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()

    def __initUi(self):
        self.weatherWidget = WeatherApiWindow()
        self.systemInfoWidget = SystemInfoWindow()

        main_layout = QVBoxLayout()

        group1 = QGroupBox("WeatherApi")
        group2 = QGroupBox("SystemInfo")
        layout1 = QHBoxLayout()
        layout1.addWidget(self.weatherWidget)
        group1.setLayout(layout1)

        layout2 = QHBoxLayout()
        layout2.addWidget(self.systemInfoWidget)
        group2.setLayout(layout2)

        main_layout.addWidget(group1)
        main_layout.addWidget(group2)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()