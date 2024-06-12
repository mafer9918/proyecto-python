# Proyecto Final Python.
Web Scraping de una tienda en línea  

## Autor.
María Fernanda Galárraga  

## Requisitos.

- Python 3.7+
- pandas
- beautifulsoup4
- requests
- matplotlib
- time
- logging

## Instalación.
Para la instalación de dependencias se creó el archivo "dep.txt" donde están incluidas las dependencias necesarias para la ejecución del proyecto.  
El comando para una instalación rápida de todas las dependiencias es el siguiente:  

````bash
pip install -r .\dep.txt
````

## Estructura de las carpetas

````bash
proyecto/
│
├── assets/
│         |__ precio_por_marca.png
│         |__ rating_por_marca.png
│
├── data/
│   ├── raw/
│   │     ├──products.csv
│   └── processed/
│         ├──clean_products.csv
│
├── informe/
│         ├──informe_analisis_laptops.pdf
│
├── notebooks/
│         |__ estadistica_basica.ipynb
│         |__ precio_por_marca.ipynb
│         |__ rating_marca.ipynb
│
├── src/
│   ├── analysis/
│   │     |__ __init__.py
│   │     |__ analysis.py
│   ├── decorators/
│   │     |__ __init__.py
│   │     |__ decorators.py
│   ├── reports/
│   │     |__ __init__.py
│   │     |__ generate_report.py
│   └── scraper/    
│         |__ __init__.py
│         |__ scraper.py
│
├── dep.txt
└── README.md
````

## Ejecución del proyecto.

1. Ejecutar el scraper con el siguiente comando:  

````bash
python -m src.scraping.scraper
````

Esto va obtener la información de la tienda en línea y generar un CSV con esta data en la ruta: data/raw, llamado "products.csv"

2. Ejecutar el script para el análisis de datos con el siguiente comando:  

````bash
python -m src.analysis.analysis
````
Esto va generar un CSV con la data procesada en la ruta: data/processed, llamado "clean_products.csv"

3. Ejecutar los notebooks para la visualización de los datos.  

Esto va a generar imágenes en la carpeta assets que va a permitir generar el informe en formato PDF.  

4. Ejecutar el script para generar el informe en formato PDF:  

````bash
python -m src.reports.generate_report
````

Esto va a generar un informe en la carpeta informe llamado "informe_analisis_laptops.pdf"