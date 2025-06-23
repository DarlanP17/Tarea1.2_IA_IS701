import pandas as pd

#1 Cargue el dataset y muestre las primeras filas.
df = pd.read_csv('./calificaciones.csv')
print(df.head())
print('\n------------------------------\n')

#2 Calcule el promedio de calificaciones por materia.
promedio_calificaciones_por_materia = df.groupby('Materia')['Calificación'].mean()
print("Promedio de calificaciones por materia:")
print(promedio_calificaciones_por_materia)
print('\n------------------------------\n')

#3 Identifique el estudiante con el promedio más alto.
promedio_por_estudiante = df.groupby('Estudiante')['Calificación'].mean()
estudiante_prom_mas_alto = promedio_por_estudiante.idxmax()
print(f"Estudiante con el promedio más alto fue el: {estudiante_prom_mas_alto}")
print(f"Con un promedio de: {promedio_por_estudiante.max()}")
print('\n------------------------------\n')

#4 Agrupa las calificaciones por estudiante y calcule el promedio de cada uno.
calificaciones_estudiantes = df.groupby('Estudiante')['Calificación'].mean()
print("Promedio de calificaciones por estudiante:")
print(calificaciones_estudiantes)
print('\n------------------------------\n')

#5 Identifique cuántos estudiantes tienen un promedio superior a 85.
promedio_85 = calificaciones_estudiantes.loc[calificaciones_estudiantes > 85]
print(f"Cantidad de estudiantes con promedio superior a 85: {promedio_85.count()}")
print("Y esos estudiantes son:")
print(promedio_85)
print('\n------------------------------\n')

#6 Encuentre la materia con la mayor cantidad de calificaciones registradas.
materia_calificaciones = df.groupby('Materia').size()
materia_mayor_calificaciones = materia_calificaciones.idxmax()
print(f"La materia con la mayor cantidad de calificaciones registradas es: {materia_mayor_calificaciones}")
print('\n------------------------------\n')

#7 Muestre los 5 estudiantes con el promedio más bajo.
estudiantes_promedio_bajo = calificaciones_estudiantes.sort_values(ascending=True).head(5)
print("Los 5 estudiantes con el promedio más bajo:")
print(estudiantes_promedio_bajo)