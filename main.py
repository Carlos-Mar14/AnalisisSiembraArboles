import pandas as pd
from helpers.crearTablasHTML import crearTabla
from helpers.graficandoBarras import graficarPromedio
from helpers.graficandoTortas import graficar_torta
from helpers.graficandoHistogram import grafica_lineal_serie_tiempo
from helpers.graficoBarrasapiladas import create_bar_chart

tablaArboles =pd.read_csv("./data/Siembras.csv")

santafeMayorSiembra=tablaArboles.query('(Ciudad== "Santa Fe de Antioquia")&(Arboles>=250)')
caucasia=tablaArboles.query ('Ciudad== "Caucasia"')
belmira=tablaArboles.query('(Vereda== "Rio Arriba")|(Vereda=="La Salazar")')
bello=tablaArboles.query('(Vereda=="Quitasol")&(Ciudad== "Bello")')
datosEstadisticosBello=bello.describe()
caramanta=tablaArboles.query('(Ciudad== "Caramanta")&(Arboles>100)')
yarumal=tablaArboles.query('(Vereda== "Mallarino")&(Ciudad=="Yarumal")')

crearTabla(yarumal, "tbl_yarumal")
crearTabla(santafeMayorSiembra, "tbl_santafe")
crearTabla(caucasia, "tbl_caucasia")
crearTabla(bello, "tbl_bello")
crearTabla(belmira, "tbl_belmira")
crearTabla(tablaArboles,"tbl_tablaArboles")
crearTabla(caramanta,"tbl_caramanta")


graficarPromedio(tablaArboles,'Ciudad','Arboles','promediArboles')

graficar_torta(caramanta, [300, 800, 1300, 1800, 2300, 2800, 3200], 'Arboles', 'Hectareas', 'datosCaramanta')

tablaArboles['Fecha'] = pd.to_datetime(tablaArboles['Fecha'])
serie_tiempo = tablaArboles.set_index('Fecha')['Arboles']
fechas = pd.date_range('2023-01-01', periods=10, freq='M')
valores = [10, 15, 12, 8, 20, 18, 13, 16, 11, 9]
grafica_lineal_serie_tiempo(serie_tiempo, 'Fecha', 'Arboles', 'Serie de Tiempo de Arboles')


ciudades = tablaArboles['Ciudad'].tolist()
arboles = tablaArboles['Arboles'].tolist()
nombre = 'barrastodaslaszonas'
create_bar_chart(ciudades, arboles, nombre)
