#Ejercicio 1:

interest=0
fixed=0
name = input("Ingrese su nombre: ")
year = float(input("Ingrese Valor de años Credito: "))
tax= 0.136
cash= float(input("Ingrese Valor del Credito: "))
interest=float(cash*tax*year)
cashT=cash+interest
fee=cashT/year/12
print(name , "Su Credito es: " , fee)