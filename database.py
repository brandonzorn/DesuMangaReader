import os
import sqlite3

from const import lib_lists_en
from items import Chapter, Image, Manga
from static import singleton


@singleton
class Database:
    def __init__(self):
        self.__wd = os.getcwd()
        if not os.path.exists(f'{self.__wd}/Desu/data.db'):
            os.makedirs(f'{self.__wd}/Desu', exist_ok=True)
        self.__con = sqlite3.connect(f'{self.__wd}/Desu/data.db', check_same_thread=False)
        self.__cur = self.__con.cursor()
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS manga (id STRING PRIMARY KEY ON CONFLICT REPLACE NOT NULL,
        name STRING, russian STRING, kind STRING, description TEXT, score FLOAT, catalog_id INTEGER);""")
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS chapters (id STRING PRIMARY KEY ON CONFLICT REPLACE NOT NULL,
        vol STRING, ch STRING, title STRING, manga_id INTEGER, index_n INTEGER);""")
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS images (id STRING PRIMARY KEY ON CONFLICT REPLACE NOT NULL,
        page INTEGER, width INTEGER, height INTEGER, img STRING, chapter_id INTEGER);""")
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS library (id STRING PRIMARY KEY ON CONFLICT REPLACE NOT NULL,
        list STRING)""")
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS chapter_history
        (chapter_id STRING PRIMARY KEY ON CONFLICT REPLACE NOT NULL, manga_id STRING NOT NULL, is_completed BOOLEAN)""")
        self.__con.commit()

    def add_manga(self, manga: Manga):
        self.__cur.execute("INSERT INTO manga VALUES(?, ?, ?, ?, ?, ?, ?);",
                           (manga.id, manga.name, manga.russian, manga.kind, manga.description,
                            manga.score, manga.catalog_id))
        self.__con.commit()

    def add_chapter(self, chapter: Chapter, manga: Manga, index: int):
        self.__cur.execute("INSERT INTO chapters VALUES(?, ?, ?, ?, ?, ?);",
                           (chapter.id, chapter.vol, chapter.ch, chapter.title, manga.id, index))
        self.__con.commit()

    def get_chapters(self, manga: Manga) -> list:
        a = self.__cur.execute(f"SELECT * FROM chapters WHERE manga_id = '{manga.id}' ORDER by index_n").fetchall()
        return [Chapter({'id': i[0], 'vol': i[1], 'ch': i[2], 'title': i[3]}) for i in a[::-1]]

    def add_image(self, image: Image, chapter: Chapter):
        self.__cur.execute("INSERT INTO images VALUES(?, ?, ?, ?, ?, ?);",
                           (image.id, image.page, image.width, image.height, image.img, chapter.id))
        self.__con.commit()

    def get_images(self, chapter: Chapter) -> list:
        a = self.__cur.execute(f"SELECT * FROM images WHERE chapter_id = '{chapter.id}' ORDER by page").fetchall()
        return [Image({'id': i[0], 'page': i[1], 'width': i[2], 'height': i[3], 'img': i[4]}) for i in a]

    def add_manga_library(self, manga: Manga, lib_list: str = "planned"):
        self.__cur.execute(f"INSERT INTO library VALUES(?, ?);", (manga.id, lib_list))
        self.__con.commit()

    def get_manga_library(self, lib_list) -> [Manga]:
        a = self.__cur.execute(f"SELECT id FROM library WHERE list = '{lib_list}';").fetchall()
        manga = []
        for i in a[::-1]:
            x = self.__cur.execute(f"SELECT * FROM manga WHERE id = '{i[0]}'").fetchall()[0]
            manga.append(Manga({'id': x[0], 'name': x[1], 'russian': x[2], 'kind': x[3],
                                'description': x[4], 'score': x[5], 'catalog_id': x[6]}))
        return manga

    def check_manga_library(self, manga: Manga):
        a = self.__cur.execute(f"SELECT list FROM library WHERE id = '{manga.id}';").fetchall()
        if a and a[0][0] in lib_lists_en:
            return a[0][0]

    def rem_manga_library(self, manga: Manga):
        self.__cur.execute(f"DELETE FROM library WHERE id = '{manga.id}';")
        self.__con.commit()

    def set_complete_chapter(self, manga: Manga, chapter: Chapter, is_completed: bool):
        self.__cur.execute(f"INSERT INTO chapter_history VALUES(?, ?, ?);", (chapter.id, manga.id, is_completed))
        self.__con.commit()

    def del_complete_chapter(self, chapter: Chapter):
        self.__cur.execute(f"DELETE FROM chapter_history WHERE chapter_id = '{chapter.id}';")
        self.__con.commit()

    def check_complete_chapter(self, chapter: Chapter):
        a = self.__cur.execute(
            f"SELECT is_completed FROM chapter_history WHERE chapter_id = '{chapter.id}';").fetchall()
        return bool(a)

    def get_complete_status(self, chapter: Chapter):
        a = self.__cur.execute(
            f"SELECT is_completed FROM chapter_history WHERE chapter_id = '{chapter.id}';").fetchall()
        return bool(a[0][0])

    def get_chapters_history(self):
        chapters = []
        a = self.__cur.execute(f"SELECT chapter_id FROM chapter_history;").fetchall()
        for i in a:
            ch = self.__cur.execute(f"SELECT * FROM chapters WHERE id = '{i[0]}'").fetchone()
            chapters.append(Chapter({'id': ch[0], 'vol': ch[1], 'ch': ch[2], 'title': ch[3]}))
        return chapters
