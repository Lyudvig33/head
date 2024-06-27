Cryptocurrency Data Management Application

This Python application allows users to manage cryptocurrency data by uploading a list of cryptocurrency symbols from a text file, fetching corresponding data from the CoinGecko API, and saving the data to an Excel file.
Features

    Upload Text File: Users can upload a text file containing a list of cryptocurrency symbols.
    Fetch Cryptocurrency Data: The application fetches data for the uploaded cryptocurrency symbols from the CoinGecko API, including current price, market cap, and 24-hour price change percentage.
    Save Data to Excel: Once the cryptocurrency data is retrieved, the application saves it to an Excel file named "Crypto.xlsx".

Prerequisites

    Python 3.x
    requests library (pip install requests)
    xlsxwriter library (pip install XlsxWriter)

Usage

    Clone the repository or download the source code.
    Install the required dependencies using pip:

pip install requests
pip install XlsxWriter

Run the crypto_app.py file using Python:

    python crypto_app.py

    The application window will open. Use the "Upload Text File" button to select and upload a text file containing cryptocurrency symbols.
    Click the "Save as XLSX" button to save the fetched cryptocurrency data to an Excel file.

Notes

    Make sure the text file contains one cryptocurrency symbol per line.
    The application uses the CoinGecko API to fetch cryptocurrency data. Ensure you have a stable internet connection while using the application.

