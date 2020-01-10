from scraper import scrape_website
from sheet_writer import write_to_sheet
from consts import events_page


def main(event, context):
    events = scrape_website(events_page)
    for event in events:
        print(event)
        write_to_sheet(event)
