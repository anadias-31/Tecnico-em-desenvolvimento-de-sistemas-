numero = int(input(" DIgite um numero: "))
multiplicacao = 0

for i in range(1,11,+1):
    multiplicacao = numero*i
    print("\n",numero,"*",i, "=", multiplicacao)