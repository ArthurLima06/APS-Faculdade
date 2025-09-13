def soma(pNumero1,pNumero2):
    return pNumero1 + pNumero2
    
def subtracao(pNumero1,pNumero2):
    return pNumero1 - pNumero2

def multiplicacao(pNumero1,pNumero2):
    return pNumero1 * pNumero2

def divisao(pNumero1,pNumero2):
    print(pNumero1 / pNumero2)

def tabuada(pNumero):
    for i in range(11):
        print(f"{i} x {pNumero} = {i * pNumero}")

#somaLambda = lambda pNumero1,pNumero2: pNumero1 + pNumero2