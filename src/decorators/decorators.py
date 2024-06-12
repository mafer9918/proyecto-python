import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def medir_tiempo_ejecucion(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f"{func.__name__} ejecutada en {elapsed_time: .4f} segundos")
        return result
    return wrapper

def registrar_ejecucion_funcion(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Corriendo {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Completado {func.__name__}")
        return result
    return wrapper
