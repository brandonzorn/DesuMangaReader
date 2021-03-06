import contextlib
import json
import os

import requests

from const.icons import ru_icon_path, gb_icon_path, jp_icon_path
from const.lists import lib_lists_en, lib_lists_ru
from const.urls import DEFAULT_HEADERS
from items import Manga, Chapter, Image


def get_html(url: str, headers: dict = DEFAULT_HEADERS, params=None):
    response = requests.Response()
    try:
        response = requests.get(url, headers=headers, params=params)
    except Exception as e:
        print(e)
        print(url)
        print(params)
        response.status_code = 0
    finally:
        return response


def get_lib_list_en(lib_list_ru):
    return lib_lists_en[lib_lists_ru.index(lib_list_ru)]


def get_language_icon(language: str):
    match language:
        case 'ru':
            return ru_icon_path
        case 'en':
            return gb_icon_path
        case 'jp':
            return jp_icon_path
        case _:
            return ''


def get_url(manga: Manga, chapter: Chapter = None, image: Image = None):
    url = f'https://desu.me/manga/api/'
    url += f'/{manga.id}'
    if chapter:
        url += f'/chapter/{chapter.id}'
        if image:
            return f'{os.getcwd()}/Desu/images/{manga.id}/{chapter.id}/{image.page}.jpg'
    return url


def singleton(cls):
    instance = [None]

    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]
    return wrapper


def with_lock_thread(locker):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with locker:
                return func(*args, **kwargs)
        return wrapper
    return decorator


@contextlib.contextmanager
def lock_ui(ui_to_lock: list):
    [i.setEnabled(False) for i in ui_to_lock]
    yield
    [i.setEnabled(True) for i in ui_to_lock]


def token_saver(token, catalog_name='Shikimori'):
    if not os.path.exists(f'Desu/{catalog_name}'):
        os.makedirs(f'Desu/{catalog_name}', exist_ok=True)
    with open(f'Desu/{catalog_name}/token.json', 'w') as f:
        f.write(json.dumps(token))


def token_loader(catalog_name):
    path = f'Desu/{catalog_name}'
    if os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        if os.path.exists(f'{path}/token.json'):
            with open(f'{path}/token.json') as f:
                data = json.load(f)
                if data:
                    return data
    return {}
