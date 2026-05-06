matriz=[
    ["laranja","roma","maça","limao","caqui"],
    ["beringela","batata","pimentão","pimenta","pepino"]
]
print(matriz[0]) #escreve a linha das frutas
print(matriz[1]) #escreve a linha dos legumes

print(matriz[0][2]) #escreve maça
print(matriz[1][3]) #escreve pimenta

#repeteco
print("frutas:")
print(matriz[0][0]) 
print(matriz[0][1]) 
print(matriz[0][2]) 
print(matriz[0][3]) 
print(matriz[0][4]) 

print("legumes:")
print(matriz[1][0]) 
print(matriz[1][1]) 
print(matriz[1][2]) 
print(matriz[1][3]) 
print(matriz[1][4]) 

#for 1
for j in range (4):
    matriz[0][j]

for j in range (4):
    matriz[1][j]

#for 2
print("Matriz completa: ")
for i in range (2):#linha
    for j in range (5):#coluna
        print(matriz[i][j])
    