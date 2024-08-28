#! /home/reiri/workspaces/freelance/web-scrapping/webenv/bin/python

import requests
from bs4 import BeautifulSoup


def get_price(u):
    """
    Fetches the prices from the given URL

    Args:
        url (str): The URL of the product page.

    Returns:
        tuple: A tuple containing the Sbpay price, normal price, and old price.
            If a price is not found, a corresponding message is returned.
    """

    response = requests.get(u)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract name of the product
    elem_product = soup.find('h1',{'class':'product-name product_name_pdp'})
    name_product = elem_product.get_text().strip() if elem_product \
        else "Name product not found"

    # Extract the Sbpay price
    elem_sbpay = soup.select_one('.sbpay-price span')
    price_sbpay = elem_sbpay.get_text().split()[1] if elem_sbpay \
        else "Sbpay price not found"
    # price_sbpay = price_sbpay.split()[1]

    # Extract the normal price
    elem_normal = soup.find('span',{'class': 'normal-price no-decoration extra-price'})
    price_normal = elem_normal.get_text() if elem_normal \
        else "Normal price not found"

    # Extract the old price
    elem_old = soup.select_one(".old")
    price_old = elem_old.text.strip() if elem_old \
        else "Old price not found"

    return name_product, price_normal, price_old, price_sbpay


url = "https://salcobrand.cl/products/estradiol-0-1-topico-" \
      "semisolido-1429a6a8-f299-4655-837a-354fbfd3e7a7" \
      "?default_sku=3028594&gclid=CjwKCAjwkuqvBhAQEiwA65XxQM" \
            "58ubie6n4zWlcqMCtRT-IaGv2sqe1D1Rt3hPqTPlcfXX-puTg9-RoCV3IQAvD_BwE"

try:
    name_product, price_normal, price_old, price_sbpay = get_price(url)
    print(f"Product: {name_product}")
    print(f"Internet price: {price_normal}")
    print(f"Old price: {price_old}")
    print(f"Sbpay price: {price_sbpay}")
except Exception as e:
    print(f"Could not fetch the prices: {e}")
