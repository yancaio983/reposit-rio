#Crie um laço de repetição que faça a tabuada de multiplicação de 1 a 10.
for i in range(1,11):
    print(f"Tabuada do {i}:")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")