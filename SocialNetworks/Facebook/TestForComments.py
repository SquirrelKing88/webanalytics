from bs4 import BeautifulSoup
import pickle
from Requests.InfinityScroller import InfinityScroller
from Requests.WebBrowser.SiteRegistration.CookieRegistration import CookieRegistration
from Requests.WebBrowser.WebAction.ActionScroll import ActionScroll


my_page = "https://www.facebook.com/permalink.php?story_fbid=449430805456555&id=100011689171425"
facebook = "https://www.facebook.com"

list_of_url = [my_page]
dataset = dict()

for url in list_of_url:

    cookies = pickle.load(open("config/cookies.pkl", "rb"))
    registration = CookieRegistration(url="https://www.facebook.com/", cookies=cookies)
    scroll_action = ActionScroll()
    scroller = InfinityScroller(url=my_page, actions=[scroll_action], scroll_pause=2,registration=registration)
    html = scroller.scroll()
    while html is not None:
        html = scroller.scroll()
        soup = BeautifulSoup(html, features="html.parser")
        div_main = soup.find_all('div', {'data-testid':'UFI2Comment/root_depth_0'})

        dataset[url] = dict()
        dataset[url]['post_url'] = url
        #dataset[url]['html'] = html

        for element in div_main:
            text = element.find('span').text
            author = element.img['alt']
            author_url = facebook + element.a['href']
            datetime = element.abbr['title']

            dataset[url]['datetime'] = datetime
            dataset[url]['author'] = author
            dataset[url]['author_url'] = author_url
            dataset[url]['text'] = text

        div_reaction = soup.find_all('span',{'data-testid':"UFI2CommentTopReactions/tooltip"})
        for el in div_reaction:
            reaction = el.a['href']
            reaction = facebook + reaction

            dataset[url]['reaction'] = reaction
            #dataset[url]['translation_en'] = translation_en
print(dataset)

