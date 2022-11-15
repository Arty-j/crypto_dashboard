import pandas as pd


# filters coins through criteria, returns lists for each critera of coins meeting those criteria
# def notification_filters (all_coin_info_df):
#    coin_df = all_coin_info_df ##change column names!!!!
#    change_list = []
   
#    for i in range(len(coin_df)):
#     # filter 1: coin price change more than 30% in 24hrs
#     if  coin_df.loc[i,"price"] > (coin_df.loc[i, "24hr_price"] + (coin_df.loc[i,"24hr_price"] * .3)):
#         greater30 = change_list.append(coin_df.loc[i, "id"])
#     elif coin_df.loc[i,"price"] < (coin_df.loc[i, "24hr_price"] - (coin_df.loc[i, "24hr_price"] * .3)):
#         lessthan30 = change_list.append(coin_df.loc[i, "id"])
    
#     # filter 2: coin price change more than 30% in 1hr
#     elif coin_df.loc[i,"percent_change_1hr"] > 0.2:
#         greater_1hr = change_list.append(coin_df.loc[i, "id"])
#     elif coin_df.loc[i,"percent_change_1hr"] < 0.2:
#         lessthan_1hr_1hr = change_list.append(coin_df.loc[i, "id"])

#     # filter 3: volume change criteria
#     elif coin_df.loc[i,"volume"] > (coin_df.loc[i, "volume"] + (coin_df.loc[i,"volume"] * .3)):
#         volume_change_list = change_list.append(coin_df.loc[i, "id"])
#     elif coin_df.loc[i,"volume"] < (coin_df.loc[i, "volume"] - (coin_df.loc[i,"volume"] *.3)):

#     return greater30, lessthan30, greater_1hr, lessthan_1hr_1hr, volume_change_list

# def notification_email_body (greater30, lessthan30, greater_1hr, lessthan_1hr_1hr, volume_change_list):
#     if len(greater30) > 0:
#         body_great30 = f"The following coins have all seen a price change of 30% or greater in the past 24 hours: {percent30_price_change_list}."

#     elif len(lessthan30) > 0:
#         body_great30 = f"The following coins have all seen a price change of 30% or greater in the past 24 hours: {percent30_price_change_list}.""

#     elif len(gr)
#     hr1 = f\"The following coins have all seen a price change of 30% or greater in the past 24 hours: {hr1_price_change_list}.\" 
#     elif volume_change_list == True\
#     volume = (f\"The following coins have all seen a price change of 30% or greater in the past 24 hours: {hr1_price_change_list}.\") \n",
#     else:
#         return 
 