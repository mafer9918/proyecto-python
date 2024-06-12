import requests # Importar el modulo requests para hacer las solicitudes HTTP
from bs4 import BeautifulSoup # Importamos BeautifulSoup para analizar los documentos HTML
import pandas as pd # Importamos pandas para manejar datos en los DataFrames 
from ..decorators.decorators import registrar_ejecucion_funcion, medir_tiempo_ejecucion # Importa los decoradores personalizados

def fetch_page(url):
    """
    Obtenemos el contenido de una pagina.
    
    Args :
        url (str) : URL de la pagina web a solicitar.

    Returns :
        str: Contenido HTML de la pagina Web.

    Raises :
        System exit: Si ocurre un error en la solicitud HTTP.
    """
    response= requests.get(url) # Realizamos una solicitud GET a la URL proporcionada.
    if response.status_code == 200: # Comparamos el status code con el 200 que significa que fue una peticion exitosa
        return response.content # Devolvemos el contenido de la pagina si la solicitud fue exitosa
    else:
        raise Exception(f"Fallo al recuperar la página: {url}") # Lanzamos una excepcion por si la solicitud falla

@registrar_ejecucion_funcion # Añade logging a la función
@medir_tiempo_ejecucion # Mide el tiempo de ejecución de la función
def parse_product(product):
    """
    Analizamos los detalles de un producto.
    
    Args :
        product (bs4.element.Tag) : Objeto BeautifulSoup que contiene la informacion del producto.

    Returns :
        dict: Diccionario con Marca, Descripcion, Precio, Rating y Número de Reviews del producto
    """
    title_tag = product.find("a", {"title": True})
    if title_tag:
        nameProduct = title_tag.get('title').strip()
    else:
        nameProduct = product.find("a", class_="title").text.strip()
    brand = nameProduct # Encontramos y obtenemos el titulo del producto
    description = product.find("p", class_="description").text.strip() # Encontramos y obtenemos la descripcion del producto
    price = product.find("h4", class_="price").text.strip() # Encontramos y obtenemos el precio del producto
    reviews_counts = product.find("p", class_="review-count").text.strip() # Encontramos y obtenemos el número de reviews del producto
    ratings_div = product.find('div', class_='ratings')
    rating_tag = ratings_div.find('p', {'data-rating': True})
    rating = rating_tag['data-rating'] if rating_tag else None # Encontramos y obtenemos el rating del producto
    return{ # Retornamos un diccionario con la marca, descripción, precio, número de reviews y rating del producto
        "brand": brand,
        "description": description,
        "price": price,
        "number_reviews": reviews_counts,
        "rating": rating
    }

@registrar_ejecucion_funcion # Añade logging a la función
@medir_tiempo_ejecucion # Mide el tiempo de ejecución de la función
def scrape(url):
    """
    Metodo principal de scraping con soporte para multiples paginas.
    
    Args :
        url (str) : URL de la pagina web a scraoear.

    Returns :
        list: Una lista de elementos que representan los datos de los productos.
    """
    page_content = fetch_page(url) # Obtenemos el codigo base de la pagina
    soup = BeautifulSoup(page_content, "html.parser") # Analizamos el contenido de la pagina con Beautiful Soup
    products = soup.find_all("div", class_="thumbnail") # Encontramos todos los elementos div con la clase "thumbnail" que representan productos
    items=[] #Inicializamos una lista para almacenar los datos de los productos.
    for product in products:
        product_info = parse_product(product) # Analizamos cada producto encontrado
        items.append(product_info) # Agregamos los datos del producto a la lista.
    return items 

@registrar_ejecucion_funcion # Añade logging a la función
@medir_tiempo_ejecucion # Mide el tiempo de ejecución de la función
def get_all_pages(base_url):
    """
    Metodo para realizar la paginación
    
    Args :
        url (str) : URL de la pagina web a scraoear.

    Returns :
        pd.DataFrame : DataFrame de pandas con los datos de los productos
    """
    productos=[] #Inicializamos una lista para almacenar los datos de los productos.
    page = 1 #Inicializamos una lista para almacenar los datos de los producots.
    while True:
        url = f"{base_url}?page={page}" # Modificamos la url base para añadir el número de página
        nuevos_productos = scrape(url) # Llamamos a la función scrape para obtener los datos de los productos de esa página
        if not nuevos_productos: # Condición que si es verdadera termina la ejecución
            break
        productos.extend(nuevos_productos) # Agrega los nuevos productos a la lista de productos.
        page += 1 # Incrementa el número de página para obtener la siguiente página de productos.
    return pd.DataFrame(productos)  

# Definimos el URL base para el Scraping.
url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

# Llamamos a la funcion get_all_pages para obtener los datos de los productos de todas las páginas
df = get_all_pages(url)
# Guardamos los datos en un archivo CSV sin incluir el indice.
df.to_csv("data/raw/products.csv", index=False)
