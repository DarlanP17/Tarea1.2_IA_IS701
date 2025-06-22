import pandas as pd

#1 Cargue los datos en un DataFrame.
df = pd.read_csv('./ventas.csv')
print(df)
print('\n------------------------------\n')

#2 Calcule la cantidad total de productos vendidos por categoría.
cantidad_total = df.groupby('Producto')['Cantidad'].sum()
print("Cantidad total vendida por producto:")
print(cantidad_total)
print('\n------------------------------\n')

#3 Determine cuál es el producto con el mayor total de ventas.
ventas_por_producto = (df['Cantidad'] * df['Precio_Unitario'])
mayor_total_ventas = ventas_por_producto.groupby(df['Producto']).sum().idxmax()
print(f"Producto con mayores ventas: {mayor_total_ventas}")
print('\n------------------------------\n')

#4 Encuentre el precio promedio de los productos vendidos.
precio_promedio = df['Precio_Unitario'].mean()
print(f"Precio promedio de los productos: ${precio_promedio:.2f}")



