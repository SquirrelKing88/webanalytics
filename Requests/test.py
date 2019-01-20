from Requests.Requester import Requester


requester = Requester(url="http://google.com")
response = requester.get_request({'q':'ok'})

print(response.data.decode('utf-8'))


requester = Requester(url="http://vk.com", proxy="138.201.223.250")
response = requester.get_request()
print(response.data.decode('utf-8'))
