from Country.Spanish.News.Efe.NewsScraper import NewsScraper
from Requests.Requester import Requester
from Scraper.Writters.FileWritter import FileWriter

url = 'https://www.efe.com/efe/espana/'

html = NewsScraper.get_page_data(root_url='https://www.efe.com/efe/espana/', page=1)
requester = Requester(url=url, retries=5, sleep_time=3)
response = requester.make_get_request()


dataset = NewsScraper.parse_articles_list(url_root=requester.get_url_root(), html=html)

writer = FileWriter('news.csv')
for data in dataset:
    print('DATA', data)
    writer.write(data)
