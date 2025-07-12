#Faça uma lista que tem 10 valores que o usuário pedir e faça a soma desses valores.
try:
    valores = []
    for i in range(10):
        valor = float(input(f"Digite o valor {i+1}: "))
        valores.append(valor)
    soma = sum(valores)
except ValueError:
    print("Por favor, digite apenas números.")
else:
    print(f"A soma dos valores é: {soma}")
