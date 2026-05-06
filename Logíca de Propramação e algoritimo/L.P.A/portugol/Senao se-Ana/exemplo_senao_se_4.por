programa {
  funcao inicio() {
    inteiro lado1, lado2, lado3
    
    escreva("Lado 1: ")
    leia(lado1)

    escreva("Lado 2: ")
    leia(lado2)

    escreva("Lado 3: ")
    leia(lado3)

    se (lado1==lado2 e lado2==lado3 e lado1==lado3){
      escreva("Equilátero")
    }
    senao se (lado1==lado2 ou lado2==lado3 ou lado3==lado1){
      escreva ("Isóceles")
    }
    senao{
      escreva ("Escaleno")
    }
    
  }
}
