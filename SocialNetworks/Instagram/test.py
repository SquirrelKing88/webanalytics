from Requests.InfinityRequester import InfinityRequester

from LanguageProcessing.Translation.GoogleTranslator import GoogleTranslator
from Requests.Requester import Requester
from selenium import webdriver


translator = GoogleTranslator()

# today news https://www.pravda.com.ua/news/
url = "https://www.instagram.com/m.malkin"


requester = InfinityRequester(url=url, parent_element='article', parent_element_classes=['FyNDV'], child_element='div', child_element_classes=['v1Nh3', 'kIKUG',  '_bz0w'])

result = requester.make_get_request()
print(list(result.keys()))


first_link =url + list(result.keys())[0]

# requester = Requester(url=first_link, retries=5, sleep_time=3)
# response = requester.make_get_request()
# html = response.data
#
# print(html)

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x400')  # optional

browser = webdriver.Chrome(executable_path='C:\\Users\\teres\\PycharmProjects\\webanalytics\\Requests\\drivers\\chromedriver_win', chrome_options=options)

# loop here

for link in list(result.keys()):
    browser.get(link)

    html = browser.page_source

    # TODO parse html

    print(html)

# # step 1. Read all page with taday's news
# requester = Requester(url=url, retries=5, sleep_time=3)
# response = requester.make_get_request()
# html = response.data
#
# # step 2. Create half empty dataset with parsed urls of articles
# dataset = PostsScraper.parse_posts_list(url_root=requester.get_url_root(),html=html, soup=None)
# print(dataset)
# # step 3. Loop over all urls and scrape article data
# for url in list(dataset):
#
#     # make new request to upload article data
#     requester = Requester(url=url, retries=5)
#     response = requester.make_get_request()
#     html = response.data
#
#
#
#     # load html into soup
#     soup = BeautifulSoup(html, 'html.parser')
#     date = PostsScraper.parse_article_datetime(html=html, soup=soup, year=2019, month=1, day=29)
#     dataset[url]["html"] = PostsScraper.parse_article_text(html=html, soup=soup)
#     dataset[url]['date'] = date
#     dataset[url]['posts']['user'] = PostsScraper.parse_posts_users(html=html, soup=soup)
#     dataset[url]['posts']['hashtags'] = PostsScraper.parse_post_hashtags(html=html, soup=soup)
#     dataset[url]['posts']['text'] = PostsScraper.parse_post_text(html=html, soup=soup)
#     dataset[url]['posts']['receivers'] = PostsScraper.parse_posts_receivers(html=html, soup=soup)
#     translation_result = translator.get_translation(dataset[url]["text"])
#     dataset[url]['posts']['translation_en'] = translation_result['translation']
#
#
# # step 4. Save dataset to folder
# #writer = FileWriter("data/posts.json")
# #writer.write(dataset)
# #print(dataset)