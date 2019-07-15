import dateutil.parser
from ._articles import Article, Source, get_pyquery_from_url
import re


class CrowdStrike(Source):
    base_url = "https://www.crowdstrike.com"
    blog_url = '{0}/blog/category/threat-intel-research'.format(base_url)

    @classmethod
    def get_page(cls, page):
        url = '{0}/page/{1}/'.format(cls.blog_url, page)
        content = get_pyquery_from_url(url)
        return [link.attr('href').lower().strip() for link in content('.blog-entry-title > a').items()]

    @classmethod
    def get_latest(cls, ):
        content = get_pyquery_from_url(cls.blog_url)
        return [link.attr('href').lower().strip() for link in content('.blog-entry-title > a').items()]

    @classmethod
    def get_page_count(cls, ):
        content = get_pyquery_from_url(cls.blog_url)
        pages = [li('a').text() for li in content('ul.page-numbers > li').items()]
        return max([int(page) for page in pages if len(page) > 0])

    class CrowdStrikeArticle(Article):
        def __init__(self, url):
            super().__init__(url)
            self.publisher = 'CrowdStrike'
            article = self.page('article')
            self.content = article.html()
            self.title = article('.single-blog-header > .single-post-title').text().strip()
            self.published = dateutil.parser.parse(article('.meta-date > time.updated').attr.datetime)
            # parse authors
            authors = article('.meta-author > .author > span > a').text()
            authors = [author.strip() for author in re.split(r'(,\s|\sand\s)', authors)]
            self.authors = [author for author in authors if not(author == ',' or author == 'and')]
