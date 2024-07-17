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
    n_servidores = int(input("Número de servidores:"))
    n__und_capacidade = int(input("Unidades de capacidade do banco de dados:"))
    n_armazenamento_dados = int(input("Armazenamento de dados (em GB):"))
    n_dados_de_entrada_saida = int(input("Transferência de dados de entrada e saída (em GB):"))

    servidor = 500
    unidade_capacidade = 100
    armazenamento_dados_GB = 0.10
    trans_dado = 0.05

    custo_servidores = n_servidores * servidor
    custo_capacidade = n__und_capacidade * unidade_capacidade
    custo_armazenamento = n_armazenamento_dados * armazenamento_dados_GB
    custo_trans_dados = n_dados_de_entrada_saida * trans_dado

    soma1 = float(custo_armazenamento+custo_capacidade+custo_servidores+custo_trans_dados)
    
    if soma1 > 10000:
        print("O custo total mensal está acima do limite.")
    else:
        print("O custo total mensal estimado para a infraestrutura é de R$","{:.2f}".format(soma1))

    
def q4():
    pass