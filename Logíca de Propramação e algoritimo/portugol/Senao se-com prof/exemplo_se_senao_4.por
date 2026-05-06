programa {
  funcao inicio() {
    cadeia operacao
    inteiro num1, num2
    real resultado

    escreva ("Digite a operação(+,-,*,/):")
    leia (operacao)

    escreva ("Digite o primeiro numero:")
    leia (num1)

    escreva("Digite o segundo numero:")
    leia (num2)

    se(operacao == "+"){
      resultado=num1 + num2
    }

    senao se(operacao == "-"){
      resultado= num1 - num2
    }

    senao se(operacao == "*"){
      resultado= num1 * num2
    }

    senao se (operacao == "/"){
      resultado= num1 / num2
    }
    
    senao{
      escreva ("Operação invalida!")
    }
    
    escreva("O resultado é:", resultado)
  }
}
