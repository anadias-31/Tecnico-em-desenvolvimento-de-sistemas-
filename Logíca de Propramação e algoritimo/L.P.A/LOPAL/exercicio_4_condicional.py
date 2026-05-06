ladoA= int(input("digite o lado A: "))
ladoB= int(input("digite o lado B: "))
ladoC = int(input("digite o lado C: "))

if ((ladoA+ladoB)>ladoC and (ladoA+ladoC)>ladoB and (ladoB+ladoC)>ladoA):
    print("É um triângulo")

    if(ladoA == ladoB and ladoB==ladoC and ladoA== ladoC):
        print("Triângulo equilatero")
    elif(ladoA != ladoB and ladoB!=ladoC and ladoA!= ladoC):
        print("Triângulo EScaleno")
    else:
        print ("Triângulo isóceles")
    