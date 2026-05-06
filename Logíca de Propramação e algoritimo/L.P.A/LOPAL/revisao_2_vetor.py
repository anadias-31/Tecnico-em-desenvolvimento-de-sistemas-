#solicite um texto para o usuario
texto=input("DIgite um texto qualquer:")

#Exibir letra por letra do texto
#para cada letra no texto
for letra in texto:
    print(letra)

#contar quantidades de caracteres , diferentes de espaços
qtd_caracteres = 0

for letra in texto:
    if(letra != " "):
        qtd_caracteres+=1
print("A quantidade é: ", qtd_caracteres)

#contar as quantidades de vogais
vogais="aeiouAEIOUàáâãÀÂÃÁéèêÈÊÉíìîÌÎÍóòõôÒÔÓÕúùûÛÙÚ"
qtd_vogais=0

for vogal in vogais:
    for letra in texto:
        if (letra == vogal):
            qtd_vogais+=1
print("A quantidade de vogais é :", qtd_vogais)

#Palindromo
texto_invertido=""

for i in range(len(texto)-1,-1,-1):
    texto_invertido=texto_invertido + texto[i]

if(texto == texto_invertido):
    print("É palindromo !")
else:
    print("Não é palindromo")
