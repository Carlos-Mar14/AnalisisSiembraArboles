import pandas as pd
import matplotlib.pyplot as plt

def graficarPromedioSalariales(dataFrame, rangos, columnaInteresRango, columnaaPromediar, nombreGrafica):
    #1. separo de graficas anteriores
    figura=plt.figure()

    #2. crear un a nueva columna en el dataframe con los rangos de interes
    dataFrame['rangoNuevo']=pd.cut(dataFrame[columnaInteresRango],bins=rangos)


    #3. calcular la suma de los salarios por cada rango
    salarioPorRango=dataFrame.groupby('rangoNuevo')[columnaaPromediar].sum()

    #4. obtener datos de salario y rango de edad
    salario=salarioPorRango.values
    rangoEdad=salarioPorRango.index

    #5. creando la torta
    plt.pie(salario,labels=rangoEdad,autopct='%1.1f %%')
    plt.title("Distribucion de salarios por rango de edad")

    plt.savefig(f'./assets/img/{nombreGrafica}.png',dpi=300,bbox_inches='tight')

