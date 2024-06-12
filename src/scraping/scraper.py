import requests
from bs4 import BeautifulSoup
import pandas as pd
from ..decorators.decorators import registrar_ejecucion_funcion, medir_tiempo_ejecucion

def fetch_page(url):
    try:
        response = requests.get(url)
        return response.content
    except requests.exceptions.RequestException as e:
        raise Exception(f"Fallo al recuperar la página: {e}")

@registrar_ejecucion_funcion
@medir_tiempo_ejecucion
def parse_product(product):
    title_tag = product.find("a", {"title": True})
    if title_tag:
        nameProduct = title_tag.get('title').strip()
    else:
        nameProduct = product.find("a", class_="title").text.strip()
    brand = nameProduct
    description = product.find("p", class_="description").text.strip()
    price = product.find("h4", class_="price").text.strip()
    reviews_counts = product.find("p", class_="review-count").text.strip()
    ratings_div = product.find('div', class_='ratings')
    rating_tag = ratings_div.find('p', {'data-rating': True})
    rating = rating_tag['data-rating'] if rating_tag else None
    return{
        "brand": brand,
        "description": description,
        "price": price,
        "number_reviews": reviews_counts,
        "rating": rating
    }

@registrar_ejecucion_funcion
@medir_tiempo_ejecucion
def get_info_product(url):
    page_content = fetch_page(url)
    soup = BeautifulSoup(page_content, "html.parser")
    products = soup.find_all('div', class_='thumbnail')
    items = []
    for product in products:
        product_info = parse_product(product)
        items.append(product_info)
    return items

@registrar_ejecucion_funcion
@medir_tiempo_ejecucion
def scrape(base_url):
    productos=[]
    page = 1
    while True:
        url = f"{base_url}?page={page}"
        nuevos_productos = get_info_product(url)
        if not nuevos_productos:
            break
        productos.extend(nuevos_productos)
        page += 1
    return pd.DataFrame(productos)  

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"
df = scrape(url)
print(df["description"])
df.to_csv("data/raw/products.csv", index=False)
