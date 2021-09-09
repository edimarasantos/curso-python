'''
Escreva a função maior_primo que
recebe um número inteiro maior ou igual a 2 como parâmetro e
devolve o maior número primo menor ou igual ao número passado à função

Dica: escreva uma função éPrimo(k) e
faça um laço percorrendo os números até o número dado checando se o número é primo ou não;
se for, guarde numa variável. Ao fim do laço, o valor armazenado na variável é o maior primo encontrado.
'''
def primo(k):
    i = 1
    cont = 0
    while i <= k:
        if k % i == 0:
            cont = cont + 1
        i = i + 1
        if cont > 2:
            return False
    return True
            
def maior_primo(n):
    k = n
    while k > 1 and primo(k) == 0:
        k = k - 1
    return k

    
    
