import pdfkit

ruta_entrada = "/views/index.html"
ruta_salida = "/views/index.html/informe.pdf"

opciones = {
    "page-size": "Letter",
    "margin-top": "0mm",
    "margin-right": "0mm",
    "margin-bottom": "0mm",
    "margin-left": "0mm"
}

pdfkit.from_file(ruta_entrada, ruta_salida, options=opciones)