#Revisão vetores -1
#Solicitar ao usuario a quantidade de numeros
#Preeencher vetor
#Percorrer o vetor e calcular a soma dos numeros
#Exibir soma
#-----------------------------------------------

vetor=[]
soma=0
qtd=int(input("Digite a quantidade de numeros:"))

for i in range(qtd):
    vetor.append(int(input("Digite os numeros")))

for numero in vetor:
    soma += numero
print(soma)



