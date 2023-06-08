import pandas as pd
import matplotlib.pyplot as plt

def graficar_torta(dataFrame, rangos, columnaInteresRango, columnaPromediar, nombre):
    df = dataFrame.copy()  # Copia explícita del DataFrame
    
    plt.figure()
    
    df['rangoNuevo'] = pd.cut(df[columnaInteresRango], bins=rangos)
    
    arboles_por_hectarea = df.groupby('rangoNuevo')[columnaPromediar].sum()
    
    arboles = arboles_por_hectarea.values
    hectareas = arboles_por_hectarea.index
    
    plt.pie(arboles, labels=hectareas, autopct='%1.1f%%')
    
    plt.savefig(f'./assets/img/{nombre}.png', dpi=250)
