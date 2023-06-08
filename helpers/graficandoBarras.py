import matplotlib.pyplot as plt

def graficarPromedio(dataframe, columnax,columnay, nombreGrafica):
    #1. definir lista de colores
    colores=['green','blue','orange','yellow']

    #2. obtener el promedio de los salarios
    promedio=dataframe.groupby(columnax)[columnay].mean()

    #3. comienzo a generar la grafica de barras
    plt.bar(promedio.index,promedio,color=colores)
    plt.xlabel("zona")
    plt.ylabel("Arboles promedio")
    plt.title("Promedio de siembra por zona")

    #4. guardar la grafica
    plt.savefig(f'./assets/img/{nombreGrafica}.png',dpi=300,bbox_inches='tight')
