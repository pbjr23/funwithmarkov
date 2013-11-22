from bs4 import BeautifulSoup
import urllib2

# Scrape some Ted Nugent quotes
r = urllib2.urlopen('http://www.brainyquote.com/quotes/authors/a/albert_einstein.html')

nugent_raw = r.text
soup = BeautifulSoup(nugent_raw)

all_quotes = []

# Parse HTML - get the text between 'a' tags with the title="view quote" attribute
for node in soup.find_all('a', attrs={'title': 'view quote'}):
    quotes_unclean = ''.join(node.find_all(text=True))
    quotes_unclean_str = str(quotes_unclean)
    all_quotes.append(quotes_unclean_str)

# Get rid of the Ted Nugent references
all_quotes = [item for item in all_quotes if item != 'Albert Einstein']


def string_quotes(quotes):
    """Print the quotes as a string"""
    result = ' '.join(quotes)
    return result