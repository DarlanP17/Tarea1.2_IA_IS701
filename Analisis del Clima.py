import pandas as pd

#1 Cargue el dataset y conviértelo en un DataFrame.
df = pd.read_csv('./clima.csv')
print(df)
print('\n------------------------------\n')

#2 Calcule la temperatura promedio de cada ciudad.
temperatura_promedio = df.groupby('Ciudad')['Temperatura'].mean()
print("Temperatura promedio por ciudad:")
print(temperatura_promedio)
print('\n------------------------------\n')

#3 Determine el registro con la temperatura más alta y el más bajo en el dataset.
temperatura_mas_alta = df['Temperatura'].max()
temperatura_mas_baja = df['Temperatura'].min()

print(f"La temperatura más alta registrada fue de: {temperatura_mas_alta}°C")
print(f"La temperatura más baja registrada fue de: {temperatura_mas_baja}°C")
print('\n------------------------------\n')

#4 Identifique qué ciudad tuvo la temperatura más alta y cuál la más baja en todo el dataset.
ciudad_temp_mas_alta = df.loc[df['Temperatura'].idxmax(), 'Ciudad']
ciudad_temp_mas_baja = df.loc[df['Temperatura'].idxmin(), 'Ciudad']
print(f"La ciudad con la temperatura más alta fue: {ciudad_temp_mas_alta}")
print(f"La ciudad con la temperatura más baja fue: {ciudad_temp_mas_baja}")
print('\n------------------------------\n')

#5 Encuentre cuántos registros tienen una temperatura mayor a 30°C.
registros_mayor_30 = df.loc[df['Temperatura'] > 30, 'Temperatura'].count()
print(f"La cantidad de registros que tienen una temperatura mayor a 30°C son: {registros_mayor_30}")
print('\n------------------------------\n')

#6 Cuenta cuántos días en total hay registrados por cada ciudad.
dias_totales_por_ciudad = df.groupby('Ciudad')['Fecha'].nunique()
print("Días registrados por ciudad:")
print(dias_totales_por_ciudad)
print('\n------------------------------\n')
