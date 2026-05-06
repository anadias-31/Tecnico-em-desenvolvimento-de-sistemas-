#CODIGO RUIM

#nomes de variaveis confusas
a=float(input())
b=float(input())
c=float(input())
d=float(input())

#O que é x? 
x=(a+b+c+d)/4

#print muito superficial
if x >=7:
    print("ok")
elif x >= 5:
    print("Rec")
else:
    print("no")

#CLEAN CODE 01
nota1= float(input("Digite a nota: "))
nota2= float(input("Digite a nota: "))
nota3= float(input("Digite a nota: "))
nota4= float(input("Digite a nota: "))
media=(nota1+nota2+nota3+nota4)/4

print("Sua media é",media)

if media >= 7:
    print("Aprovado 🤩!!!")
elif media >= 5:
    print("Recuperação 😓")
elif media < 5:
    print("Reprovado ❌")
else:
    print("Dados invalidos!")

#CLEAN CODE 02
notas=[]

for i in range (4):
    notas.append(float(input(f"Digite a {i+1}ª nota:")))

#sum- soma 
#len- tamanho 
media = sum(notas)/len (notas)
print("Sua media é",media)

if media >= 7:
    print("Aprovado 🤩!!!")
elif media >= 5:
    print("Recuperação 😓")
elif media < 5:
    print("Reprovado ❌")
else:
    print("Dados invalidos!")
