programa {
  funcao inicio() {
    inteiro num1, num2 
    real resultado

    escreva ("Digite o primeiro numero:")
    leia (num1)

    escreva("Digite o segundo número:")
    leia(num2)
    
    se (num1>num2){
    escreva("o primeiro número é maior que o segundo número ")
    }

    senao se (num1<num2){
      escreva(" o primeiro número  é menor que o segundo número ")
    }

    senao{
      escreva ("os números são iguais")
    }
  
  }
}
