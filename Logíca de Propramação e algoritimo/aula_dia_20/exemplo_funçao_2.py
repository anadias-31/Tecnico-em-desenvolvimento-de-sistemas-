#Criar a função
def calcular_media(nota1,nota2,nota3,nota4,):
    media= (nota1+nota2+nota3+nota4)/4
    print("A sua media é: ",media)

#Chamar função media
calcular_media(10,9,8,9)

#Chamar função pro 2º aluno
n1=int(input("Digite sua nota 1: "))
n2=int(input("Digite sua nota 2: "))
n3=int(input("Digite sua nota 3: "))
n4=int(input("Digite sua nota 4: "))

calcular_media(n1,n2,n3,n4)



