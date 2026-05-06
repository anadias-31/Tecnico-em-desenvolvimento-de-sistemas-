#Revisão matrizes 1
#solicitar a quantidade de linhas
#solicitar a quantidade de colunas
#Preencher a matriz
#calcular a soma de todos
#----------------------------------


linhas=int(input("Digite a quantidade de linhas:"))
colunas=int(input("Digite o numero de colunas"))
matriz=[]
soma=0

for i in range(linhas):
    linha=[]
    for j in range(colunas):
        linha.append (int(input(f"Digite o valor da posição [{i}][{j}]")))
    matriz.append(linha)
    
for i in range(linhas):
    for j in range (colunas):
        soma += matriz[i][j]
print(soma)


