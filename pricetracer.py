import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
url = "https://www.amazon.in/dp/B0BBQGVNNZ/ref=QAHzEditorial_en_IN_1?pf_rd_r=WEN2BNARJ2X76XPHABHX&pf_rd_p=01e7c1aa-9dee-4d1c-91f4-af294e3fc2ff&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-8&pf_rd_t=&pf_rd_i=2563504031"
headers = {"<span class=\"a-price a-text-price a-size-medium apexPriceToPay\" data-a-size="b" data-a-color=\"price\"><span class=\"a-offscreen\">₹3,994.00</span><span aria-hidden=\"true\">₹3,994.00</span></span>"}

def check_price(url, headers):
    page = requests.get(url , headers= headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    print(title.strip())
    
    try:
        price = soup.find(id="priceblock_ourprice").get_text()
        print(price.strip())
    except AttributeError:
        print("price = _")

    try:
        price = soup.find(id="priceblock_dealprice").get_text()
        print(price.strip())
    except AttributeError:
        print("price = _")

    price = list(price)
    price[3] = '.'

    conv_price = float("".join(price[2:7]))
    print(conv_price)

    if(conv_price < 1.899):
        sendsms()

def sendsms():
    client = Client('AXXXXXXXXXXXXXXXXXXXXXXXX', '1XXXXXXXXXXXXXXXXXXXXXXX')
    client.messages.create(to = '+91XXXXXXXXXX', from_ = '+1XXXXXXXXXX', body = 'Price reduced: https://www.amazon.in/United-Colors-Benetton-Mens-Sneakers/dp/B0792DDS9C/ref=pd_sbs_309_41?_encoding=UTF8&pd_rd_i=B0792DDS9C&pd_rd_r=37f5a38e-7aec-4629-a13c-e0275af08fe8&pd_rd_w=UmPpQ&pd_rd_wg=TNla8&pf_rd_p=5c023088-3bf1-437a-ba7d-b879da18a58e&pf_rd_r=0HT9K76XMP84AZY2A5Y7&refRID=0HT9K76XMP84AZY2A5Y7')

check_price(url, headers)



    
    
    
    
    