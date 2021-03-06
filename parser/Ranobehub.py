from const.urls import URL_RANOBEHUB_API, DEFAULT_HEADERS
from items import RequestForm, Manga
from parser.Parser import Parser
from utils import get_html


class Ranobehub(Parser):
    catalog_name = 'Ranobehub'

    def __init__(self):
        self.url_api = URL_RANOBEHUB_API
        self.headers = DEFAULT_HEADERS
        self.catalog_id = 4

    def get_manga(self, manga: Manga) -> Manga:
        url = f'{self.url_api}/ranobe/{manga.id}'
        html = get_html(url, self.headers)
        if html and html.status_code == 200 and html.json():
            manga.description = html.json().get('data').get('description')
        return manga

    def search_manga(self, params: RequestForm):
        url = f'{self.url_api}/search'
        params = {'title-contains': params.search, 'page': params.page}
        html = get_html(url, self.headers, params)
        manga = []
        if html and html.status_code == 200 and html.json():
            for i in html.json().get('resource'):
                manga_id = i.get('id')
                name = i.get('names').get('eng')
                russian = i.get('names').get('rus')
                score = i.get('rating')
                manga.append(Manga(manga_id, self.catalog_id, name, russian, "ranobe", '', score))
        return manga

    def get_preview(self, manga: Manga):
        url = f'{self.url_api}/ranobe/{manga.id}'
        html = get_html(url, self.headers)
        if html and html.status_code == 200 and html.json():
            img = html.json().get('data').get('posters').get('big')
            return get_html(img)
