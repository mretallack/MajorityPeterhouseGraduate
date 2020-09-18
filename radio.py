import requests
from requests.auth import HTTPBasicAuth

radio="10.0.0.86"

url="http://"+radio+"/play_url?id=8_1"


r =requests.get(url, auth=HTTPBasicAuth('su3g4go6sk7', 'ji39454xu/^'))

print(r.text)


url="http://"+radio+"/play_stn?id=8_1"


r =requests.get(url, auth=HTTPBasicAuth('su3g4go6sk7', 'ji39454xu/^'))

print(r.text)



