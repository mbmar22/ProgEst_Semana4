# Clasificar edades según su categoría.

edades = []

def agregar(persona):
    if persona < 0 or persona >= 110:
        print("\nIngrese una edad válida.")
    else:
        edades.append(persona)

def mostrar():
    return edades

def evaluarEdades():
    for edad in edades:
        if edad >= 0 and edad <= 4:
            print(f"{edad}, es infante.")
        if edad >= 5 and edad <= 13:
            print(f"{edad}, es in niñez.")
        if edad >= 14 and edad <= 17:
            print(f"{edad}, es adolescencia.")
        if edad >= 18 and edad <= 35:
            print(f"{edad}, es adulto joven.")
        if edad >= 36 and edad <= 64:
            print(f"{edad}, es adulto.")
        if edad >= 65 and edad < 110:
            print(f"{edad}, es tercera edad.")  