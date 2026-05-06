# importar as bibliotecas
import pandas as pd
import os

dados = {
    "Nome":       [],
    "Id":         [],
    "Quantidade": [],
    "Preço":      []
}

deseja_continuar = ""

while(deseja_continuar != "n"):
    print("\nDigite os dados ")
    nome = input("Nome: ")
    id = int(input("Id: "))
    quantidade = input("Quantidade: ")
    preco = float(input("Preço: "))

    dados["Nome"].append(nome)
    dados["Id"].append(id)
    dados["Quantidade"].append(quantidade)
    dados["Preço"].append(preco)


    deseja_continuar=input("Deseja continuar? (s/n)").strip().lower()
    #strip -> tirar espaços em branco
    #lower -> tranformar em minúsculo

#Criar tabela 
df= pd.DataFrame(dados)
print(df)

#Definir o caminho onde será salvo o arquivo 
os.chdir("C:\\Users\\50186921896\\Documents\\Leitura_manipulação_Ex02\\")

df.to_csv("estoque.csv", index=False)
print("✅Dados salvos em 'estoque.csv'!")

try:
    df_lido = pd.read_csv("estoque.csv")
    print(df_lido)
except FileNotFoundError:
    print("\n ❌ Arquivo não encontrado ! ")