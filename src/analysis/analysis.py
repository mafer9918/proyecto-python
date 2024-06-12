import pandas as pd
import os
import re

def load_data(data_path):
    if data_path.endswith(".csv"):
        df = pd.read_csv(data_path)
    elif data_path.endswith(".xlsx"):
        df = pd.read_excel(data_path)
    else:
        raise ValueError("Formato de archivo no soportado")
    print("Data cargada correctamente")
    return df

def clean_data(df):
    df['price'] = df['price'].replace(r"[\$,]", "", regex=True).astype(float)
    df['number_reviews'] = df['number_reviews'].apply(lambda x: int(''.join(filter(str.isdigit, str(x)))))
    return df

def save_clean_data(df, output_path):
    if output_path.endswith(".csv"):
      df.to_csv(output_path, index = False)
    elif output_path.endswith(".xlsx"):
      df.to_excel(output_path, index = False)
    else:
        raise ValueError("Formato de archivo no soportado")
    print(f"La data limpiada fue guardada en {output_path}")

if __name__ == "__main__":
    data_path = "data/raw/products.csv"
    output_path = "data/processed/clean_products.csv"

    df = load_data(data_path)
    df = clean_data (df)
    print(df)
    os.makedirs("data/processed", exist_ok=True)
    save_clean_data(df, output_path)