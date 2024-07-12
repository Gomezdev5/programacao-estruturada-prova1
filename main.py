def q1():
    """ Faça um programa que calcula a quantidade de divisores de um número (incluindo 1 e o próprio número) que são divisíveis por 3. """
   
    numero = int(input("Digite um numero"))
    contador = 0
      
    for i in range(1, numero + 1):
        if (numero % i == 0) and (i % 3 == 0):
           contador += 1
        
    if contador == 0:
        print("O número não possui divisores multiplos de 3")

    else:
        print("Quantidade de divisores divisiveis por 3:", contador)

def q2():
    """Escreva um programa que receba como entrada dois números inteiros e retorne a soma dos números positivos no intervalo definido por eles,
     considerando inclusive os extremos. """
    menor = int(input(""))
    maior = int(input(""))
    if menor > maior:
        menor, maior = maior, menor     
    soma = 0
    
    for i in range(menor, maior+1):
        if i > 0:
            soma += i
    print(soma)

def q3():
    pass

def q4():
    pass