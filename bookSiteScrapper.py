import requests
from bs4 import BeautifulSoup
import csv

def fetch_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    headers = ['Title', 'Price', 'Availability']
    data = []
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        data.append([title, price, availability])
    return headers, data

def save_to_csv(headers, data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

def main():
    url = 'http://books.toscrape.com/'
    html_content = fetch_webpage(url)
    if html_content:
        headers, data = parse_html(html_content)
        if headers and data:
            save_to_csv(headers, data, 'books.csv')
            print("Data has been saved to books.csv")
        else:
            print("No data found to save.")
    else:
        print("Failed to fetch the webpage content.")

if __name__ == "__main__":
    main()