import dateutil.parser
from ._articles import Article, Source, get_pyquery_from_url


class Securelist(Source):
    base_url = 'https://securelist.com'
    blog_url = '{0}/all/'.format(base_url)

    @classmethod
    def get_page(cls, page=0):
        url = cls.blog_url if page == 0 else '{0}/page/{1}/'.format(cls.blog_url, page)
        content = get_pyquery_from_url(url)
        return [link.attr('href').lower().strip() for link in content('h3.entry-title > a').items()]

    @classmethod
    def get_latest(cls, ):
        return cls.get_page(page=0)

    @classmethod
    def get_page_count(cls, ):
        return 255

    class SecurelistArticle(Article):
        def __init__(self, url):
            super().__init__(url)
            self.publisher = 'Kaspersky'
            article = self.page('article')
            self.content = article.html()
            self.title = article('header.entry-header > .title-wrap > h1').text().strip()
            self.published = dateutil.parser.parse(article('.entry-meta > .entry-author > time').attr.datetime)
            self.authors = [author.text().strip() for author in article('.entry-meta > .entry-author > a').items()]