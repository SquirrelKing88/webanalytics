from Requests.Requester import Requester


requester = Requester(url="http://google.com")
response = requester.get_request({'q':'ok'})

print(response.data.decode('utf-8'))