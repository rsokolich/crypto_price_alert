from requests import Request, Session, post
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import datetime
import time
import config

# Enter comma delimited symbols on which you wish to alert:
param_symbols = 'BTC,ETH,LTC,XRP,BCH,BSV,LINK'

# Enter fiat currency to which you wish to convert:
param_conversion = 'USD'

# Enter percentage change on which you wish to alert:
percentage_change_negative = (-5.0)
percentage_change_positive = (5.0)


# Function to action the above inputs:
def cryptoPriceQuery(param_symbols):

    parameters = {
        'symbol': param_symbols,
        'convert': param_conversion
        }

    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': config.cmc_key
    }

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    session = Session()
    session.headers.update(headers)

    loop_symbols = param_symbols.split(",")
    
    while True:        
        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)        
            for symbol in loop_symbols:
                percent_change_1h = data['data'][symbol]['quote']['USD']['percent_change_1h']
                if (float(percent_change_1h) <= (percentage_change_negative)) or (float(percent_change_1h) >= (percentage_change_positive)):                    
                    name = data['data'][symbol]['name']
                    price = data['data'][symbol]['quote']['USD']['price']                    
                    ifttt_webhook_url = 'https://maker.ifttt.com/trigger/%s/with/key/%s?value1=%s&value2=%s%%&value3=$%s' % (config.ifttt_alert_name, config.ifttt_alert_key, name, percent_change_1h, price)
                    print ("%s \t name = %s \t 1h Percentage Change = %s \t $%s \t %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name, percent_change_1h, price, post(ifttt_webhook_url)))
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
        time.sleep(300)

cryptoPriceQuery(param_symbols)




