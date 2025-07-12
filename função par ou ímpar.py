#Crie uma função que recebe um número inteiro e retorna se ele é par ou ímpar.
def par_ou_impar(numero):
        if numero % 2 == 0:
            return "par"
        elif numero % 2 != 0:
            return "ímpar"
print(par_ou_impar(numero=int(input("Digite um número inteiro: "))))