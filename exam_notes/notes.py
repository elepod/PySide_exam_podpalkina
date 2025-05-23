import json

from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import QPushButton, QTableView, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QDateTimeEdit, \
    QFormLayout, QPlainTextEdit


class AddNoteDialog(QtWidgets.QDialog):
    """
    Диалоговое окно для добавления новой заметки
    """

    def __init__(self, parent=None, mode="add", note_data=None, note_id=None):
        super().__init__(parent)
        self.mode = mode
        self.note_id = note_id
        self.setWindowTitle({
                                "add": "Добавить заметку",
                                "view": "Просмотр заметки",
                                "edit": "Редактировать заметку"
                            }[mode])
        self.setModal(True)

        # Создаем элементы формы
        self.titleLabel = QLabel("Название:")
        self.titleEdit = QLineEdit()

        self.descriptionLabel = QLabel("Описание:")
        self.descriptionEdit = QPlainTextEdit()
        self.descriptionEdit.setReadOnly(mode == "view")

        self.dateLabel = QLabel("Время выполнения:")
        self.dateEdit = QDateTimeEdit()
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setReadOnly(mode == "view")

        # Кнопки
        self.saveButton = QPushButton("Сохранить")
        self.cancelButton = QPushButton("Отмена")

        if mode == "view":
            self.saveButton.hide()

        # Размещаем элементы
        layout = QFormLayout()
        layout.addRow(self.titleLabel, self.titleEdit)
        layout.addRow(self.descriptionLabel, self.descriptionEdit)
        layout.addRow(self.dateLabel, self.dateEdit)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.saveButton)
        buttonLayout.addWidget(self.cancelButton)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layout)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)
        # Если переданные данные заметки (для режима просмотра)
        if note_data:
            self.titleEdit.setText(note_data.get('title', ''))
            self.descriptionEdit.setPlainText(note_data.get('text', ''))

            # Устанавливаем дату из данных заметки
            due_date = QtCore.QDateTime.fromString(
                note_data.get('due_date', ''),
                "HH:mm dd.MM.yyyy"
            )
            if due_date.isValid():
                self.dateEdit.setDateTime(due_date)

        # Подключаем сигналы
        self.saveButton.clicked.connect(self.saveNote)
        self.cancelButton.clicked.connect(self.reject)

    def saveNote(self):
        """Сохраняет заметку в таблицу и файл"""
        title = self.titleEdit.text()
        text = self.descriptionEdit.toPlainText()
        due_date = self.dateEdit.dateTime().toString("HH:mm dd.MM.yyyy")

        if not title:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Название заметки не может быть пустым")
            return

        parent_window = self.parent()
        if self.mode == "add":
            # Добавляем запись в таблицу родительского окна
            creation_date = QtCore.QDateTime.currentDateTime().toString("HH:mm dd.MM.yyyy")
            parent_window.addNoteToTable(title, creation_date, due_date, text)

            # Добавляем запись в JSON файл
            parent_window.saveDataToFile()
        elif self.mode == "edit" and self.note_id:
            parent_window.updateNoteInTable(
                self.note_id,
                title,
                due_date,
                text
            )
            parent_window.saveDataToFile()

        self.accept()


class NotesWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.notes_data = {}
        self.tableModel = QtGui.QStandardItemModel()
        self.initTableModel()
        self.initUi()
        self.initSignals()

        # Таймер для обновления подсветки каждую секунду
        self.highlight_timer = QtCore.QTimer(self)
        self.highlight_timer.timeout.connect(self.highlight_overdue_notes)
        self.highlight_timer.start(1000)

    def highlight_overdue_notes(self):
        """Подсвечивает просроченные заметки в таблице"""
        current_datetime = QtCore.QDateTime.currentDateTime()

        for row in range(self.tableModel.rowCount()):
            due_date_str = self.tableModel.item(row, 2).text()  # Дата выполнения
            due_date = QtCore.QDateTime.fromString(due_date_str, "HH:mm dd.MM.yyyy")

            # Устанавливаем стиль только если дата валидна и просрочена
            if due_date.isValid() and due_date < current_datetime:
                self.apply_highlight_style(row, True)
            else:
                self.apply_highlight_style(row, False)

    def apply_highlight_style(self, row, is_overdue):
        """Применяет стиль подсветки к строке таблицы"""
        bg_color = QtGui.QColor(255, 200, 200) if is_overdue else QtGui.QColor(255, 255, 255)
        text_color = QtGui.QColor(255, 0, 0) if is_overdue else QtGui.QColor(0, 0, 0)

        for col in range(self.tableModel.columnCount()):
            item = self.tableModel.item(row, col)
            item.setBackground(bg_color)
            if col == 2:  # Только для колонки с датой выполнения
                item.setForeground(text_color)

    def initUi(self):
        self.setStyleSheet("font-size: 20px")
        self.setWindowTitle("Список заметок")

        self.notesTable = QTableView()
        self.notesTable.setModel(self.tableModel)
        self.notesTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.notesTable.resizeColumnsToContents()
        self.notesTable.resizeRowsToContents()
        self.notesTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.addButton = QPushButton("Добавить")
        self.deleteButton = QPushButton("Удалить")
        self.editButton = QPushButton("Редактировать")
        self.showButton = QPushButton("Открыть")

        layout1 = QHBoxLayout()
        layout1.addWidget(self.addButton)
        layout1.addWidget(self.deleteButton)
        layout1.addWidget(self.editButton)
        layout1.addWidget(self.showButton)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.notesTable)
        main_layout.addLayout(layout1)

        self.setLayout(main_layout)
        self.setMinimumSize(600, 400)

    def loadDataFromFile(self):
        """Загружает данные из файла"""
        try:
            with open("data.json", "r", encoding="utf8") as file:
                loaded_data = json.load(file)

                # Очищаем текущие данные
                self.notes_data = {}
                self.tableModel.removeRows(0, self.tableModel.rowCount())

                # Сортируем записи по ID (ключам словаря)
                sorted_ids = sorted(loaded_data.keys(), key=lambda x: int(x))

                for note_id in sorted_ids:
                    note = loaded_data[note_id]
                    # Используем addNoteToTable, который сам добавит данные в self.notes_data
                    self.addNoteToTable(
                        note['title'],
                        note['creation_date'],
                        note['due_date'],
                        note.get('text', '')
                    )

        except (FileNotFoundError, json.JSONDecodeError):
            self.notes_data = {}


    def initTableModel(self) -> None:
        """
        Инициализация табличной модели и загрузка данных
        """
        self.tableModel.setHorizontalHeaderLabels(["Название", "Дата создания", "Дата выполнения"])
        self.loadDataFromFile()


    def initSignals(self):
        """Инициализация сигналов"""
        self.addButton.clicked.connect(self.onAddButtonClicked)
        self.deleteButton.clicked.connect(self.deleteSelectedNote)
        self.showButton.clicked.connect(self.showSelectedNote)
        self.editButton.clicked.connect(self.editSelectedNote)

    def onAddButtonClicked(self):
        """Обработчик нажатия кнопки добавления"""
        dialog = AddNoteDialog(self)
        dialog.exec()

    def showSelectedNote(self):
        """Просмотр выбранной заметки"""
        selected = self.notesTable.selectedIndexes()

        if not selected:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Не выбрана ни одна заметка для просмотра")
            return

        row = selected[0].row()

        # Получаем данные из выбранной строки
        title = self.tableModel.item(row, 0).text()

        # Ищем полные данные заметки (включая текст) в словаре notes_data
        note_data = None
        for note in self.notes_data.values():
            if note['title'] == title:
                note_data = note
                break

        if note_data:
            dialog = AddNoteDialog(self, mode="view", note_data=note_data)
            dialog.exec()
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Не удалось найти данные заметки")

    def editSelectedNote(self):
        """Редактирование выбранной заметки"""
        selected = self.notesTable.selectedIndexes()

        if not selected:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Не выбрана ни одна заметка для редактирования")
            return

        row = selected[0].row()

        # Получаем все данные из выбранной строки
        title = self.tableModel.item(row, 0).text()
        creation_date = self.tableModel.item(row, 1).text()

        # Ищем заметку в словаре по названию и дате создания
        note_id, note_data = None, None
        for id_, note in self.notes_data.items():
            if note['title'] == title and note['creation_date'] == creation_date:
                note_id = id_
                note_data = note
                break

        if note_data:
            dialog = AddNoteDialog(
                self,
                mode="edit",
                note_data=note_data,
                note_id=note_id
            )
            dialog.exec()
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Не удалось найти данные заметки")

    def addNoteToTable(self, title, creation_date, due_date, text):
        """Добавляет заметку в таблицу"""
        # Создаем новые элементы для таблицы
        title_item = QtGui.QStandardItem(title)
        title_item.setEditable(False)

        creation_date_item = QtGui.QStandardItem(creation_date)
        creation_date_item.setEditable(False)

        due_date_item = QtGui.QStandardItem(due_date)
        due_date_item.setEditable(False)

        # Добавляем строку в таблицу
        self.tableModel.appendRow([title_item, creation_date_item, due_date_item])

        # Добавляем данные в словарь
        note_id = str(len(self.notes_data) + 1)
        self.notes_data[note_id] = {
            'title': title,
            'creation_date': creation_date,
            'due_date': due_date,
            'text': text
        }

    def updateNoteInTable(self, note_id, title, due_date, text):
        """Обновляет заметку в таблице"""
        if note_id not in self.notes_data:
            return

        # Сохраняем старую дату создания для поиска
        creation_date = self.notes_data[note_id]['creation_date']
        old_title = self.notes_data[note_id]['title']

        # Обновляем данные в словаре
        self.notes_data[note_id].update({
            'title': title,
            'due_date': due_date,
            'text': text
        })

        # Находим строку в таблице по старому названию и дате создания
        for row in range(self.tableModel.rowCount()):
            if (self.tableModel.item(row, 0).text() == old_title and
                    self.tableModel.item(row, 1).text() == creation_date):
                # Обновляем данные в таблице
                self.tableModel.item(row, 0).setText(title)
                self.tableModel.item(row, 2).setText(due_date)

                # Обновляем подсветку
                self.highlight_overdue_notes()
                break

        self.saveDataToFile()

    def saveDataToFile(self):
        """Сохраняет данные в файл в формате JSON"""
        with open("data.json", "w", encoding="utf8") as file:
            json.dump(self.notes_data, file, ensure_ascii=False, indent=4)

    def deleteSelectedNote(self):
        """Удаляет выбранную заметку из таблицы и данных"""
        selected = self.notesTable.selectedIndexes()

        # Получаем индекс строки (все ячейки строки имеют одинаковый row)
        row = selected[0].row()

        # Удаляем запись из словаря notes_data
        # Для этого нужно найти ID записи, соответствующей этой строке
        # Так как порядок в таблице может не совпадать с порядком в словаре,
        # нам нужно найти запись по содержимому

        # Получаем данные из удаляемой строки
        title = self.tableModel.item(row, 0).text()

        # Ищем соответствующую запись в словаре
        note_id_to_delete = None
        for note_id, note in self.notes_data.items():
            if note['title'] == title:
                note_id_to_delete = note_id
                break

        del self.notes_data[note_id_to_delete]
        self.saveDataToFile()  # Сохраняем изменения в файл

        # Удаляем строку из таблицы
        self.tableModel.removeRow(row)



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = NotesWindow()
    window.show()

    app.exec()
