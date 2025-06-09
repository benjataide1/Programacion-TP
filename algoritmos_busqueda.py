import time
import random
import matplotlib.pyplot as plt



def producto_mas_vendido(ventas):
    max_producto = None      # O(1) – asignación inicial
    max_cantidad = 0         # O(1) – asignación inicial

    # Primer bucle: se ejecuta n veces (una por cada producto)
    for producto in ventas:  # O(n)
        # O(1) – se ejecuta en cada iteración del bucle externo
        cantidad = 0

        # Segundo bucle anidado: también se ejecuta n veces
        for otro_producto in ventas:  # O(n)
            if producto == otro_producto:   # O(1) – comparación
                cantidad += 1              # O(1) – suma
                if cantidad > max_cantidad:  # O(1) – comparación
                    max_producto = producto    # O(1) – asignación
                    max_cantidad = cantidad    # O(1) – asignación

    return max_producto, max_cantidad   # O(1) – operación final


#! Bucle anidado sobre ventas → O(n²)

#! Las demás operaciones son O(1), no afectan el crecimiento total

#? T(n) = O(n²)




def producto_mas_vendido_rapido(ventas):
    conteo = {}  # O(1) – creación del diccionario

    for producto in ventas:  # O(n)
        if producto in conteo:      # O(1) – acceso a diccionario (promedio)
            conteo[producto] += 1   # O(1) – suma
        else:
            conteo[producto] = 1    # O(1) – asignación

    # Esta línea recorre todos los productos una vez para encontrar el máximo → O(n)
    max_producto = max(conteo, key=conteo.get)  # O(n)

    # Acceder a un valor en el diccionario → O(1)
    return max_producto, conteo[max_producto]  # O(1)


#! El bucle for producto in ventas recorre la lista una vez → O(n)

#! Cada acceso al diccionario es O(1) en promedio (aunque puede ser peor en casos extremos, no se considera para Big-O estándar)

#! max(conteo, key=conteo.get) es otro recorrido completo del diccionario → O(n)

#? T(n) = O(n) + O(n) = O(n)



# Algoritmo lento
def producto_mas_vendido_lento(ventas):
    max_producto = None
    max_cantidad = 0
    for producto in ventas:
        cantidad = 0
        for otro in ventas:
            if producto == otro:
                cantidad += 1
        if cantidad > max_cantidad:
            max_producto = producto
            max_cantidad = cantidad
    return max_producto, max_cantidad

# Algoritmo rápido
def producto_mas_vendido_rapido(ventas):
    conteo = {}
    for producto in ventas:
        if producto in conteo:
            conteo[producto] += 1
        else:
            conteo[producto] = 1
    max_producto = max(conteo, key=conteo.get)
    return max_producto, conteo[max_producto]

# Generador de datos
def generar_datos(n):
    productos = ["A", "B", "C", "D", "E"]
    return [random.choice(productos) for _ in range(n)]

# Medición de tiempo
def medir_tiempo(func, ventas):
    inicio = time.time()
    func(ventas)
    fin = time.time()
    return fin - inicio

# Tamaños para probar
tamaños = [1000, 2000, 5000, 10000]

tiempos_lento = []
tiempos_rapido = []

for n in tamaños:
    ventas = generar_datos(n)
    tiempos_lento.append(medir_tiempo(producto_mas_vendido_lento, ventas))
    tiempos_rapido.append(medir_tiempo(producto_mas_vendido_rapido, ventas))

# Gráfico
plt.plot(tamaños, tiempos_lento, label="Algoritmo Lento (O(n²))", color="red", marker="o")
plt.plot(tamaños, tiempos_rapido, label="Algoritmo Rápido (O(n))", color="green", marker="o")
plt.title("Comparación de tiempos de ejecución")
plt.xlabel("Cantidad de ventas")
plt.ylabel("Tiempo (segundos)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("comparacion_algoritmos.png")  # Guarda la imagen
plt.show()

