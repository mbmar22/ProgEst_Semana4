import edades

def leerDatos():
    try:
        edad = int(input("Dime tu edad: "))
        edades.agregar(edad)
    except ValueError:
        print("\nDebe ingresar un número entero.")

def menu():
    print("""
1. Ingresar edad.
2. Mostrar edad.
3. Clasificar edad.
0. Salir.
""")
    option = int(input("Digite una opción válida: "))
    return option

def main():
    while True:
        op = menu()
        if op == 1:
            leerDatos()
        elif op == 2:
            print(edades.mostrar())
        elif op == 3:
            edades.evaluarEdades()
        elif op == 0:
            print("\nCerrando programa...")
            break
        else:
            print("Ingrese un opción válida.")
            
main()