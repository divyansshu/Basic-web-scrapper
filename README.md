# Basic Web Scraper

This project contains two web scrapers: one for scraping book information from a book site and another for scraping quotes from a quote site. The scraped data is saved into CSV files.


## Usage

### 1. Book Site Scraper
- **Script**: `bookSiteScraper.py`
- **Functionality**: Scrapes book information from [Books to Scrape](http://books.toscrape.com/) and saves the data to a CSV file named `books.csv`.
- **Run Command**:
  ```sh
  python bookSiteScraper.py

### 2. Quote Site Scraper
- **Script**: `quoteSiteScraper.py`
- **Functionality**: Scrapes quotes from  [Quotes to Scrape](https://quotes.toscrape.com/) and saves the data to a CSV file named `quotes.csv`.
- **Run Command**:
  ```sh
  python quoteSiteScraper.py


## Example

### Book Site Scraper Output
- **CSV Columns**: `Title`, `Price`, `Availability`
- **Sample Data**:
  ```mathematica
  "A Light in the Attic", £51.77, In stock
  "Tipping the Velvet", £53.74, In stock

### Quote Site Scraper Output
- **CSV Columns**: `Quote`, `Author`, `Tags`
- **Sample Data**:
  ```mathematica
  "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.", "Albert Einstein", "change, deep-thoughts, thinking, world"
  "It is our choices, Harry, that show what we truly are, far more than our abilities.", "J.K. Rowling", "abilities, choices"  


## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using pip:

  ```sh
  pip install requests beautifulsoup4


  
