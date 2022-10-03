import requests  #pip install requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4
from pytz import timezone as tz # pip install pytz
from datetime import datetime as date 

timezone = tz('Africa/Addis_Ababa')  # set the timezone

def get_currency():
    """This functions scraps the latest exchange rate information from official page of
    The National Bank of Ethiopia.

    Returns:
        dictionary: {
            'time': 'Time Date stamp GMT+3'
            'currency_name': [buying_value, selling_value],
            'currency_name2': [buying_value, selling_value],
            ...
        }
    """
    time = date.now(timezone).strftime("%d/%m/%Y %H:%M:%S")
    url = "https://market.nbebank.com/market/banks/index.php"
    page = requests.get(url)

    exchange_rates = {'time': time}  # format currency: [buy, sell]
    soup = BeautifulSoup(page.content, 'html.parser')

    tables = soup.find_all('table')[3:]
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            name = ""
            buy_sell = []
            datas = row.find_all('td')
            name = datas[1].text.strip()
            buy_sell.append(datas[2].text.strip())
            buy_sell.append(datas[-1].text.strip())
            exchange_rates[name] = buy_sell
    return exchange_rates

