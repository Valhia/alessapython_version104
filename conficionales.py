print("ejemplos de condicionales")

valores = [5, 8, 12, 7]
if all(x > 3 for x in valores):
    print("Todos los valores son mayores que 3")
if any(x % 2 == 0 for x in valores):
    print("Al menos un valor es par")