'''
2. Paso de parámetros: por valor y por referencia
Práctica del tema
    1. Crea una función que reciba un salario numérico, aumente su parámetro y comprueba si cambió la variable original.
    2. Crea una función que reciba una lista de ventas y agregue una nueva venta mediante append().
    3. Explica por qué los dos ejercicios producen comportamientos diferentes.
'''

print("2. Paso de parámetros: por valor y por referencia.")
print("----- Ejercicio 1 -----")

def aumento_salario(salario):
    print("\n- Resultado -")
    print(f"Salario inicial: C${salario:.2f}")
    salario = salario + (salario * 0.1) # Salario más un aumento del 10%.
    print(f"Salario más aumento: C${salario:.2f}")

trabajador = float(input("Salario trabajador: "))
aumento_salario(trabajador)


print("\n----- Ejercicio 2 -----")

def lista_ventas(factura, producto):
    factura.append(producto)

productos_cliente = ["Pan", "Cebolla", "Carne", "Limonada"]

compra = "Paprika"
lista_ventas(productos_cliente, compra)

print(productos_cliente)


print("\n----- Ejercicio 3 -----")
print("Ambos ejercicios son diferentes porque uno trabaja con una variable y el otro con una lista.")