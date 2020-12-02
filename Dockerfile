FROM python:3-alpine
COPY . /apps
WORKDIR /apps
RUN pip install -r requirements.txt
CMD ["python","-u","crypto_price_alert.py"]