import pandas as pd
import os

dados = {
    "Nome":  [],
    "Disciplina": [],
    "Nota":[]
}

deseja_continuar = ""

while(deseja_continuar != "n"):
    print("\nDigite os dados ")
    nome = input("Nome: ")
    disciplina = input("Disciplina: ")
    nota = int(input("Nota: "))

    dados["Nome"].append(nome)
    dados["Disciplina"].append(disciplina)
    dados["Nota"].append(nota)

    deseja_continuar=input("Deseja continuar? (s/n)").strip().lower()
    #strip -> tirar espaços em branco
    #lower -> tranformar em minúsculo

#Criar tabela 
df= pd.DataFrame(dados)
print(df)

#Definir o caminho onde será salvo o arquivo 
os.chdir("C:\\Users\\50186921896\\Documents\\leitura_manipulaçao_Ex01\\")

df.to_csv("dados.txt",sep="\t", index=False)
print("✅Dados salvos em 'dados.txt'!")

try:
    df_lido = pd.read_csv("dados.txt", sep="\t")

except FileNotFoundError:
        print("\n ❌ Arquivo não encontrado ! ")
    