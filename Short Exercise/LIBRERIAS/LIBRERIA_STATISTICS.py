import statistics
import csv
monthly_sales = {}
with open('monthly.csv', mode='r')as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(sales)
#Sacar la Media
media_ventas = statistics.mean(sales)
print(f"La media es: {media_ventas}")

#Sacar la mediana
mediana_ventas = statistics.median(sales)
print(f"La mediana es: {mediana_ventas}")

# Sacar la Moda
moda_ventas = statistics.mode(sales)
print(f"La moda es: {moda_ventas}")

#Sacar la Desviacion Estandar
desviacion_estandar = statistics.stdev(sales)
print(f"La Desviacion estandra es: {desviacion_estandar}")

#Sacar la Varianza
varianza = statistics.variance(sales)
print(f"La varinza es: {varianza}")

#Maximo Minimo De ventas y Rango es decir , diferencia entre estos dos

max_sales = max(sales)
min_sales = min(sales)

rango_ventas = max_sales - min_sales

print(f"Valor Maximo Registrado Es : {max_sales},  Valor Minimo Registrado: {min_sales}")
print(f"Rango De Valor Es decir diferencia entre el maximo y el minimo : {rango_ventas}")
