import requests
def get_stock():
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
    data=requests.get(url)
    if data.status_code==200:
        res=data.json()
        return res
    else:
        return None
ans=get_stock()
print(ans['Time Series (5min)'])