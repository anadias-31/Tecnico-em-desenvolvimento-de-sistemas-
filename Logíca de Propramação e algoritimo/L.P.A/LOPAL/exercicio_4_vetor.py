vetor=[]
invertido=[0,0,0,0,0]

for i in range (5):
    num=int(input("Digite um numero:"))
    vetor.append(num)
for i in range (5):
    invertido[i] = vetor[4-i]

print(invertido)

