# crypto_price_alert

### App to query pro-api.coinmarketcap.com's API and alert on crypto price swings via IFTTT.

###### How to run the app:
    1. Rename config_sample.py to config.py
    2. Add config.py to .gitignore, as it will contain secrets 
    3. In config.py, enter the following:
        a. cmc_key
        b. ifttt_alert_name
        c. ifttt_alert_key 
    
    4. In crypto_price_alert:
        a. Input comma delimited crypto symbols (param_symbols)
        b. Input fiat currency to which you wish to convert (param_conversion)
        c. Input one hour percentage variance on which you wish to alert (percentage_change_negative, percentage_change_positive)

**Note:** the default query time is every 5 minutes, remaining within coinmarketcap's free basic plan for API calls. This can be modified in the cryptoPriceQuery function.


###### How to run app as a Docker container:
    1. Create an /apps/crypto_price_alert directory on your Docker host and copy Dockerfile, crypto_price_alert.py, config.py and requirements.txt
    2. Create an image:
        sudo docker build -t rsokolich/crypto_price_alert /apps/crypto_price_alert
    3. Create a container:
        sudo docker create --name crypto_price_alert -p 5010:5010 rsokolich/crypto_price_alert
    4. Start the container:
        sudo docker start crypto_price_alert
