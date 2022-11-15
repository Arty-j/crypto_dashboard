# Crypto Dashboard Multipage - White Paper -
-----

This project will create a dashboard for cryptocurrency data, including coin trend indicators of the top 10 ranking coins by market cap.  It is meant to be simple and straight-forward for users new to crypto, to help them evaluate coin performance and a starting point for evaluating buy/sell opportunities. Finally, is project evaluates coin prices and trading fees across 5 different trading exchanges to find the best price for each coin. The user can elect to receive notifications via email notification every (XXXXXXXtimeframe)to tell them the "best value" exchange for their top 3 prefered coins. 


## *Project Description*
*User Experience:*
Crypto Currency Dashboard  
                   
1. The Welcome Page, gives the user a quickview of the top 10 coins by market cap and their current trends in an easy to read table.

2. The next page follows the user's interest in diving deeper into coin trend analyses. The user is able to select a coin from the top 10 and see a graphical display of it's price history over a choosen timeframe.  There are also results of performance indicators for the choosen coin, such as Reset Settings Index (RSI), Moving Average, and Bollinger bands.  These trade signal statistics are provided with  short explanations of their significance and represented graphically to highlight trends.

3. The final page offers the users the opportunity to receive email notifications, identifying the "best value" exchange on which to buy their top 3 prefered coins.


## *Questions to Answer* *Future Functionality*

Questions, we looked to answer:
    1. I am new to crypto currency, what criteria should I look at when evaluating coins?
    2. Besides price trend, and volume, what metrics are used to indicate trends and buy/sell opportunities?
    3. Are all exchanges the same? Why should I by my coin on one exchange versus another.

This is a simple to navigate dashboard for new crypto users; it is set up so not to overwhelmed a user with options, functionality, and platform navigation. It provides basic insight into what data is important when evaluating coins profit/risk potential. 

Future development could include:
    1. refine data sourcing
    2. smart order routing in buy/sell funtionality
    3. coin recommendations based on machine learning modeling
    4. arbitrage opportunity notification for subscription users

## *Technologies*
----------
coingecko API - for coin data

StreamIt/Panel - for Dashboard


## *Project Tasks*
 - Kausar - main dashboard page construction of project pages in streamlit

 - Marissa - access api data from 5 exchanges, evaluate for best price
 
 - Edith - 

 - Jodi - looping live api data saved to csv file
