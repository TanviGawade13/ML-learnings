import csv
from pathlib import Path

import requests
from bs4 import BeautifulSoup


URL = "https://books.toscrape.com/"
CSV_PATH = Path(__file__).with_name("books.csv")


def main():
    response = requests.get(URL, timeout=30)

    soup = BeautifulSoup(response.text, "html.parser")

    books = []
    for book in soup.select("article.product_pod"):
        title = book.h3.a["title"]
        price = book.select_one("p.price_color").get_text(strip=True)
        books.append({"title": title, "price": price})

    for book in books:
        print(f"{book['title']} — {book['price']}")

    with CSV_PATH.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["title", "price"])
        writer.writeheader()
        writer.writerows(books)


if __name__ == "__main__":
    main()
