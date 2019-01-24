from Requests.Requester import Requester


requester = Requester(url="http://google.com")
response = requester.make_get_request({'q': 'ok'})

print(response.data.decode('utf-8'))


requester = Requester(url="http://vk.com", proxy="87.181.249.204")
response = requester.make_get_request()
print(response.data.decode('utf-8'))
