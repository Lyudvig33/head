"""
this code uses Tkinter, a standard GUI
(Graphical User Interface) library for Python,
to create a simple desktop application.
The user interface consists of a text box where the content of the uploaded text file is displayed,
along with buttons to upload the text file and save the cryptocurrency data to an Excel file.

Author Lyudvig Asoyan,
Date 05.05.2024
"""
from tkinter import *
from tkinter import filedialog as fd
import requests
import xlsxwriter


# the window for the application
desktop = Tk()
desktop.geometry('600x370+600+300')
desktop.title("Crypto app")

def upload_txt():
    """
    function for read and open txt file
    """
    text_file = fd.askopenfilename(initialdir="/Desktop/pyt_git/Desktop-app",
                                   title="Upload File",
                                   filetypes=(("txt files","*.txt"),("all files","*.*")))
    # checking is text_file TRUE?
    if text_file:
        with open(text_file,'r') as file:
            content = file.read()

        # adding content to the end of the list
        my_txt.insert(END, content)


def crypto_values(symbols):
    """
    the function to receive is the date of the cryptocurrency
    """
    filtered_coins = []
    for i in symbols:
        if len(i) > 1:
            filtered_coins.append(str(i).strip().lower())

    url = 'https://api.coingecko.com/api/v3/coins/markets'

    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'sparkline': 'false',
        'price_change_percentage': '24h',
        'market_data': 'true'
    }

    response = requests.get(url,params=params)
    data = response.json()

    results = []
    for i in data:

        symbol = i['symbol']

        if symbol.lower() in filtered_coins:
            name = i['name']
            current_price = i['current_price']
            market_cap = i['market_cap']
            price_change_24 = i['price_change_percentage_24h']

            results.append({
                "Symbol": symbol.upper(),
                "Name": name,
                "Current Price":current_price,
                "Market Cap": market_cap,
                "Price Change 24":price_change_24
            })
    return results


def save_as_xlsx():
    """
    the function for save cryptocurrency data in Xlsx file
    """

    # get all the elements from the txt file
    content = my_txt.get(1.0, END)

    symbols = content.split('\n')

    data = crypto_values(symbols)

    # get the keys for crypto_data
    symbols = list(data[0].keys())

    # function for give the Xlsx file a name
    filename = fd.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

    # Create Workbook Xlsx and worksheet
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
# put the names of title
    for ind, header in enumerate(symbols):
        worksheet.write(0,ind,header)

    row_index = 1
    for row in data:

        column = 0
        for key in row:
            value = row[key]
            worksheet.write(row_index,column,value)
            column += 1
        row_index += 1

    # rows sizes
    worksheet.autofit()

    workbook.close()

my_txt = Text(desktop, width=30, height=10, font=("arial",12))
my_txt.pack(pady=10)

open_button = Button(desktop, text="Upload Text File", command=upload_txt)
open_button.pack()

save_button = Button(desktop, text="Save as XLSX", command=save_as_xlsx)
save_button.pack()

desktop.mainloop()
