from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QWidget, QListWidgetItem

from const.icons import delete_icon_path
from database import Database
from forms.ui_history import Ui_Dialog
from items import HistoryNote


class FormHistory(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btn_delete.setIcon(QIcon(delete_icon_path))
        self.db: Database = Database()
        self.ui.btn_delete.clicked.connect(self.delete_note)
        self.notes: list[HistoryNote] = []

    def setup(self):
        self.ui.listWidget.clear()
        self.notes: list[HistoryNote] = self.db.get_history_notes()
        for note in self.notes:
            item = QListWidgetItem(note.get_name())
            if note.is_completed:
                item.setBackground(QColor("GREEN"))
            else:
                item.setBackground(QColor("RED"))
            self.ui.listWidget.addItem(item)

    def get_current_manga(self):
        return self.notes[self.ui.listWidget.currentIndex().row()].manga

    def delete_note(self):
        if self.ui.listWidget.currentIndex().row() >= 0:
            self.db.del_history_note(self.notes[self.ui.listWidget.currentIndex().row()].chapter)
            self.setup()
