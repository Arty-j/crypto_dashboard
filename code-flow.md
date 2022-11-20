## Code Flow - Notifications

# Modules: live_data_storage.py
Pull, filter and storage of live API data
1. `def api-timer()` runs continuous scheduler ever(x) minutes
    --calls function `get_live_data()` api call every (x)minues, gets data for all 10 coins
        --calls `clean_coin_data(all_coiN_info.df)` which returns all_coin_info.df
        --calls `save_coin_data(all_coin_info.df)` which creates sql database table "coin_info"

# Indicators
1. asks user for coin choice via sidebar widget (from top 10 coin list - which is called from code in `data_utils.get_top_ten_coins()`)
    -api call with that coin for data past 90 days
    -creates db of price
    -currently slices 90 days of data  to create new df (because I got api call from jan1,2022- can be changed)
    -plots price for 90 days
    -computes simple moving average (SMA)for 7 & 12 days, and plots
        --explains significance and plot
    -computes weighted moving average (WMA)for 7 days
    -plots price vs. SMA-7 & WMA -7
        --explains significance and plot
    -computes bollinger bands
    -plots price vs bollinger bands
        --explains significance and plot

# Email Notifications
1. Sidebar checkbox widget asks if they want **email notifications**
    -if yes, it runs `verify notification(coin_list)` from Modules.email_list
       --runs function `coin_choice'(coin_list)` to save their 4 coin preferances
       --runs function `add_email_and_coin(new email, coin choices)`, saves them to dataframe and
       sql database. 
       --returns the email and coin df
 
   
2. email_send.py **this needs refining -- grabs right emails and coin preference fromsql database)**
    -takes in global variable email_msg
    -takes email and coin preferance from sql database lists
    -sends emails
    -

