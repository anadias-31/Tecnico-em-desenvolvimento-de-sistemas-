saltos=[]
soma=0

for i in range (7):
    saltos.append(int(input("DIgite o valor do salto: ")))
print(saltos)
#todos os saltos na ordem em que foram realizados

#maior
maior=saltos[0]

for salto in saltos:
    if(salto> maior):
        maior=salto
print("O maior salto é: ", maior)

#menor
menor=saltos[0]

for salto in saltos:
    if(salto < menor):
        menor=salto
print("O menor salto é: ", menor)

#media
for  salto in saltos:
    if (salto != menor and salto != maior ):
        soma= soma+salto
        
media= soma/5
print("A média é:",media)

#media geral
soma=0

for salto in saltos:
    soma=soma+salto
media_geral= soma/7
print("Amédia geral é", media)
