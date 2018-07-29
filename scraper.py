import urllib2
from bs4 import BeautifulSoup
from datetime import datetime


def scrape_website(website_url):
    page = urllib2.urlopen(website_url)

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
    name_box = soup.find_all('td', attrs={'class': 'has-events'})

    events = []
    for item in name_box:
        mini_soup = BeautifulSoup(str(item), "html.parser")
        event_date = mini_soup.time['datetime'].encode('utf-8')
        event_datetime = datetime.strptime(event_date, "%Y-%m-%dT%H:%M:%S")
        artist = mini_soup.find(attrs={'class': 'longdesc'}).text
        try:
            artist = str(artist.replace("\n", "").encode("utf-8"))
        except UnicodeEncodeError as e:
            print("Couldn't parse artist - %s" % e.message)

        event_body = {
            "artist": artist,
            "datetime": str(event_datetime),
        }
        events.append(event_body)
    return events
