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
author_ref_url = ''
crawl = True

while crawl:
    print(f'\nSending request to {base_url + page_url}')
    response = get(base_url + page_url)
    print(f'Request to {response.url} has been processed with code {response.status_code} with reason  - '
          f'{response.reason}\n')

    if response.status_code == 200:
        soup_page = BeautifulSoup(response.text, "html.parser")
        soup_quotes = soup_page.select('.quote')

        for soup_quote in soup_quotes:
            text = soup_quote.find(class_='text').get_text()
            author_name = soup_quote.find(class_='author').get_text()
            author_ref_url = soup_quote.find('a').get('href')
            soup_tags = soup_quote.select('.tag')
            tags = []
            for soup_tag in soup_tags:
                tags.append(soup_tag.get_text())

            q = Quote(text, author_name, tags)
            print(f'Formed quote object {q}')
            quotes.add(q)

            print(f'Sending request to {base_url + author_ref_url}')
            response = get(base_url + author_ref_url)
            print(f'Request to {response.url} has been processed with code {response.status_code} with reason  - '
                  f'{response.reason}\n')

            if response.status_code == 200:
                soup_author = BeautifulSoup(response.text, 'html.parser')
                name = soup_author.find(class_='author-title').get_text()
                birth = soup_author.find(class_='author-born-date').get_text()
                place = soup_author.find(class_='author-born-location').get_text()
                bio = soup_author.find(class_='author-description').get_text()

                a = Author(name, birth, place, bio)
                print(f'Formed author object {a}')
                authors.add(a)

        soup_next = soup_page.find(class_='next')
        if soup_next is not None:
            page_url = soup_next.find('a').get('href')
        else:
            print('Could not find the next page to crawl. Ending the adventure here.')
            crawl = False
    else:
        print(f'Could not find or Error loading the specified url - {base_url + page_url}. '
              f'Received status - {response.status_code}.\n'
              f'Ending the adventure here.')
        crawl = False
