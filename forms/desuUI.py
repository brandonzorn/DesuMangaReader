# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'desuUI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QBrush, QColor, QIcon,
                           QPalette)
from PySide6.QtWidgets import (QCheckBox, QFormLayout,
                               QFrame, QHBoxLayout, QLabel, QLineEdit,
                               QListWidget, QPushButton, QRadioButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(612, 652)
        palette = QPalette()
        Dialog.setPalette(palette)
        Dialog.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(32, 32, 32);")
        self.horizontalLayout_5 = QHBoxLayout(Dialog)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.list_manga = QListWidget(Dialog)
        self.list_manga.setObjectName(u"list_manga")
        palette1 = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(32, 32, 32, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(45, 45, 45, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush2)
        brush3 = QBrush(QColor(0, 133, 62, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush3)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush2)
        brush4 = QBrush(QColor(236, 240, 241, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush2)
        brush5 = QBrush(QColor(0, 120, 215, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Highlight, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.list_manga.setPalette(palette1)
        self.list_manga.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.list_manga)

        self.search_frame = QFrame(Dialog)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.search_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.line_search = QLineEdit(self.search_frame)
        self.line_search.setObjectName(u"line_search")
        self.line_search.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.line_search)

        self.btn_search = QPushButton(self.search_frame)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"images/search.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_search.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.btn_search)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.prev_page = QPushButton(self.search_frame)
        self.prev_page.setObjectName(u"prev_page")
        self.prev_page.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"images/prev.png", QSize(), QIcon.Normal, QIcon.On)
        self.prev_page.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.prev_page)

        self.label_page = QLabel(self.search_frame)
        self.label_page.setObjectName(u"label_page")

        self.horizontalLayout_3.addWidget(self.label_page)

        self.next_page = QPushButton(self.search_frame)
        self.next_page.setObjectName(u"next_page")
        self.next_page.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u"images/next.png", QSize(), QIcon.Normal, QIcon.On)
        self.next_page.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.next_page)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.search_frame)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.catalog_list = QListWidget(Dialog)
        self.catalog_list.setObjectName(u"catalog_list")
        self.catalog_list.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catalog_list.sizePolicy().hasHeightForWidth())
        self.catalog_list.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.catalog_list)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.filters_frame = QFrame(Dialog)
        self.filters_frame.setObjectName(u"filters_frame")
        self.filters_frame.setFrameShape(QFrame.StyledPanel)
        self.filters_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.filters_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.order_frame = QFrame(self.filters_frame)
        self.order_frame.setObjectName(u"order_frame")
        self.order_frame.setFrameShape(QFrame.StyledPanel)
        self.order_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.order_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_sort = QLabel(self.order_frame)
        self.label_sort.setObjectName(u"label_sort")

        self.verticalLayout_2.addWidget(self.label_sort)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.sort_popular = QRadioButton(self.order_frame)
        self.sort_popular.setObjectName(u"sort_popular")
        self.sort_popular.setChecked(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.sort_popular)

        self.sort_name = QRadioButton(self.order_frame)
        self.sort_name.setObjectName(u"sort_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.sort_name)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout_6.addWidget(self.order_frame)

        self.kind_frame = QFrame(self.filters_frame)
        self.kind_frame.setObjectName(u"kind_frame")
        self.kind_frame.setFrameShape(QFrame.StyledPanel)
        self.kind_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.kind_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_type = QLabel(self.kind_frame)
        self.label_type.setObjectName(u"label_type")

        self.verticalLayout_4.addWidget(self.label_type)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.type_manga = QCheckBox(self.kind_frame)
        self.type_manga.setObjectName(u"type_manga")
        self.type_manga.setChecked(False)
        self.type_manga.setTristate(False)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.type_manga)

        self.type_manhua = QCheckBox(self.kind_frame)
        self.type_manhua.setObjectName(u"type_manhua")
        self.type_manhua.setChecked(False)
        self.type_manhua.setTristate(False)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.type_manhua)

        self.type_manhwa = QCheckBox(self.kind_frame)
        self.type_manhwa.setObjectName(u"type_manhwa")
        self.type_manhwa.setChecked(False)
        self.type_manhwa.setTristate(False)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.type_manhwa)

        self.type_one_shot = QCheckBox(self.kind_frame)
        self.type_one_shot.setObjectName(u"type_one_shot")
        self.type_one_shot.setChecked(False)
        self.type_one_shot.setTristate(False)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.type_one_shot)

        self.type_comics = QCheckBox(self.kind_frame)
        self.type_comics.setObjectName(u"type_comics")
        self.type_comics.setChecked(False)
        self.type_comics.setTristate(False)

        self.formLayout_2.setWidget(2, QFormLayout.SpanningRole, self.type_comics)


        self.verticalLayout_4.addLayout(self.formLayout_2)


        self.verticalLayout_6.addWidget(self.kind_frame)

        self.genres_frame = QFrame(self.filters_frame)
        self.genres_frame.setObjectName(u"genres_frame")
        self.genres_frame.setFrameShape(QFrame.StyledPanel)
        self.genres_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.genres_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_genre = QLabel(self.genres_frame)
        self.label_genre.setObjectName(u"label_genre")

        self.verticalLayout_5.addWidget(self.label_genre)

        self.btn_genres_list = QPushButton(self.genres_frame)
        self.btn_genres_list.setObjectName(u"btn_genres_list")
        self.btn_genres_list.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.btn_genres_list)


        self.verticalLayout_6.addWidget(self.genres_frame)

        self.catalogs_frame = QFrame(self.filters_frame)
        self.catalogs_frame.setObjectName(u"catalogs_frame")
        self.catalogs_frame.setFrameShape(QFrame.StyledPanel)
        self.catalogs_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.catalogs_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_catalogs = QPushButton(self.catalogs_frame)
        self.btn_catalogs.setObjectName(u"btn_catalogs")
        self.btn_catalogs.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.btn_catalogs)


        self.verticalLayout_6.addWidget(self.catalogs_frame)


        self.verticalLayout_3.addWidget(self.filters_frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filter_reset = QPushButton(Dialog)
        self.filter_reset.setObjectName(u"filter_reset")
        self.filter_reset.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.filter_reset)

        self.filter_apply = QPushButton(Dialog)
        self.filter_apply.setObjectName(u"filter_apply")
        self.filter_apply.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.filter_apply)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_search.setText("")
        self.prev_page.setText("")
        self.label_page.setText(QCoreApplication.translate("Dialog", u" \u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 1", None))
        self.next_page.setText("")
        self.label_sort.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.sort_popular.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043f\u0443\u043b\u044f\u0440\u043d\u043e\u0441\u0442\u044c", None))
        self.sort_name.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_type.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f", None))
        self.type_manga.setText(QCoreApplication.translate("Dialog", u"\u041c\u0430\u043d\u0433\u0430", None))
        self.type_manhua.setText(QCoreApplication.translate("Dialog", u"\u041c\u0430\u043d\u044c\u0445\u0443\u0430", None))
        self.type_manhwa.setText(QCoreApplication.translate("Dialog", u"\u041c\u0430\u043d\u0445\u0432\u0430", None))
        self.type_one_shot.setText(QCoreApplication.translate("Dialog", u"\u0412\u0430\u043d\u0448\u043e\u0442", None))
        self.type_comics.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043c\u0438\u043a\u0441", None))
        self.label_genre.setText(QCoreApplication.translate("Dialog", u"\u0416\u0430\u043d\u0440", None))
        self.btn_genres_list.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0436\u0430\u043d\u0440\u043e\u0432", None))
        self.btn_catalogs.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433\u0438", None))
        self.filter_reset.setText(QCoreApplication.translate("Dialog", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.filter_apply.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

