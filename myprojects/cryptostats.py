# Importing necessary libraries
import requests
import time

# Function to retrieve and display cryptocurrency statistics
def crypto_stats(name_filter,name_value):
    

        #API endpoint URL for retrieving cryptocurrency data
        url = 'https://api.coingecko.com/api/v3/coins/markets'

        # Parameters for API request
        params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': '20',
            'page': '1',
            'sparkline': 'false',
            'price_change_percentage': '24h',
            'market_data': 'true'
        }

        
        try:
            # Continuous loop to keep fetching data
            while True:
                    # Sending GET request to the API endpoint
                    response = requests.get(url, params=params)

                    
                    data = response.json()

                    # Looping through each cryptocurrency in the retrieved data
                    for i in data:
                        # Extracting relevant information for each cryptocurrency
                        name = i['name']
                        symbol = i['symbol'].upper()
                        current_price = i['current_price']
                        market_cap = i['market_cap']
                        price_change_24 = i['price_change_percentage_24h']

                        #Filtering based on user input criteria
                        if name_filter and name_filter.lower() and name_filter != symbol.lower():
                            continue
                        if name_value and market_cap < name_value:
                            continue

                        
                        print(f"{name}, Symbol: {symbol}, Current_Price: {current_price}, Market_cap: {market_cap}, 24h Change: {price_change_24}\n")

                    
                
                    print("----------------")
                    # Delaying next iteration by 5 seconds
                    time.sleep(5)
        # Handling exceptions
        except Exception as e:
            print("Please Wait:", e)



name_filter = input("Write Cryto name: ")
name_value = input("Write  value: ")
    
if name_value:
        
    # Converting market cap value to float if provided by the user
    name_value = float(name_value)
else:
    # Setting name_value to None if not provided by the user
    name_value = None

if __name__ == "__main__":
    print("Crypto price for the last 24 hours")
    crypto_stats(name_filter,name_value)





# def crypto_values():
    
#     url = 'https://api.coingecko.com/api/v3/coins/markets'
    
    
#     params = {
#             'vs_currency': 'usd',
#             'order': 'market_cap_desc',
#             'per_page': '20',
#             'page': '1',
#             'sparkline': 'false',
#             'price_change_percentage': '24h',
#             'market_data': 'true'
#         }

#     response = requests.get(url,params=params)
#     data = response.json()
#     with open("crypto.txt", "w") as file:
#         for i in data:
        
#             # name = i['name']
#             symbol = i['symbol'].upper()
#             # current_price = i['current_price']
#             # market_cap = i['market_cap']
#             # price_change_24 = i['price_change_percentage_24h']
            
#             file.write(f" {symbol} \n")
            

# crypto_values()