#!/usr/bin/env python
# coding: utf-8

# In[60]:


import requests
from bs4 import BeautifulSoup
from time import sleep
import base64
import pandas as pd

# Getting user inputs
url = input("Paste URL from Star Tech: ")
file_name = input("File name (e.g., laptop_data, intel_processor, etc.): ")

products = []

# Function to scrape a page
def page_scrap(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")  # This variable contains all information of the page in a BeautifulSoup object
    product_divs = soup.find_all("div", class_="p-item")  # Finding all divs that contain individual product data
    sleep(2)

    for product in product_divs:
        all_info = {}
        product_name = product.find("h4", class_="p-item-name").text.strip()  # Finding product names in an h4 HTML tag, then converting to text data and stripping to remove extra space
        all_info.update({"product_name": product_name})

        sleep(2)
        product_image = product.find("img")["src"]  # Finding product image URL from img tag
        image_data = requests.get(product_image).content  # Requesting image content
        image_base64 = base64.b64encode(image_data).decode('utf-8')  # Encoding the image to base64 instead of saving it to hard disk
        all_info.update({"image_base64": image_base64})

        product_features = product.find("ul").text.strip()
        sleep(2)
        all_info.update({"product_features": product_features})

        price_text = product.find("div", class_="p-item-price").text.strip()

        if price_text.endswith("৳"):
            product_price = price_text.split()[0].strip().replace("৳", "")
            all_info.update({"product_price": product_price})
        else:
            out_of_stock_message = price_text
            all_info.update({"out_of_stock_message": out_of_stock_message})

        sleep(2)
        products.append(all_info)

# Function to get the next page URL
def get_next_page(soup):
    pagination_ul = soup.find("ul", class_="pagination")
    if pagination_ul:
        next_page_li = pagination_ul.find_all("li")[-1]
        if "disabled" not in next_page_li.get("class", []):
            a_tag = next_page_li.find("a")
            if a_tag and "href" in a_tag.attrs:
                return a_tag["href"]
            else:
                print("No link found in the last li element")
        else:
            print("The next page link is disabled")
    else:
        print("Pagination not found")
    return None

# Main loop to scrape all pages
while url:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    page_scrap(url)
    next_url = get_next_page(soup)
    if next_url:
        url = next_url
    else:
        break

# Save scraped data to a CSV file
product_info = pd.DataFrame(products)
product_info.to_csv(f"{file_name}.csv", index=False)
# print("Alhamdulillah Done")
# input("Press Enter to exit")


# In[ ]:




