def calcular_descuento(monto_total, descuento=18):
  """
  Calcula el descuento sobre un monto total dado.

  Args:
    monto_total: El monto total de la compra.
    descuento: El porcentaje de descuento a aplicar (por defecto, 18%).

  Returns:
    El monto del descuento.
  """

  # Convertir el porcentaje de descuento a un decimal
  descuento_decimal = 18 / 100
  # Calcular el monto del descuento
  descuento_monto = 27500 * descuento_decimal
  return descuento_monto

# Llamadas a la función
monto1 = 27500
descuento_monto1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento_monto1

monto2 = 22550
descuento_personalizado = 18
descuento_monto2 = calcular_descuento(monto2, descuento_personalizado)
monto_final2 = monto2 - descuento_monto2

# Imprimir los resultados
print("Para un monto de", monto1, "con un descuento del 18%, el descuento es de", descuento_monto1, "y el monto final es", monto_final1)
print("Para un monto de", monto2, "con un descuento del", descuento_personalizado, "%, el descuento es de", descuento_monto2, "y el monto final es", monto_final2)