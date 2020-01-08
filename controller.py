from scraper import scrape_website
from sheet_writer import write_to_sheet
from consts import events_page


def main():
    events = scrape_website(events_page)
    for event in events:
        write_to_sheet(event)
