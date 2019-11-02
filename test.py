import requests
from json import loads
from train import Train

uri = 'http://developer.itsmarta.com/RealtimeTrain/RestServiceNextTrain/GetRealtimeArrivals?apikey=3198e5fa-9787-418f-8d66-8ec1a0b52c38'


response = loads(requests.get(uri).text)
trains = [Train(resp) for resp in response]

for train in trains:
    print(train)
