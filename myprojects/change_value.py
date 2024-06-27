
# import requests


# def change_rates(amount,base_currency,target_currency):
#     url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"    
 
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         rates = data['rates']
#         if target_currency in rates:
#             exchange_rates = rates[target_currency]
#             converted_amount = amount * exchange_rates
#             return converted_amount
#         else:
#             print(f"Eror: Target currency {target_currency} not found")
#     else:
#         print(f"Error: Failed to fetch exchange rates. Status code:{response.status_code}")
#         return None


# def main():
#     print("welcome to the Currency Converter")
#     user_amount = (input("Enter the amount to converter: "))

#     if user_amount.isdigit() == False:
#         print('Please write numeric value for the amount')
#         return
    
#     amount = float(user_amount)
#     source_currency = input("Enter the source currency: ").upper()
#     target_currency = input("Enter the source currency: ").upper()


#     converted_amount = change_rates(amount,source_currency,target_currency)
#     if converted_amount is not None:
#         print("\nConverted amount")
#         print(f"{amount},{source_currency} is equivalent to {converted_amount:.2f} {target_currency}")

# if __name__ == "__main__":
#     main()
