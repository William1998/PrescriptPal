# To scrape a page, we need to download the page first
# use the get function
from requests import get
# import beautiful soup
from bs4 import BeautifulSoup
import pandas as pd

# Assign webpage address to variable url
url = "https://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1"

# Get a response and store the server's response in variable response
response = get(url)
print (response.text[:500])

# Parse response.text by creating a beautifulsoup object and assigning it to object
# to html_soup
# This uses Python's inbuilt html parser argument
html_soup = BeautifulSoup(response.text, "html.parser")
type(html_soup)

# Find all methods to extract the div containers
movie_containers = html_soup.find_all("div", class_ = "lister-item mode-advanced")
print(type(movie_containers))
print(len(movie_containers))

# Find the movie name
first_movie = movie_containers[0]
first_name = first_movie.h3.a.text
print(first_name)

# Find the movie year
first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold')
first_year = first_year.text
print(first_year)

# Get the rating, which is found in the strong tag
first_imdb = float(first_movie.strong.text)
print(first_imdb)

# Find MetaScore
first_mscore = first_movie.find("span", class_ = "metascore favorable")

first_mscore = int(first_mscore.text)
print(first_mscore)

# Get the number of votes 
first_votes = first_movie.find("span", attr = {'name': 'nv'})
print(type(first_votes))

# Declare variables to have something to store data in
# Loop through each container in movie_containers (the variable which contains all the 50 movie containers).
# Extract the data points of interest only if the container has a Metascore.

names = []
years = []
imdb_ratings = []
metascores = []

# Extract data from individual movie container

for container in movie_containers:

    # If the movie has Metascore, then extract:
    if container.find("div", class_ = "ratings-metascore") is not None:

        # The name
        name = container.h3.a.text
        names.append(name)

        # The year
        year = container.h3.find("span", class_ = "lister-item-year").text
        years.append(year)

        # The IMDB Rating
        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)

        # The Metascore
        m_score = container.find("span", class_ = "metascore").text
        metascores.append(int(m_score))

test_df = pd.DataFrame({'movie': names,
                       'year': years,
                       'imdb': imdb_ratings,
                       'metascore': metascores})
print(test_df.info())
test_df