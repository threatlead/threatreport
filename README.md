# Threat Reports Scraper

## Usage

### Get Latest

```python
links = securelist.Securelist.get_latest()
print(links)
```

```javascript
[
    'https://securelist.com/new-finspy-ios-and-android-implants-revealed-itw/91685/',
    'https://securelist.com/twas-the-night-before/91599/',
    'https://securelist.com/sodin-ransomware/91473/',
    ...
]
```

### Get Article

```python
article = securelist.Securelist.SecurelistArticle(url=links[0])
print(vars(article))
```

```javacript
{
  'url': 'https://securelist.com/new-finspy-ios-and-android-implants-revealed-itw/91685/',
  'content': '\n\n\t<div class="columnwrapper content-list-section">...</div>\n\n\t</div>\n\n', 
  'published': datetime.datetime(2019, 7, 10, 10, 0, 23, tzinfo=tzutc()),
  'title': 'New FinSpy iOS and Android implants revealed ITW', 
  'publisher': 'Kaspersky',
  'authors': ['GReAT', 'AMR']
}
```