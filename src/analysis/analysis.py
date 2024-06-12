import pandas as pd # Importamos pandas para manejo de datos
import os # Importamos os para manejo del sistema de archivos

def load_data(data_path):
    """
    Cargamos los datos desde un archivo CSV o Excel.

    Args :
        data_path (str) : Ruta del archivo a cargar.

    Returns :
        pd.DataFrame: DataFrame de pandas con los datos cargados.

    Raises :
        ValueError: Si el formato del archivo no es soportado.
    """
    if data_path.endswith(".csv"):
        df = pd.read_csv(data_path) # Lee datos desde un archivo CSV
    elif data_path.endswith(".xlsx"):
        df = pd.read_excel(data_path) # Lee datos desde un archivo Excel
    else:
        raise ValueError("Formato de archivo no soportado") # Lanza un error si el formato no es compatible
    print("Data cargada correctamente") # Imprime un mensaje indicando que los datos se cargaron correctamente
    return df # Devuelve el DataFrame con los datos cargados

def clean_data(df):
    """
    Limpiamos los datos.

    Args :
        df (pd.DataFrame) : DataFrame con los datos a limpiar.

    Returns :
        pd.DataFrame: DataFrame con los datos limpios
    """
    df['price'] = df['price'].replace(r"[\$,]", "", regex=True).astype(float) # Limpia y convierte la columna de precios a tipo float
    df['number_reviews'] = df['number_reviews'].apply(lambda x: int(''.join(filter(str.isdigit, str(x))))) # Toma únicamente el valor correspondiente al número de reviews
    print("Data cleaned successfully")  # Imprime un mensaje indicando que los datos se limpiaron correctamente.
    return df # Devuelve el DataFrame con los datos limpiados

def save_clean_data(df, output_path):
    """
    Guardamos los datos limpios en un archivo CSV o Excel.

    Args :
        df (pd.DataFrame) : DataFrame con los datos a guardar.
        output_path (str) : Ruta del archivo de salida.

    Raises :
        ValueError: Si el formato del archivo no es soportado.
    """
    if output_path.endswith('.csv'):
        df.to_csv(output_path, index=False)  # Guarda los datos en un archivo CSV sin índice
    elif output_path.endswith('.xlsx'):
        df.to_excel(output_path, index=False)  # Guarda los datos en un archivo Excel sin índice
    else:
        raise ValueError("Formato de archivo no soportado")  # Lanza un error si el formato no es compatible
    print(f"La data procesado fue almacenada en {output_path}")  # Imprime un mensaje indicando que los datos se guardaron correctamente

if __name__ == "__main__":
    data_path = "data/raw/products.csv" # Define la ruta del archivo de datos
    output_path = "data/processed/clean_products.csv" # Define la ruta del archivo de datos limpios

    df = load_data(data_path) # Carga los datos
    df = clean_data (df) # Limpia los datos
    os.makedirs("data/processed", exist_ok=True) # Crea el directorio de salida si no existe
    save_clean_data(df, output_path) # Guarda los datos limpios