'''
Receba um número inteiro positivo na entrada e
imprima os n primeiros números ímpares naturais.
Para a saída, siga o formato do exemplo abaixo.
'''
n = int(input("Digite o valor de n: "))
contador = 0
impar = 1

while contador < n:
    print(impar)
    contador = contador + 1
    impar = impar + 2
