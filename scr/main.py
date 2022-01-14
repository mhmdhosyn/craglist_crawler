import sys
# import requests
#
# from bs4 import BeautifulSoup
#
from crawl import LinkCrawler
#
#
# def get_page(url, start=0):
#     try:
#         response = requests.get(url + str(start))
#     except:
#         return None
#     # print(response.status_code, response.url)
#     return response
#
#
# def find_links(html_doc):
#     soup = BeautifulSoup(html_doc, 'html.parser')
#     # content = soup.find('div', attrs={'class': 'content'})
#     # adv_list = soup.find_all('li', attrs={'class': 'result-row'})
#     return soup.find_all('a', attrs={'class': 'hdrlnk'})
#
#
# def start_crawl_city(url):
#     start = 0
#     crawl = True
#     adv_links = list()
#     while crawl:
#         response = get_page(url, start)
#         if response is None:
#             crawl = False
#             continue
#         new_links = find_links(response.text)
#         adv_links.extend(new_links)
#         start += 120
#         crawl = bool(len(new_links))
#
#     return adv_links
#
#
# def start_crawl():
#     cities = ['paris', 'berlin', 'amsterdam', 'munich']
#     link = 'https://{}.craigslist.org/search/hhh?availabilityMode=0&lang=en&cc=gb&s='
#     for city in cities:
#         links = start_crawl_city(link.format(city))
#         print(f'{city} total: {len(links)}')


def get_pages_data():
    raise NotImplementedError()


if __name__ == "__main__":
    switch = sys.argv[1]
    if switch == 'find_links':
        crawler = LinkCrawler(cities=['paris', 'berlin', 'amsterdam', 'munich'])
        crawler.start()
    elif switch == 'extract_pages':
        get_pages_data()

