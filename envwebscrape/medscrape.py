from requests import get
# import beautiful soup
from bs4 import BeautifulSoup
import pandas as pd

# Assign webpage address to variable url
url = "https://www.healthdirect.gov.au/medicines/brand/amt,10951000168106/diprosone"

# Get a response and store the server's response in variable response
response = get(url)
print (response)

# Parse response.text by creating a beautifulsoup object and assigning it to object
# to html_soup
# This uses Python's inbuilt html parser argument
html_soup = BeautifulSoup(response.text, "html.parser")
type(html_soup)

dosage = html_soup.find("span", class_ = "section-body expanded", id_ = "section-2")
print(dosage)