print("ejemplos de bucles")

empleados = [
    {"nombre": "Ana", "sueldo": 3000, "activo": True},
    {"nombre": "Luis", "sueldo": 2500, "activo": False},
    {"nombre": "Sofía", "sueldo": 3200, "activo": True},
    {"nombre": "Pedro", "sueldo": 2800, "activo": True},
]

total_sueldos = 0

for empleado in empleados:
    if not empleado["activo"]:
        continue  # Saltar empleados inactivos
    total_sueldos += empleado["sueldo"]

print(f"Suma total de sueldos activos: ${total_sueldos}")