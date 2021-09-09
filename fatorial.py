'''
Escreva um programa que receba um número naturaln na entrada e
imprima n! (fatorial) na saída.
Dica: lembre-se que o fatorial de 0 vale 1!
'''
n = int(input("Digite o valor de n: "))
contador = 1
fatorial = 1

while contador <= n:
    fatorial = fatorial * contador
    contador = contador + 1
print(fatorial)
