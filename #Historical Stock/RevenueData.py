#Historical Stock/Revenue Data 
# Question 1: Use yfinance to Extract Tesla Stock Data

import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Extract Tesla stock data
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")

# Reset the index
tesla_data.reset_index(inplace=True)

# Display the first five rows
print("Tesla Stock Data (First 5 rows):")
tesla_data.head()

# Question 2: Use Webscraping to Extract Tesla Revenue Data
url_tesla = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_tesla = requests.get(url_tesla).text
soup_tesla = BeautifulSoup(html_tesla, "html.parser")

# Find the revenue table
tables = soup_tesla.find_all("table")
for table in tables:
    if "Tesla Quarterly Revenue" in table.text:
        tesla_revenue_table = table
        break

# Extract data into a DataFrame
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in tesla_revenue_table.find_all("tr"):
    cols = row.find_all("td")
    if len(cols) == 2:
        date = cols[0].text.strip()
        revenue = cols[1].text.strip().replace("$", "").replace(",", "")
        tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame({"Date": [date], "Revenue": [revenue]})], ignore_index=True)

# Remove empty rows
tesla_revenue = tesla_revenue[tesla_revenue["Revenue"] != ""]
print("Tesla Revenue Data (Last 5 rows):")
tesla_revenue.tail()


# Question 3: Use yfinance to Extract GameStop Stock Data

gme = yf.Ticker("GME")
gme_data = gme.history(period="max")

# Reset the index
gme_data.reset_index(inplace=True)

# Display the first five rows
print("GameStop Stock Data (First 5 rows):")
gme_data.head()


# Question 4: Use Webscraping to Extract GameStop Revenue Data

url_gme = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_gme = requests.get(url_gme).text
soup_gme = BeautifulSoup(html_gme, "html.parser")

# Find the revenue table
tables = soup_gme.find_all("table")
for table in tables:
    if "GameStop Quarterly Revenue" in table.text:
        gme_revenue_table = table
        break

# Extract data into a DataFrame
gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in gme_revenue_table.find_all("tr"):
    cols = row.find_all("td")
    if len(cols) == 2:
        date = cols[0].text.strip()
        revenue = cols[1].text.strip().replace("$", "").replace(",", "")
        gme_revenue = pd.concat([gme_revenue, pd.DataFrame({"Date": [date], "Revenue": [revenue]})], ignore_index=True)

# Remove empty rows
gme_revenue = gme_revenue[gme_revenue["Revenue"] != ""]
print("GameStop Revenue Data (Last 5 rows):")
gme_revenue.tail()
