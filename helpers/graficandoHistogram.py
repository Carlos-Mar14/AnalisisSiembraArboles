import matplotlib.pyplot as plt

def grafica_lineal_serie_tiempo(datos, etiqueta_x, etiqueta_y, titulo):
    # Crear la figura y el eje
    fig, ax = plt.subplots()

    # Graficar la serie de tiempo
    ax.plot(datos.index, datos.values)

    # Configurar etiquetas y título
    ax.set_xlabel(etiqueta_x)
    ax.set_ylabel(etiqueta_y)
    ax.set_title(titulo)

    # Rotar las etiquetas del eje x para mayor legibilidad (opcional)
    plt.xticks(rotation=45)

    # Mostrar la gráfica
    
    plt.savefig(f'./assets/img/{titulo}.png', dpi=250)