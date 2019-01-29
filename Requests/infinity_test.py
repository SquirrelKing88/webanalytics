from Requests.InfinityRequester import InfinityRequester

url = 'https://www.instagram.com/yulia_chornenko/'

requester = InfinityRequester(url =url, parent_element='article', parent_element_classes=['FyNDV'],child_element='div',child_element_classes=['v1Nh3', 'kIKUG',  '_bz0w'])

result = requester.make_get_request()

print(result.keys())