from Requests.Requester import Requester


requester = Requester(url="http://google.com")
response = requester.make_get_request({'q': 'ok'})

html = response.get_data()
status = response.get_status()
print("Status {0}\nData {1}".format(status, html))




requester = Requester(url="https://www.instagram.com/p/BtRzmCkA2sT/", run_html=True)
response = requester.make_get_request()

html = response.get_data()
status = response.get_status()
print("Status {0}\nData {1}".format(status, html))