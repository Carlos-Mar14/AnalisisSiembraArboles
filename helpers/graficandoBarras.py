import matplotlib.pyplot as plt

def graficarPromedioSalarial(dataframe, columnax,columnay, nombreGrafica):
    #1. definir lista de colores
    colores=['green','blue','orange','yellow']

    #2. obtener el promedio de los salarios
    salarioPromedio=dataframe.groupby(columnax)[columnay].mean()

    #3. comienzo a generar la grafica de barras
    plt.bar(salarioPromedio.index,salarioPromedio,color=colores)
    plt.xlabel("cargo")
    plt.ylabel("Salario Promedio")
    plt.title("salario Promedio por cargo")

    #4. guardar la grafica
    plt.savefig(f'./assets/img/{nombreGrafica}.png',dpi=300,bbox_inches='tight')
