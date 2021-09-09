'''
Escreva a função vogal que recebe um único caractere como parâmetro e
devolve True se ele for uma vogal e
False se for uma consoante.
s valores True e False devolvidos devem ser do tipo bool (booleanos), e não strings

Dica: Lembre-se que para passar uma vogal como
parâmetro ela precisa ser um texto, ou seja, precisa estar entre aspas.
'''

def vogal(v):
    verdade = True
    falso = False
    if v == "a" or v == "A" or v == "e" or v == "E" or v == "i" or v == "I" or v == "o" or v == "O" or v == "u" or v == "U":
        return verdade
    else:
        return falso
    
    
