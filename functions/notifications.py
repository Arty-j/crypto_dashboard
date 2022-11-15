import datetime
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import sqlalchemy as sql
import questionary
#from Modules import data as data_utils


def choose_coin(top_ten_coin_list):
    coin_id = questionary.checkbox('''Here is a list of the top ten cryoptocurrency coins by market cap. 
    Please choose a coin.''', choices=top_ten_coin_list).ask()
    return coin_id

def get_coin_data (coin_id):
    start_time = 1641042000 #2022-01-01 1pmGMT
    end_time = 1668208735 #now
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart/range?vs_currency=usd&from={start_time}&to={end_time}"
    response = requests.get(url)
    data = response.json()
    
    timestamp_list = []
    price_list = []
    
    for row in data['prices'] :
        timestamp_list.append(datetime.datetime.fromtimestamp(row[0]/1000))
        price_list.append(row[1])
        
    raw_data = {'timestamp': timestamp_list, 'price' : price_list}
    df = pd.DataFrame(raw_data, columns=['timestamp','price'])
    pd.options.display.float_format = '{:.2f}'.forma
    df = df.set_index('timestamp')
    print(df)
    return coin_id, df
    
    
# def indicators (coin_df, coin_id):
#     coin_price_df = coin_df["price"]

#     plt.title(coin_id + ' Daily Price for 2022')
#     plt.xlabel('Timestamp')
#     plt.ylabel('Daily Prices in USD')
#     plt.plot(coin_price_df, label='Daily Price')
#     plt.legend()
#     plt.xticks(rotation = 45)
#     plt.show()

#     explanation = "xxxxx"
#     print(explanation)
#     return coin_price_df
  
# def sma_plot(coin_price_df,coin_id):  #Simple Moving Average
#     sma_df = coin_price_df
#     sma_seven = sma_df.loc["price"].rolling(7).mean()
#     sma_twelve = sma_df.loc["price"].rolling(12).mean()
#     sma_df.dropna(inplace=True)
    
#     plt.title(coin_id + ' Bollinger Bands for 2022')
#     plt.xlabel('timestamp')
#     plt.ylabel('Daily Prices')
#     plt.plot(daily_prices, label='Daily Price')
#     plt.plot(sma_seven, label='Simple Moving Average 7-Day', c='o')
#     plt.plot(sma_twelve, label='Simple Moving Average 12-Day', c='b')
#     plt.legend()
#     plt.xticks(rotation = 45)
#     plt.show()

#     explanation = "xxxxx"
#     print(explanation)
#     return sma_df

# # def wma_plot (sma_df):
# #     sma_df["WMA7"] = sma_df["price"].ewm(7).mean()
# #     sma_df.dropna(inplace=True)
# #     sma_wma7_df = sma_df[["price", "SMA7", "WMA7"]]
# #     plt.title(coin_id + ' Bollinger Bands for 2022')
# #     plt.xlabel('timestamp')
# #     plt.ylabel('Daily Prices')
# #     plt.plot(daily_prices, label='Daily Price')
# #     plt.plot(bollinger_up, label='Bollinger Up', c='g')
# #     plt.plot(bollinger_down, label='Bollinger Down', c='r')
# #     plt.legend()
# #     plt.xticks(rotation = 45)
# #     plt.show()
# #     return sma_wma7_df
    

# # def get_sma(prices, rate=7):
# #         return prices.rolling(rate).mean()

    
# # def get_bollinger_bands(prices, rate=20):
# #         sma = get_sma(prices, rate) # <-- Get SMA for 20 days
# #         std = prices.rolling(rate).std() # <-- Get rolling standard deviation for 20 days
    
# #         bollinger_up = sma + std * 2 # Calculate top band
# #         bollinger_down = sma - std * 2 # Calculate bottom band
# #         return bollinger_up, bollinger_down

# #     symbol = coin_id
# #     daily_prices = df['price']
# #     bollinger_up, bollinger_down = get_bollinger_bands(daily_prices)
    
# # #plots the daily price with the bollinger bands
# #     plt.title(symbol + ' Bollinger Bands for 2022')
# #     plt.xlabel('timestamp')
# #     plt.ylabel('Daily Prices')
# #     plt.plot(daily_prices, label='Daily Price')
# #     plt.plot(bollinger_up, label='Bollinger Up', c='g')
# #     plt.plot(bollinger_down, label='Bollinger Down', c='r')
# #     plt.legend()
# #     plt.xticks(rotation = 45)
# #     plt.show()

    
###########################################################
def notification ():
    
    top_ten_coin_list = ["bitcoin", "ethereum", "tether", "binancecoin", "usd-coin", "binance-usd", "ripple", "cardano", "dogecoin", "matic-network"]
    
    coin_id = choose_coin(top_ten_coin_list)
    coin_id, coin_df = get_coin_data (coin_id)
    print(coin_df)


    # coin_price_df = indicators (coin_df,coin_id)
    
    # sma_df = sma_plot(coin_price_df, coin_id)
    
   
    # st.line_chart(sma_df)

    
    # sma_wma7_df = wma_plot (sma_df)
    # st.line_chart(sma_wma7_df)
    
    # prices = coin_price_df
    # bollinger_up, bollinger_down = get_bollinger_bands(prices, rate=20)
    # st.line_chart(prices, bollinger_up, bollinger_down)
notification()
