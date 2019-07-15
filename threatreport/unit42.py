import dateutil.parser
import re
from ._articles import Article, Source, get_pyquery_from_url


class Unit42(Source):
    base_url = 'https://unit42.paloaltonetworks.com'
    blog_url = '{0}/wp-admin/admin-ajax.php?action=news_infinite&data%5Boffset%5D='.format(base_url)

    @classmethod
    def get_page(cls, page):
        url = '{0}{1}'.format(cls.blog_url, page * 15)
        content = get_pyquery_from_url(url)
        links = []
        for match in re.findall(r'<a\s+href="\\&quot;([^\s]*?)\\&quot;"\s+data-page-track="', content.html()):
            links.append(match.replace('\/', '/'))
        return links

    @classmethod
    def get_latest(cls, ):
        return cls.get_page(page=0)

    @classmethod
    def get_page_count(cls, ):
        return 255

    class Unit42Article(Article):
        def __init__(self, url):
            super().__init__(url)
            self.publisher = 'Palo Alto Networks'
            article = self.page('article')
            self.content = article.html()
            self.title = article('header.news-header > .container > .row > div > h1').text().strip()
            self.published = dateutil.parser.parse(article('div > .container > div > div > p > time').attr.datetime)
            self.authors = [author.text().strip() for author in article('a.author').items()]
