#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10. """
__version__ = "0.1.1"
__author__  = "Rafael"

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

for numero in numeros:
    print("{:-^18}".format(f"Tabuada de {numero}"))
    print()
    for outro_numero in numeros:
        operacao = numero * outro_numero
        print("{:^18}".format(f"{numero} x {outro_numero} = {operacao}"))
    print("\U0001F44C" * 15)
    print("{:_^20}".format(""))

