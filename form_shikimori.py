from PySide6.QtWidgets import QWidget

from catalog_manager import get_catalog
from database import Database
from form.shikimoriUI import Ui_Form
from form_auth import FormAuth
from items import Manga, RequestForm, User


class FormShikimori(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.mangas: list[Manga] = []
        self.catalog = get_catalog(1)()
        self.Form_auth = FormAuth(self.catalog)
        self.db = Database()
        self.request_params = RequestForm()
        self.cur_list = 'planned'
        self.ui.b_planned.clicked.connect(lambda: self.update_list('planned'))
        self.ui.b_watching.clicked.connect(lambda: self.update_list('watching'))
        self.ui.b_on_hold.clicked.connect(lambda: self.update_list('on_hold'))
        self.ui.b_completed.clicked.connect(lambda: self.update_list('completed'))
        self.ui.b_dropped.clicked.connect(lambda: self.update_list('dropped'))
        self.ui.b_rewatching.clicked.connect(lambda: self.update_list('rewatching'))
        self.ui.prev_page.clicked.connect(lambda: self.change_page('-'))
        self.ui.next_page.clicked.connect(lambda: self.change_page('+'))
        self.ui.btn_search.clicked.connect(self.search)
        self.ui.btn_auth.clicked.connect(self.authorize)
        self.Form_auth.accepted.connect(self.auth_accept)

    def setup(self):
        self.ui.btn_auth.setText(self.get_whoami().nickname)

    def get_current_manga(self):
        return self.catalog.get_manga(self.mangas[self.ui.list_manga.currentIndex().row()])

    def auth_accept(self):
        self.catalog.session.auth_login(self.Form_auth.get_user_data())
        self.ui.btn_auth.setText(self.get_whoami().nickname)

    def authorize(self):
        self.Form_auth.show()

    def get_whoami(self) -> User:
        return self.catalog.get_user()

    def change_page(self, page):
        match page:
            case '+':
                self.request_params.page += 1
            case '-':
                if self.request_params.page == 1:
                    return
                self.request_params.page -= 1
        self.ui.label_page.setText(f"Страница {self.request_params.page}")
        self.update_list()

    def search(self):
        self.request_params.page = 1
        self.request_params.search = self.ui.line_search.text()
        self.update_list()

    def update_list(self, lib_list=None):
        self.ui.list_manga.clear()
        if not lib_list:
            lib_list = self.cur_list
        else:
            self.cur_list = lib_list
        self.request_params.mylist = lib_list
        self.mangas = self.catalog.get_manga_login(self.request_params)
        for i in self.mangas:
            self.db.add_manga(i)
        [self.ui.list_manga.addItem(i) for i in self.get_manga_library()]

    def get_manga_library(self) -> list:
        return [i.get_name() for i in self.mangas]