#Sistema doe cadastro de usuarios e produtos 
#O sistema devera permitir :
#-cadastra
#-listar
#-deletar

#Criação de listas 
usuarios= []
produtos= []

#-----------------------------------------------
#-------------Função menu usuario---------------
def menu_usuarios ():
    opcao_menu_usuario = 0

    while(opcao_menu_usuario != 4 ):
        print()
        print("----Menu Usuário----")
        print("1-Cadastrar Usuarios")
        print("2-Lista usuario")
        print("3-Deletar usuarios")
        print("4-Voltar")

        opcao_menu_usuario = int(input("Escolha uma opção: "))

        match opcao_menu_usuario:
            #Cadastrar usuario
            case 1:
                nome=input("Digite o nome:")
                telefone=input("Digite o telefone:")
                email=input("Digite o email:")
            
                #Criação do Json de usurios (chava:valor)
                usuario={
                    "nome": nome, 
                    "telefone": telefone,
                    "email": email
                }

                #Adicionar o json no array
                usuarios.append(usuario)
                print(f"Usuario {usuario['nome']}cadastrado com sucesso!")
            #Listar usuarios
            case 2:
                print("\n Lista de usuários")
                if (len(usuarios)==0):
                    print("Nenhum usuário cadastrado")
                else:
                    for usu in usuarios:
                        print("-----------")
                        print("Nome",usu["nome"])
                        print("Telefone: ",usu["telefone"])
                        print("Email",usu["email"])
            #Deletar Usuarios
            case 3:
                nome_deletar = input("Digite o nome do usuário que deseja deletar: ")
                encontrado = False

                for usu in usuarios:
                    if (usu["nome"]== nome_deletar):
                        usuarios.remove(usu)
                        encontrado=True
                        print("Usuários removidos com sucesso!")

                if(encontrado == False):
                    print("Usuário removido com sucesso")
            #Voltar ao menu principal
            case 4:
                print("Voltando ao menu principal...")
                break

#-----------------------------------------------
#------------Função menu produtos---------------
def menu_produtos ():
    opcao_menu_produto = 0

    while(opcao_menu_produto != 5 ):
        print()
        print("----Menu Produto----")
        print("1-Cadastrar Produtos")
        print("2-Lista produtos")
        print("3-Deletar produtos")
        print("4-calcular total")
        print("5-voltar")

        opcao_menu_produto = int(input("Escolha uma opção: "))

        match opcao_menu_produto:
            #Cadastrar produto
            case 1:
                nome=input("Digite o nome:")
                descricao=input("Digite a descrição:")
                quantidade=input("Digite o quantidade:")
                valor=input("Digite o valor:")
            
                #Criação do Json de produto (chava:valor)
                produto={
                    "nome": nome, 
                    "descricao": descricao,
                    "quantidade": quantidade,
                    "valor":valor
                }

                #Adicionar o json no array
                produtos.append(produto)
                print(f"Produto {produto['nome']}cadastrado com sucesso!")
            #Listar produtos
            case 2:
                print("\n Lista de produtos")

                if (len(produtos)==0):
                    print("Nenhum produto cadastrado")

                else:
                    for pro in produtos:
                        print("-----------")
                        print("Nome",pro["nome"])
                        print("Descrição: ",pro["descricao"])
                        print("Quantidade",pro["quantidade"])
                        print("Valor",pro["valor"])
            #Deletar Produtos
            case 3:
                nome_deletar = input("Digite o nome do produto que deseja deletar: ")
                encontrado = False

                for pro in produtos:
                    if (pro["nome"]== nome_deletar):
                        produtos.remove(pro)
                        encontrado=True
                        print("Produto removidos com sucesso!")

                if(encontrado == False):
                    print("Produto removido com sucesso")
            
            #Voltar ao menu principal
            case 5:
                print("Voltando ao menu principal...")
                break
#-----------------------------------------------
#----------------Menu principal-----------------
opcao_menu =0
while (opcao_menu != 3):
    print("----Menu sistema de cadastro----")
    print("Opções:")
    print("1-Usuarios")
    print("2-Produtos")
    print("3-Sair")
    opcao_menu=int(input("Escolha uma opção: "))

    match opcao_menu:
        #menu Usuario
        case 1:
            menu_usuarios()
        #menu produtos
        case 2 :
            menu_produtos()
        case 3:
            print("Até logo")
        case 4: 
            print("Opção inválida")




