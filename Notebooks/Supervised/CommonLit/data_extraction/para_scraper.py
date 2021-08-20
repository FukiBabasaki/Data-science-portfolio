import requests, re, itertools
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

# Make a request
urls = ['''https://www.gutenberg.org/ebooks/search/?sort_order=downloads&count=100&start_index=''' 
+ i for i in ['''1''', '''26''', '''51''', '''76''', '''101''']]

book_titles = []
book_ids = []

first = True
for url in urls:
    response = requests.get(url)
    books_soup = BeautifulSoup(response.text, 'html.parser')

    tags = books_soup.find_all('a', attrs={'class': 'link'})
    titles = books_soup.find_all('span', attrs={'class': 'title'})

    if first:
        tags = tags[2:]
        titles = titles[2:]
        first = False
    
    book_ids.extend([tag.attrs['href'].split('/')[2] for tag in tags])
    book_titles.extend([title.contents[0].replace('\n', ' ').replace(';', ' ').rstrip() for title in titles])




books = data = pd.DataFrame({
    'title': book_titles,
    'id': book_ids
})

result = []
index = 0
to_remove = []
for id in book_ids:
    response = requests.get('''https://www.gutenberg.org/files/'''+id+'/'+id+ '''-h/'''+id+'''-h.htm''')
    
    if response.status_code == 404:
        to_remove.append(id)
        continue
    
    index += 1

    bs = BeautifulSoup(response.text, 'html.parser')
    ps = bs.find_all('p', attrs={'class': None})

    paragraphs = []
    count = 0
    for p in ps:        
        if len(p.contents) == 1:
            try:
                p_to_add = re.sub(re.compile(r'\s+'), ' ',  p.contents[0])

                if len(p_to_add) < 50:
                    continue
                paragraphs.append(p_to_add)

            except TypeError:
                continue
            count += 1
        elif p.contents[1].name == 'i':
            p_to_add = re.sub(re.compile(r'\s+'), ' ',  p.i.string)
            if len(p_to_add) < 50:
                continue
            paragraphs.append(p_to_add)
            count += 1
        
        if count == 3:
            break
    
    joined_paragraph = "".join(paragraphs)
    if len(joined_paragraph) == 0:
        to_remove.append(id)
        continue

    result.append(joined_paragraph)

data = books.loc[~books['id'].isin(to_remove)]
data['excerpt'] = np.asarray(result)
data.to_csv('dataset/web_scraped.csv')

if __name__ == "__main__":
    pass