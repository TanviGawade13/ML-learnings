import csv
import requests

from pathlib import Path
from bs4 import BeautifulSoup


URL = "https://this-domain-absolutely-does-not-exist-12345.com"
CSV_PATH = Path(__file__).with_name("books.csv")
# for path check where this file exists and then there only create a new file with books.csv when asked to do 


def main():
    try:
        #response has all the html that we got from sending the request 
        response = requests.get("https://httpbin.org/status/404", timeout=30)
        #raise_for_status handles only the httperror like if its anything other than 200
        # and it does not raise an http error if raise for status is not there

        response.raise_for_status()  
    except Exception as e:
        print(type(e))  # prints the whole class
        print(type(e).__name__) # just prints the exception name
        print(f"Falied to connect {e}")
        return


    soup = BeautifulSoup(response.text, "html.parser")
    #gives the html text in proper organised format 

    # we use .select when we want to seect any tag using the classname


    # soup.select returns all the html article tags in a list that has a classname product pod 
    # select_one is the sibling function of select but returns only the first match or none is nothing matches 
    # in beutiful soup book.p.instock searches for a first p tag and next instock tag which should be the child tag
    # of p but it does not exists so instead we search using class name which is done using the 
    # book.select or book.select_one and the in the bracket we enter the tag+class name ie p.instock 
    # get_text gets the visible text and strip removes the extra white spaces

    books = []
    books_onpage = soup.select("article.product_pod")
    if not books_onpage:
        print("No books found! mybe the website renders javascript")
        return

    for book in books_onpage:

        #if book.h3 is present then store book.h3.a tag in title_tag or else store None
        title_tag = book.h3.a if book.h3 else None
        # if the value of title_tag variable is None or title_tag does not have the attiburte title 
        # then print the statement 
        if title_tag is None or not title_tag.has_attr('title'):
            print("Skipping a book as title not found")
            continue
        title = title_tag['title']

        price_tag = book.select_one('p.price_color')
        if price_tag is None:
            print(f"Skipping {title} because the price of the book not found")
            continue
        price = price_tag.get_text(strip=True)

        instock_tag = book.select_one('p.instock')
        if not instock_tag:
            print(f"Skipping {title} book beacuse its not in stock")
            continue
        instock = instock_tag.get_text(strip=True)
        books.append({"title": title, "price": price, "availability": instock})
        print(f"{title} — {price}, {instock}")

    with CSV_PATH.open("w", newline="", encoding="utf-8") as csv_file:
        #with means open the notebook let me do my work and then close it after i am done
        # open this notebook(csv_path) and lets call it csv_file 
        # if there is anything erase it and start clean
        writer = csv.DictWriter(csv_file, fieldnames=["title", "price", "availability"])
        # give me a assistant object DictWritter and lets call it writer 
        # and these are the feild names and this is the file we want to write in the exact order
        writer.writeheader()
        #write the headings first at the top row 
        writer.writerows(books)
        #go through this whole list of dictniories and one at a time write it in the file matching them with column names


if __name__ == "__main__":
    main()
