import pandas as pd
from helpers.crearTablasHTML import crearTabla
from helpers.graficandoBarras import graficarPromedioSalarial
from helpers.graficandoTortas import graficarPromedioSalariales

tablaArboles =pd.read_csv("./data/Siembras.csv")

#filtrando o aplicando condiciones a mi dataframe 
santafeMayorSiembra=tablaArboles.query('(Ciudad== "Santa Fe de Antioquia")&(Arboles>=250)')
caucasia=tablaArboles.query ('Ciudad== "Caucasia"')
# print (caucasia)
belmira=tablaArboles.query('(Vereda== "Rio Arriba")|(Vereda=="La Salazar")')
# print (belmira)
bello=tablaArboles.query('(Vereda=="Quitasol")&(Ciudad== "Bello")')
datosEstadisticosBello=bello.describe()
print (datosEstadisticosBello)

caramanta=tablaArboles.query('(Ciudad== "Caramanta")&(Arboles>100)')
print(caramanta)

yarumal=tablaArboles.query('(Vereda== "Mallarino")&(Ciudad=="Yarumal")')
print (yarumal)

# #generando la tabla para el reporte
crearTabla(santafeMayorSiembra, "tbl_santafe")
crearTabla (caucasia, "tbl_caucasia")
crearTabla (belmira, "tbl_belmira")
crearTabla(bello, "tbl_bello")
crearTabla(datosEstadisticosBello, "tbl_belloEstadistica")
crearTabla (caramanta, "tbl_caramanta")
crearTabla(yarumal, "tbl_yarumal")

# #generando graficas 
# graficarPromedioSalarial(jubilados,'cargo','salario','promediojubilados')
# graficarPromedioSalariales(analista1, [20,30,40,50,60],'edad','salario','promedioAnalista1')

