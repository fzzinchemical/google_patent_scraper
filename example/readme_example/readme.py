# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Example 1: Scrape a single patent
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# ~ Import packages ~ #
import json
from google_patent_scraper import Scraper

# ~ Initialize scraper class ~ #
scraper = Scraper()

# ~~ Scrape patents individually ~~ #
patent_1 = 'US2668287A'
patent_2 = 'US266827A'
err_1, soup_1, url_1 = scraper.request_single_patent(patent_1)
err_2, soup_2, url_2 = scraper.request_single_patent(patent_2)

# ~ Parse results of scrape ~ #
patent_1_parsed = scraper.get_scraped_data(soup_1, patent_1, url_1)
patent_2_parsed = scraper.get_scraped_data(soup_2, patent_2, url_2)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Example 2: Scrape a list of patents
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# ~ Import packages ~ #

# ~ Initialize scraper class ~ #
scraper = Scraper()

# ~ Add patents to list ~ #
scraper.add_patents('US2668287A')
scraper.add_patents('US266827A')

# ~ Scrape all patents ~ #
scraper.scrape_all_patents()

# ~ Get results of scrape ~ #
patent_1_parsed = next(
    (p for p in scraper.parsed_patents if p.patent == 'US2668287A'), None)
patent_2_parsed = next(
    (p for p in scraper.parsed_patents if p.patent == 'US266827A'), None)

# ~ Print inventors of patent US2668287A ~ #
if patent_1_parsed:
    for inventor in json.loads(patent_1_parsed.inventor_name):
        print(f'Patent inventor : {inventor['inventor_name']}')
else:
    print('Patent US2668287A not found in parsed patents')
