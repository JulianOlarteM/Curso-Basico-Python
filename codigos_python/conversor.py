pesos_col = input("¿Cuantos pesos colombianos tienes?")
pesos_col = float(pesos_col)
valor_dolar = 3875
dolares = pesos_col/ valor_dolar
dolares = round(dolares,2) #redondear a dos decimales
dolares = str(dolares)
print("tienes $ " + dolares + " dolares")
