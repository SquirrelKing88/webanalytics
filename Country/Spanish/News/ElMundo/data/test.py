from Country.Spanish.News.ElMundo.data.NewsScraper import NewsScraper
from Requests.Requester import Requester


html = NewsScraper.get_page_data(root_url='https://www.efe.com/efe/espana/', page=1)
print(html)
