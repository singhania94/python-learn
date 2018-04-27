from requests import get
from bs4 import BeautifulSoup


class Author:
    def __init__(self, name, birth, place, bio):
        self.name = name
        self.birth = birth
        self.place = place
        self.bio = bio

    def __repr__(self):
        return f'\nAuthor {self.author} was born on {self.birth} in {self.place} \nBio - {self.bio}\n'


class Quote:
    def __init__(self, quote, author, tags):
        self.quote = quote
        self.author = author
        self.tags = tags

    def __repr__(self):
        return f'\nAuthor {self.author} says {self.quote}\nAssosiated tags - {self.tags}\n'


authors = set()
quotes = set()
base_url = 'http://quotes.toscrape.com'
page_url = ''
crawl = True

while crawl:
    print(f'Sending request to {base_url + page_url}')
    response = get(base_url + page_url)
    print(f'Request to {response.url} has been processed with code {response.status_code} with reason  - '
          f'{response.reason}\n')

    if response.status_code == 200:
        soup_page = BeautifulSoup(response.text, "html.parser")
        soup_quotes = soup_page.select('.quote')

        for soup_quote in soup_quotes:
            text = soup_quote.find(class_='text').get_text()
            author_name = soup_quote.find(class_='author').get_text()
            author_ref = soup_quote.find('a').get('href')
            soup_tags = soup_quote.select('.tag')
            tags = []
            for soup_tag in soup_tags:
                tags.append(soup_tag.get_text())
            q = Quote(text, author_name, tags)
            print(f'Formed quote object {q}')
            quotes.add(q)

            print(f'Sending request to {base_url + author_ref}')
            response = get(base_url + author_ref)
            print(f'Request to {response.url} has been processed with code {response.status_code} with reason  - '
                  f'{response.reason}\n')

            soup_author = BeautifulSoup(response.text, 'html.parser')
            print(soup_author)
        crawl = False
    else:
        break
