import requests
print("hello")
link = "https://www.makemytrip.com"
html = requests.get(link, params=None)
print(html.text)
print(type(html))

# https://www.makemytrip.com/flight/search?itinerary=DEL-BLR-01/06/2019&tripType=O&paxType=A-1_C-0_I-0&intl=false&=&cabinClass=E