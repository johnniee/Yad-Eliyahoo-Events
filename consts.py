from datetime import datetime

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year


events_page = 'http://www.sportpalace.co.il/menora-mivtachim/' \
              '%D7%9C%D7%95%D7%97-%D7%90%D7%A8%D7%95%D7%A2%D7%99%D7%9D/' \
              '?yr={0}&month={1}'.format(str(currentYear), str(currentMonth))
