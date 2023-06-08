import matplotlib.pyplot as plt

def create_bar_chart(ciudades, arboles, nombre):
    colores = ['blue', 'navy', 'teal', 'aqua']
    plt.rcParams.update({'font.size': 7})
    # Configuración del gráfico
    fig, ax = plt.subplots()
    ax.bar(ciudades, arboles)

    # Títulos y etiquetas
    ax.set_title('Recuento de Arboles por ciudad')
    ax.set_xlabel('ciudades')
    ax.set_ylabel('Recuento')

    plt.savefig(f'./assets/img/{nombre}.png', dpi=250)
    # Mostrar el gráfico
    plt.show()
   