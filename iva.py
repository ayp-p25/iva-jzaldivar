"""
Calcular IVA y total con IVA
"""

# Declaraciones
TASA_IVA = 0.16

# Entradas
cantidad = float(input("Cantidad: "))

# Proceso
iva = cantidad * TASA_IVA
total = cantidad + iva 


# Salidas
print("IVA", iva)
print("Total", total)
