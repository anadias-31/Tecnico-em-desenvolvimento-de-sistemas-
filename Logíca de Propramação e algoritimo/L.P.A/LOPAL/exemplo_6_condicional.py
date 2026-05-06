cupom = input("Você tem cupom de desconto ?")
valordacompra = float(input("Digite o valor da compra:"))

if(valordacompra >= 200 or cupom == "Sim"):
    print("Você ganhou um desconto de 15%")
else:
    print("Você não tem direito a desconto ")