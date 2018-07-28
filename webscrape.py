#import libraries
import urllib2
from bs4 import BeautifulSoup

#Specifies URL
scraped_page = "https://www.bloomberg.com/quote/SPX:IND"

#Query website and return the html to the variable "page"
page = urllib2.urlopen(quote_page)

# parse html using beautiful soup and store in variable "soup"
soup = BeautifulSoup(page, "html.parser")

# Take out <div> of name and get its value
name_box = soup.find("h1", attrs = {"class": "name"})

name = name_box.text.strip()
# strip removes starting and trailing
print (name)

# get the index price
price_box = soup.find("fiv", attrs = {"class": "price"})
price = price_box.text
print (price)