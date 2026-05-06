linhas= int(input("quantidade de linhas (i):"))
colunas= int(input("quantidade de colunas(j):"))
matriz= []

for i in range (linhas):
    linha=[]
    for j in range(colunas):
        linha.append(int(input(f"M[{i}][{j}]=")))
    matriz.append(linha)
print("matriz preenchida: ")
for linha in matriz:
    print(linha)