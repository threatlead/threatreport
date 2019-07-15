import requests
from pyquery import PyQuery


def get_pyquery_from_url(url):
    page = requests.get(url)
    page.raise_for_status()
    return PyQuery(page.content)


class Article:
    """
    Base class for articles
    """
    def __init__(self, url):
        self.url = url
        self.page = get_pyquery_from_url(url=self.url)
        self.content = None
        self.published = None
        self.title = None
        self.publisher = None
        self.authors = []


class Source:
    base_url = None
    blog_url = None

    @classmethod
    def get_page(cls, page):
        pass

    @classmethod
    def get_latest(cls, ):
        pass

    @classmethod
    def get_page_count(cls, ):
        pass
