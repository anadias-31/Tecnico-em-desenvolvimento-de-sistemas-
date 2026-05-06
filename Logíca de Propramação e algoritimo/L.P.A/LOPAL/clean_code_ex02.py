notas= []

for i in range (4):
    #tenta solicitar as notas
    try:
        nota=float(input("Digite {i=1}ª nota: "))

        if(nota < 0  or  nota > 10):
            print("Nota invalida, Insira um valor entre 0 e 10")
            exit()
        else:
            notas.append(nota)
    #Se tiver algun erro (excessão de valor), retorna uma mensagem
    except ValueError:
        print("Erro:Insira um numero valido!")
#Se a pessoa apenas digitou texto
if not notas :
    print("Nenhuma nota foi inserida!")

else:
    media=sum(notas)/len(notas)

    if(media >= 7):
        print(f"Média= {media}-Aprovado")
    elif(media >= 5):
        print(f"Média= {media}-Recuperação")
    else:
        print(f"Média= {media}-Reprovado")