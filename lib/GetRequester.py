import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        request_list= []
        request_items = json.loads(self.get_response_body())
        for item in request_items:
            request_list.append(item)
        return request_list
