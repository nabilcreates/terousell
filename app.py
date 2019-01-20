import requests
from bs4 import BeautifulSoup

# Process of program
# The program search for each listing link with your search query
# It pushes the listing link into an array


def get_listings_from_query(query_str):

    # get the URI to make the get request to
    uri = 'https://sg.carousell.com/search/products/?sort_by=time_created%2Cdescending&query='

    # Get data from the uro + query string passed as an argument
    html_data = requests.get(uri + query_str).content

    # parse it into beautifulsoup
    query_soup = BeautifulSoup(html_data, 'html.parser')

    # !!! look for the individual listing link !!!
    # <a class="C-ac"></a>
    query_soup_results = query_soup.find_all('a', {'class': 'C-ac'})

    # declare an empty array
    other_listing_links = []

    # for each of the item found
    for item in query_soup_results:

        # append or push to the array
        other_listing_links.append('https://sg.carousell.com{}'.format(str(item['href'])))

    # return the listings array
    return other_listing_links

# ============================
# ============================
# ============================
# MAIN PROGRAM
# MAIN PROGRAM
# MAIN PROGRAM
# ============================
# ============================
# ============================

query_str = input('Enter query for Carousell Search: ')
listings = get_listings_from_query(query_str)

# ============================
# ============================
# ============================
# OTHER CODE
# OTHER CODE
# OTHER CODE
# ============================
# ============================
# ============================


# Now it loops to get the more specific info
for listing_link in listings:

    # so for every listing_link...

    # make a get request to get the http data
    html_data = requests.get(listing_link).content

    # parse it into beautifulsoup
    query_soup = BeautifulSoup(html_data, 'html.parser')

    # !!! look for the title !!!
    # Title
    # <p class="eh-b eh-e"></p>
    title = query_soup.find_all('p', {'class': 'eh-b eh-e'})[0].text

    # !!! look for the price !!!
    # Price
    # <p class="eh-b eh-d"></p>
    price = query_soup.find_all('p', {'class': 'eh-b eh-d'})[1].text

    # Print the price and the title of the listing all out
    print('[{}] - {}'.format(price, title.encode('utf-8')))