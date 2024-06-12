from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Informe de Análisis de Laptops', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_image(self, image_path, width):
        self.image(image_path, x=None, y=None, w=width)
        self.ln(10)

def replace_special_characters(text):
    replacements = {
        '\u2018': "'",
        '\u2019': "'",
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    return text

pdf = PDF()
pdf.add_page()

pdf.chapter_title('Análisis de Precios por Marca')
pdf.chapter_body(replace_special_characters('En este análisis, hemos calculado el precio medio de laptops agrupadas por marca. El siguiente gráfico muestra la comparación.'))
pdf.add_image('assets/precio_por_marca.png', width=180)

pdf.chapter_title('Análisis de Calificaciones por Marca y Reviews')
pdf.chapter_body(replace_special_characters('Esta figura presenta un gráfico de dispersión, que ilustra las calificaciones de los clientes para diversas marcas tecnológicas. El eje x enumera las marcas, mientras que el eje y muestra el ‘Rating Máximo’ que va de 0 a 4. Los puntos de datos reflejan las calificaciones asignadas a cada marca y la intensidad de color de cada punto corresponde al número de reseñas recibidas, proporcionando una indicación de la popularidad y la percepción de calidad de la marca entre los consumidores.'))
pdf.add_image('assets/rating_por_marca.png', width=180)
pdf.output('informe/informe_analisis_laptops.pdf')
