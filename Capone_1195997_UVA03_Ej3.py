valorInicial = input("Ingrese el valor al que se le debe calcular el IVA: ")

valorIva = float(valorInicial) * 0.21

valorTotal = float(valorInicial) + valorIva

print("El total a pagar es: €", round(valorTotal, 2))

