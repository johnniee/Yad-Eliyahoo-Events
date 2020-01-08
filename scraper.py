import requests
from bs4 import BeautifulSoup
from datetime import datetime

TIME_PRESET = "%Y-%m-%dT%H:%M:%S"


def scrape_website(website_url):
    page = requests.get(website_url)
    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page.text, 'html.parser')

    # Take out the <div> of name and get its value
    name_box = soup.find_all('td', attrs={'class': 'has-events'})

    events = []
    for item in name_box:
        mini_soup = BeautifulSoup(str(item), "html.parser")
        if mini_soup.time is None:
            continue
        event_date = mini_soup.time['datetime']
        event_datetime = datetime.strptime(event_date, TIME_PRESET)
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
