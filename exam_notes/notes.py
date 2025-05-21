import json

from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QPushButton, QTableView, QHBoxLayout, QVBoxLayout


class NotesWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initTableModel()
        self.__initUi()

    def __initUi(self):
        self.setStyleSheet("font-size: 20px")

        self.notesTable = QTableView()
        self.notesTable.setModel(self.tableModel)
        self.notesTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.notesTable.resizeColumnsToContents()
        self.notesTable.resizeRowsToContents()
        self.notesTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.addButton = QPushButton("Добавить")
        self.deleteButton = QPushButton("Удалить")
        self.editButton = QPushButton("Редактировать")

        layout1 = QHBoxLayout()
        layout1.addWidget(self.addButton)
        layout1.addWidget(self.deleteButton)
        layout1.addWidget(self.editButton)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.notesTable)
        main_layout.addLayout(layout1)

        self.setLayout(main_layout)
        self.setMinimumSize(600, 400)



    def initTableModel(self) -> None:
        """
        Инициализация табличной модели

        :return: None
        """

        try:
            with open("data.json", "r", encoding="utf8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
            with open("data.json", "w", encoding="utf8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

        self.tableModel = QtGui.QStandardItemModel()

        self.tableModel.setHorizontalHeaderLabels(["Название", "Дата создания", "Дата выполнения"])
        for num, item in data.items():
            item1 = QtGui.QStandardItem(item['title'])
            item1.setEditable(False)
            item2 = QtGui.QStandardItem(item['creation_date'])
            item2.setEditable(False)
            item3 = QtGui.QStandardItem(item['due_date'])
            item3.setEditable(False)
            self.tableModel.appendRow([item1, item2, item3])





if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = NotesWindow()
    window.show()

    app.exec()
