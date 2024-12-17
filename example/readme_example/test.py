import pandas as pd
from google_patent_scraper.main import Scraper  # Assuming Scraper is defined in main.py

# Create an instance of the Scraper class
scraper = Scraper()

# Add patents to the scraper
scraper.add_patents('US2668287A')
scraper.add_patents('US266827A')

# Scrape all added patents
scraper.scrape_all_patents()

# Extract parsed data into a list of dictionaries
patents_data = scraper.parsed_patents

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame()
for patent in patents_data:
    df = pd.concat([df, patent.to_dataframe()], ignore_index=True)



# Display the DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv('patents.csv', index=False)
