#criando uma variavel numero
numero = 10

#criando uma variavel textual
nome = "Gabriel"

#usuario inserir um texto
nome_completo = input("Digite seu nome")

#Usuario digitar um numero inteiro
idade = int(input("Digite sua idade"))

#usuario digitar um numero decimal
salario = float(input("Digite seu salario"))

#estrutura de repetição
if(salario > 1500 and idade >= 18):
    print("Você pode ter sua carta")
elif(salario < 1500 and idade < 18):
    print("Você nao pode ter sua carta")
else:
    print("Invalido")

#exemplo- exercicio 2
turno = input("Digite seu turno(M/V/N;")

if (turno == "M" ):
    print("Bom dia 🌤️")
elif (turno == "V"):
    print("Boa tarde ☕")
elif(turno == "N"):
    print("Boa noite 🛏️")
else:
    print("Invalido")

#estrutura de repetição
for i in range (56): #sempre +1
    print(i) 

for i in range (1,11,+2): #vai rodar de 1 á 10 pulando de 2 em 2 
    print(i)

#usuario escolhe o fim e o inicio 
inicio= int(input("Digite o inicio"))
fim= int(input("Diogite o fim"))

for i in range(inicio, fim+1): #+1 serve para terminar no numero que o usuario digitar
    print(i)

#vetor
nomes=[]
#preeencher nomes
for i in range(5):
    nomes.append(input("Digite os nomes"))

#exibir nomes
for nome in nomes:
    print(nome)