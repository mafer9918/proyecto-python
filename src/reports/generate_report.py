from fpdf import FPDF  # Importamos la clase FPDF para crear PDFs
import os  # Importamos os para manejo del sistema de archivos

class PDF(FPDF):
    """
    Clase PDF personalizada que hereda de FPDF para generar un informe en PDF.
    """

    def header(self):
        """
        Método para agregar el encabezado al PDF.
        """
        self.set_font('Arial', 'B', 12) # Establece la fuente a Arial, negrita, tamaño 12.
        self.cell(0, 10, 'Informe de Análisis de Laptops', 0, 1, 'C') # Agrega una celda a la página del PDF

    def chapter_title(self, title):
        """
        Método para agregar un título de capítulo al PDF.
        """
        self.set_font('Arial', 'B', 12) # Establece la fuente a Arial, negrita, tamaño 12.
        self.cell(0, 10, title, 0, 1, 'L') # Agrega una celda con el título del capítulo
        self.ln(10) # Agrega un espacio vertical de 10 puntos después del título del capítulo.

    def chapter_body(self, body):
        """
        Método para agregar el cuerpo de un capítulo al PDF.
        """
        self.set_font('Arial', '', 12) # Establece la fuente a Arial, normal, tamaño 12.
        self.multi_cell(0, 10, body) # Agrega el cuerpo del capítulo en celdas que se ajustan automáticamente.
        self.ln() # Agrega un salto de línea después del cuerpo del capítulo.

    def add_image(self, image_path, width):
        if os.path.exists(image_path):  # Verifica si la imagen existe
            self.image(image_path, x=None, y=None, w=width) #Agrega una imagen al PDF
            self.ln(10) # Agrega un espacio vertical de 10 puntos después del título del capítulo.
        else:
            print(f"La imagen '{image_path}' no existe. No se agregará al informe.")

def replace_special_characters(text):
    """
    Método para reemplazar caracteres especiales en un texto.
    
    Args :
        text (str) : Texto en el que reemplazar los caracteres especiales.

    Returns :
        str: Texto con los caracteres especiales reemplazados.
    """
    replacements = {
        '\u2018': "'",  # Reemplaza el carácter Unicode de comilla simple izquierda por una comilla simple.
        '\u2019': "'",  # Reemplaza el carácter Unicode de comilla simple derecha por una comilla simple.
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)  # Reemplaza cada carácter especial en el texto con su reemplazo.
    return text  # Devuelve el texto con los caracteres especiales reemplazados.

# Crear instancia del PDF
pdf = PDF()
pdf.add_page()

# Agregar título,cuerpo e imagen del primer capítulo
pdf.chapter_title('Análisis de Precios por Marca')
pdf.chapter_body(replace_special_characters('En este análisis, hemos calculado el precio medio de laptops agrupadas por marca. El siguiente gráfico muestra la comparación.'))
pdf.add_image('assets/precio_por_marca.png', width=180)

# Agregar título,cuerpo e imagen del segundo capítulo
pdf.chapter_title('Análisis de Calificaciones por Marca y Reviews')
pdf.chapter_body(replace_special_characters('Esta figura presenta un gráfico de dispersión, que ilustra las calificaciones de los clientes para diversas marcas tecnológicas. El eje x enumera las marcas, mientras que el eje y muestra el ‘Rating Máximo’ que va de 0 a 4. Los puntos de datos reflejan las calificaciones asignadas a cada marca y la intensidad de color de cada punto corresponde al número de reseñas recibidas, proporcionando una indicación de la popularidad y la percepción de calidad de la marca entre los consumidores.'))
pdf.add_image('assets/rating_por_marca.png', width=180)
pdf.output('informe/informe_analisis_laptops.pdf')

# Verificar si las imágenes existen antes de guardar el informe
if os.path.exists('assets/precio_por_marca.png') and os.path.exists('assets/rating_por_marca.png'):
    pdf.output('informe/informe_analisis_laptops.pdf')
else:
    print("No se pudo generar el informe porque una o ambas imágenes no existen.")
