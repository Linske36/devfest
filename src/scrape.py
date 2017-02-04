from bs4 import BeautifulSoup, SoupStrainer
import requests

def get_orders():

    response = requests.get('https://www.whitehouse.gov/briefing-room/presidential-actions/executive-orders')  
    
    print response.content

    for order in BeautifulSoup(response.content, parse_only=SoupStrainer('a')):
        if order.has_attr('href'):
            print order['href']     
