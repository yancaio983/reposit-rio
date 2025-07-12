#Faça uma lista que tenha 100 números aleatórios entre 0 a 100
import random
lista_numeros = [random.randint(0, 100) for _ in range(100)]
print(lista_numeros)