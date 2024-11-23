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

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using pip:

```sh
pip install requests beautifulsoup4  
