import requests
from bs4 import BeautifulSoup

FEAR_AND_GREED_URL = "https://edition.cnn.com/markets/fear-and-greed"
FEAR_AND_GREED_PHRASE = "Fear &amp; Greed Now: "
FEAR_THRESHOLD = 20
GREED_THRESHOLD = 80

r = requests.get(FEAR_AND_GREED_URL)

html = r.content

soup = BeautifulSoup(html)

div = soup.findAll(id='needleChart')

div = str(div[0])

position = div.find(FEAR_AND_GREED_PHRASE)

position = position + len(FEAR_AND_GREED_PHRASE)

current_fear_and_greed_index = int(div[position:position+3].strip())

print(current_fear_and_greed_index)


others_are_greedy = current_fear_and_greed_index >= GREED_THRESHOLD
others_are_fearful = current_fear_and_greed_index <= FEAR_THRESHOLD

if others_are_greedy:
    # sell sell sell
    pass

if others_are_fearful:
    # buy buy buy
    pass
