numeros=[]

for i in range (5):
    numeros.append(float(input(f"Digite o {i+1}º numero:")))

#sum- soma  
soma = sum(numeros)
print("A soma é",soma)
