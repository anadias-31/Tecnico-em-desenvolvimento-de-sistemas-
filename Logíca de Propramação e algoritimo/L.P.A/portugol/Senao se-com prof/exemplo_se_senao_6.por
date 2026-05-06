programa {
  funcao inicio() {
    inteiro valor_compra 
    cadeia possui_cupom 

    escreva ("valor da compra: ")
    leia (valor_compra)
    
    escreva("Possui cupom?: ")
    leia (possui_cupom)

    se (valor_compra >=200 ou possui_cupom == "sim"){
      escreva ("Você ganhou desconto!😍")
    }

    senao{
      escreva ("Infelizmente você  não ganhou desconto 😣")
    }
  }
}
