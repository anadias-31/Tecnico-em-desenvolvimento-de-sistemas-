positivo=0
negativo=0
for i in range(10):
    num=int(input("Digit um numeros: "))
    if(num<0):
        negativo += 1
    else:
        positivo += 1
print("Há",positivo,"numeros positivos e ",negativo,"numeros negativos")

