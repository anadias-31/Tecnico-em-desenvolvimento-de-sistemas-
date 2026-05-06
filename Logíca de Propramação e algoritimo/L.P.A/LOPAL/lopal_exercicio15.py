numeros=[]
soma=0
media=0

for i in range(8):
    num=int(input("Numeros:"))
    numeros.append(num)
    soma+=num

media=soma/8
for numero in numeros:
    if(numero>media):
        print(numero,">",media)
