matriz1=[]
matriz2=[]
matriz_soma=[]

#Preenche Matriz ( repetir sempre que preecher matriz)
for i in range(3):
    linha=[]
    for j in range(3):
        linha.append(int(input(f"matriz1[{i}][{j}]=")))
    matriz1.append(linha)

#Preenche Matriz ( repetir sempre que preecher matriz)
for i in range(3):
    linha=[]
    for j in range(3):
        linha.append(int(input(f"matriz2[{i}][{j}]=")))
    matriz2.append(linha)

#preeencher matriz (repetir sempre que preencher a matriz)
for i in range(3):
    linha=[]
    for j in range(3):
        linha.append(matriz1[i][j] + matriz2[i][j])
    matriz_soma.append(linha)


print=("matriz soma: " )
for linha in matriz_soma:
    print(linha)

