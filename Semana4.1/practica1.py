'''
1. Ámbito de variables y funciones
Práctica del tema
    1. Crea una variable global llamada nombre_empresa y muéstrala dentro de una función.
    2. Crea una función con una variable local llamada total. Intenta utilizarla fuera de la función, observa el error y explícalo.
    3. Crea un contador global y modifícalo desde una función mediante global.
'''

'''
def calcular_total():
    global nombre_empresa
    total += 1

print(total)

No funciona ya que "total" no está definido fuera de la función.
'''

print("1. Ámbito de variables y funciones.")
total = int(input("Ingrese un número entero: "))

def calcular_total():
    global total
    total += 1
    return total # o también print("Se ha incrementado el valor satisfactoriamente.")

calcular_total()

print("\n----- Resultados -----")
print(f"Total = {calcular_total()}")