import pandas as pd #para manejar datos
import matplotlib.pyplot as plt #para hacer gráficos

df = pd.read_csv("produccion_bovina.csv", sep=";") #cargamos el dataset desde el archivo csv, ";" porque archivo usa punto y coma como separador
# #convertimos la columna de fecha de texto a formato fecha real, dayfirst=True porque es el formato en argentina
# df["Fecha_Medicion"] = pd.to_datetime(df["Fecha_Medicion"], dayfirst=True)
# df["año"] = df["Fecha_Medicion"].dt.year #creamos la columna año para analizar por año
# df["mes"] = df["Fecha_Medicion"].dt.month #creamos la columna mes para analizar por mes

# produccion_anual = df.groupby("año")["producción_(kg/ha)"].sum() #agrupamos por año y sumamos la produccion total por año
# print(produccion_anual)

# #Graficamos
# produccion_anual.plot(marker="o")  #marker="o" agrega puntos en cada año para visualizar mejor
# plt.title("Producción por Año") #título del gráfico
# #etiquetas de lso ejes
# plt.xlabel("Año") 
# plt.ylabel("Producción")

# plt.savefig("produccion_por_año.png") #guardamos el gráfico
# plt.show() #para mostrar el gráfico

# #Agrupamos por año y sumamos el neto (cuánto se ganó o perdió cada año)
# resultado_anual = df.groupby("año")["Resultado_Neto"].sum()
# print(resultado_anual)

# resultado_anual.plot(marker="o")

# plt.title("Resultado Neto por Año")
# plt.xlabel("Año")
# plt.ylabel("Resultado Neto")
# plt.savefig("resultado_neto_por_año.png")
# plt.show()

# comparacion =pd.DataFrame({
#     "Producción": produccion_anual,
#     "Resultado": resultado_anual
# })
# print(comparacion)

# #Para saber qué actividad es mas rentable (promedio de ganancia)
# resultado_actividad = df.groupby("Id_Actividad")["Resultado_Neto"].mean()
# print(resultado_actividad)

# resultado_actividad.plot(kind="bar")
# plt.title("Resultado Neto Promedio por Actividad")
# plt.xlabel("Actividad")
# plt.ylabel("Resultado Neto Promedio")
# plt.savefig("estimación_activ_mas_rentable.png")
# plt.show()

#producción promedio por actividad
# produccion_actividad = df.groupby("Id_Actividad")["producción_(kg/ha)"].mean()
# print(produccion_actividad)

#Ingresos vs costos por actividad
ingresos_vs_costos = df.groupby("Id_Actividad")[["Ingreso_Bruto", "Costos_Directos", "Costos_Indirectos"]].mean()
print(ingresos_vs_costos)


#print(df.head()) #muestra las primeras filas del dataset p/verificar que esten bien los datos
#print(df.info()) #muestra info gral del dataset (tipos de datos, cant de filas, etc)

