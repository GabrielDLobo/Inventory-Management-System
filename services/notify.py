import requests


class Notify:
    
    def __init__(self):
        self.__base__url = 'http://localhost:8001'
    
    def send_order_event(self, data):
        requests.post(
            url=f'{self.__base_url}''/api/V1/webhooks/order/',
            json=data,
        )
