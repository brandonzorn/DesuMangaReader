# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desu_genresUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(728, 329)
        Dialog.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.g_parody = QtWidgets.QCheckBox(Dialog)
        self.g_parody.setObjectName("g_parody")
        self.gridLayout.addWidget(self.g_parody, 4, 3, 1, 1)
        self.g_space = QtWidgets.QCheckBox(Dialog)
        self.g_space.setObjectName("g_space")
        self.gridLayout.addWidget(self.g_space, 3, 1, 1, 1)
        self.g_color = QtWidgets.QCheckBox(Dialog)
        self.g_color.setObjectName("g_color")
        self.gridLayout.addWidget(self.g_color, 0, 2, 1, 1)
        self.g_psychological = QtWidgets.QCheckBox(Dialog)
        self.g_psychological.setObjectName("g_psychological")
        self.gridLayout.addWidget(self.g_psychological, 5, 2, 1, 1)
        self.g_adventure = QtWidgets.QCheckBox(Dialog)
        self.g_adventure.setObjectName("g_adventure")
        self.gridLayout.addWidget(self.g_adventure, 5, 1, 1, 1)
        self.g_scifi = QtWidgets.QCheckBox(Dialog)
        self.g_scifi.setObjectName("g_scifi")
        self.gridLayout.addWidget(self.g_scifi, 4, 2, 1, 1)
        self.g_isekai = QtWidgets.QCheckBox(Dialog)
        self.g_isekai.setObjectName("g_isekai")
        self.gridLayout.addWidget(self.g_isekai, 2, 3, 1, 1)
        self.g_seinen = QtWidgets.QCheckBox(Dialog)
        self.g_seinen.setObjectName("g_seinen")
        self.gridLayout.addWidget(self.g_seinen, 6, 3, 1, 1)
        self.g_supernatural = QtWidgets.QCheckBox(Dialog)
        self.g_supernatural.setObjectName("g_supernatural")
        self.gridLayout.addWidget(self.g_supernatural, 6, 0, 1, 1)
        self.g_mecha = QtWidgets.QCheckBox(Dialog)
        self.g_mecha.setObjectName("g_mecha")
        self.gridLayout.addWidget(self.g_mecha, 3, 4, 1, 1)
        self.g_hentai = QtWidgets.QCheckBox(Dialog)
        self.g_hentai.setObjectName("g_hentai")
        self.gridLayout.addWidget(self.g_hentai, 8, 4, 1, 1)
        self.g_harem = QtWidgets.QCheckBox(Dialog)
        self.g_harem.setObjectName("g_harem")
        self.gridLayout.addWidget(self.g_harem, 1, 0, 1, 1)
        self.g_shounenai = QtWidgets.QCheckBox(Dialog)
        self.g_shounenai.setObjectName("g_shounenai")
        self.gridLayout.addWidget(self.g_shounenai, 7, 0, 1, 1)
        self.g_genderbender = QtWidgets.QCheckBox(Dialog)
        self.g_genderbender.setObjectName("g_genderbender")
        self.gridLayout.addWidget(self.g_genderbender, 7, 1, 1, 1)
        self.g_fantasy = QtWidgets.QCheckBox(Dialog)
        self.g_fantasy.setObjectName("g_fantasy")
        self.gridLayout.addWidget(self.g_fantasy, 8, 3, 1, 1)
        self.g_sliceoflife = QtWidgets.QCheckBox(Dialog)
        self.g_sliceoflife.setObjectName("g_sliceoflife")
        self.gridLayout.addWidget(self.g_sliceoflife, 4, 4, 1, 1)
        self.g_romance = QtWidgets.QCheckBox(Dialog)
        self.g_romance.setObjectName("g_romance")
        self.gridLayout.addWidget(self.g_romance, 5, 3, 1, 1)
        self.g_shoujo = QtWidgets.QCheckBox(Dialog)
        self.g_shoujo.setObjectName("g_shoujo")
        self.gridLayout.addWidget(self.g_shoujo, 6, 1, 1, 1)
        self.g_yonkoma = QtWidgets.QCheckBox(Dialog)
        self.g_yonkoma.setObjectName("g_yonkoma")
        self.gridLayout.addWidget(self.g_yonkoma, 2, 1, 1, 1)
        self.g_demons = QtWidgets.QCheckBox(Dialog)
        self.g_demons.setObjectName("g_demons")
        self.gridLayout.addWidget(self.g_demons, 1, 2, 1, 1)
        self.g_thriller = QtWidgets.QCheckBox(Dialog)
        self.g_thriller.setObjectName("g_thriller")
        self.gridLayout.addWidget(self.g_thriller, 8, 0, 1, 1)
        self.g_shounen = QtWidgets.QCheckBox(Dialog)
        self.g_shounen.setObjectName("g_shounen")
        self.gridLayout.addWidget(self.g_shounen, 6, 4, 1, 1)
        self.g_horror = QtWidgets.QCheckBox(Dialog)
        self.g_horror.setObjectName("g_horror")
        self.gridLayout.addWidget(self.g_horror, 8, 1, 1, 1)
        self.g_sports = QtWidgets.QCheckBox(Dialog)
        self.g_sports.setObjectName("g_sports")
        self.gridLayout.addWidget(self.g_sports, 7, 2, 1, 1)
        self.g_martialarts = QtWidgets.QCheckBox(Dialog)
        self.g_martialarts.setObjectName("g_martialarts")
        self.gridLayout.addWidget(self.g_martialarts, 0, 1, 1, 1)
        self.g_heroicfantasy = QtWidgets.QCheckBox(Dialog)
        self.g_heroicfantasy.setObjectName("g_heroicfantasy")
        self.gridLayout.addWidget(self.g_heroicfantasy, 1, 1, 1, 1)
        self.g_vampire = QtWidgets.QCheckBox(Dialog)
        self.g_vampire.setObjectName("g_vampire")
        self.gridLayout.addWidget(self.g_vampire, 0, 3, 1, 1)
        self.g_music = QtWidgets.QCheckBox(Dialog)
        self.g_music.setObjectName("g_music")
        self.gridLayout.addWidget(self.g_music, 4, 1, 1, 1)
        self.g_yaoi = QtWidgets.QCheckBox(Dialog)
        self.g_yaoi.setObjectName("g_yaoi")
        self.gridLayout.addWidget(self.g_yaoi, 9, 4, 1, 1)
        self.g_magic = QtWidgets.QCheckBox(Dialog)
        self.g_magic.setObjectName("g_magic")
        self.gridLayout.addWidget(self.g_magic, 3, 3, 1, 1)
        self.g_mystic = QtWidgets.QCheckBox(Dialog)
        self.g_mystic.setObjectName("g_mystic")
        self.gridLayout.addWidget(self.g_mystic, 4, 0, 1, 1)
        self.g_shoujoai = QtWidgets.QCheckBox(Dialog)
        self.g_shoujoai.setObjectName("g_shoujoai")
        self.gridLayout.addWidget(self.g_shoujoai, 6, 2, 1, 1)
        self.g_samurai = QtWidgets.QCheckBox(Dialog)
        self.g_samurai.setObjectName("g_samurai")
        self.gridLayout.addWidget(self.g_samurai, 5, 4, 1, 1)
        self.g_action = QtWidgets.QCheckBox(Dialog)
        self.g_action.setObjectName("g_action")
        self.gridLayout.addWidget(self.g_action, 9, 1, 1, 1)
        self.g_tragedy = QtWidgets.QCheckBox(Dialog)
        self.g_tragedy.setObjectName("g_tragedy")
        self.gridLayout.addWidget(self.g_tragedy, 7, 4, 1, 1)
        self.g_comedy = QtWidgets.QCheckBox(Dialog)
        self.g_comedy.setObjectName("g_comedy")
        self.gridLayout.addWidget(self.g_comedy, 3, 0, 1, 1)
        self.g_litrpg = QtWidgets.QCheckBox(Dialog)
        self.g_litrpg.setObjectName("g_litrpg")
        self.gridLayout.addWidget(self.g_litrpg, 3, 2, 1, 1)
        self.g_ecchi = QtWidgets.QCheckBox(Dialog)
        self.g_ecchi.setObjectName("g_ecchi")
        self.gridLayout.addWidget(self.g_ecchi, 9, 2, 1, 1)
        self.g_historical = QtWidgets.QCheckBox(Dialog)
        self.g_historical.setObjectName("g_historical")
        self.gridLayout.addWidget(self.g_historical, 2, 4, 1, 1)
        self.g_drama = QtWidgets.QCheckBox(Dialog)
        self.g_drama.setObjectName("g_drama")
        self.gridLayout.addWidget(self.g_drama, 2, 0, 1, 1)
        self.g_mystery = QtWidgets.QCheckBox(Dialog)
        self.g_mystery.setObjectName("g_mystery")
        self.gridLayout.addWidget(self.g_mystery, 1, 3, 1, 1)
        self.g_postapocalyptic = QtWidgets.QCheckBox(Dialog)
        self.g_postapocalyptic.setObjectName("g_postapocalyptic")
        self.gridLayout.addWidget(self.g_postapocalyptic, 5, 0, 1, 1)
        self.g_fiction = QtWidgets.QCheckBox(Dialog)
        self.g_fiction.setObjectName("g_fiction")
        self.gridLayout.addWidget(self.g_fiction, 8, 2, 1, 1)
        self.g_school = QtWidgets.QCheckBox(Dialog)
        self.g_school.setObjectName("g_school")
        self.gridLayout.addWidget(self.g_school, 9, 0, 1, 1)
        self.g_dementia = QtWidgets.QCheckBox(Dialog)
        self.g_dementia.setObjectName("g_dementia")
        self.gridLayout.addWidget(self.g_dementia, 0, 0, 1, 1)
        self.g_superpower = QtWidgets.QCheckBox(Dialog)
        self.g_superpower.setObjectName("g_superpower")
        self.gridLayout.addWidget(self.g_superpower, 7, 3, 1, 1)
        self.g_web = QtWidgets.QCheckBox(Dialog)
        self.g_web.setObjectName("g_web")
        self.gridLayout.addWidget(self.g_web, 0, 4, 1, 1)
        self.g_game = QtWidgets.QCheckBox(Dialog)
        self.g_game.setObjectName("g_game")
        self.gridLayout.addWidget(self.g_game, 2, 2, 1, 1)
        self.g_josei = QtWidgets.QCheckBox(Dialog)
        self.g_josei.setObjectName("g_josei")
        self.gridLayout.addWidget(self.g_josei, 1, 4, 1, 1)
        self.g_yuri = QtWidgets.QCheckBox(Dialog)
        self.g_yuri.setObjectName("g_yuri")
        self.gridLayout.addWidget(self.g_yuri, 9, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStyleSheet("background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.g_parody.setText(_translate("Dialog", "Пародия"))
        self.g_space.setText(_translate("Dialog", "Космос"))
        self.g_color.setText(_translate("Dialog", "В цвете"))
        self.g_psychological.setText(_translate("Dialog", "Психологическое"))
        self.g_adventure.setText(_translate("Dialog", "Приключения"))
        self.g_scifi.setText(_translate("Dialog", "Научная фантастика"))
        self.g_isekai.setText(_translate("Dialog", "Исекай"))
        self.g_seinen.setText(_translate("Dialog", "Сейнен"))
        self.g_supernatural.setText(_translate("Dialog", "Сверхъестественное"))
        self.g_mecha.setText(_translate("Dialog", "Меха"))
        self.g_hentai.setText(_translate("Dialog", "Хентай"))
        self.g_harem.setText(_translate("Dialog", "Гарем"))
        self.g_shounenai.setText(_translate("Dialog", "Сёнен Ай"))
        self.g_genderbender.setText(_translate("Dialog", "Смена пола"))
        self.g_fantasy.setText(_translate("Dialog", "Фэнтези"))
        self.g_sliceoflife.setText(_translate("Dialog", "Повседневность"))
        self.g_romance.setText(_translate("Dialog", "Романтика"))
        self.g_shoujo.setText(_translate("Dialog", "Сёдзе"))
        self.g_yonkoma.setText(_translate("Dialog", "Ёнкома"))
        self.g_demons.setText(_translate("Dialog", "Демоны"))
        self.g_thriller.setText(_translate("Dialog", "Триллер"))
        self.g_shounen.setText(_translate("Dialog", "Сёнен"))
        self.g_horror.setText(_translate("Dialog", "Ужасы"))
        self.g_sports.setText(_translate("Dialog", "Спорт"))
        self.g_martialarts.setText(_translate("Dialog", "Боевые искусства"))
        self.g_heroicfantasy.setText(_translate("Dialog", "Героическое фэнтези"))
        self.g_vampire.setText(_translate("Dialog", "Вампиры"))
        self.g_music.setText(_translate("Dialog", "Музыка"))
        self.g_yaoi.setText(_translate("Dialog", "Яой"))
        self.g_magic.setText(_translate("Dialog", "Магия"))
        self.g_mystic.setText(_translate("Dialog", "Мистика"))
        self.g_shoujoai.setText(_translate("Dialog", "Сёдзе Ай"))
        self.g_samurai.setText(_translate("Dialog", "Самураи"))
        self.g_action.setText(_translate("Dialog", "Экшен"))
        self.g_tragedy.setText(_translate("Dialog", "Трагедия"))
        self.g_comedy.setText(_translate("Dialog", "Комедия"))
        self.g_litrpg.setText(_translate("Dialog", "ЛитRPG"))
        self.g_ecchi.setText(_translate("Dialog", "Этти"))
        self.g_historical.setText(_translate("Dialog", "Исторический"))
        self.g_drama.setText(_translate("Dialog", "Драма"))
        self.g_mystery.setText(_translate("Dialog", "Детектив"))
        self.g_postapocalyptic.setText(_translate("Dialog", "Постапокалиптика"))
        self.g_fiction.setText(_translate("Dialog", "Фантастика"))
        self.g_school.setText(_translate("Dialog", "Школа"))
        self.g_dementia.setText(_translate("Dialog", "Безумие"))
        self.g_superpower.setText(_translate("Dialog", "Супер сила"))
        self.g_web.setText(_translate("Dialog", "Веб"))
        self.g_game.setText(_translate("Dialog", "Игры"))
        self.g_josei.setText(_translate("Dialog", "Дзёсей"))
        self.g_yuri.setText(_translate("Dialog", "Юри"))
