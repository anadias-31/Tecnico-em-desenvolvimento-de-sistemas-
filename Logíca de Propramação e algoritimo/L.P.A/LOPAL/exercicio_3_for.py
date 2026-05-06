numero= int(input("Digite um numero:"))
fatorial=1


for i in range (numero,0,-1):
    fatorial = fatorial * i
    
print(numero,"! =",fatorial)