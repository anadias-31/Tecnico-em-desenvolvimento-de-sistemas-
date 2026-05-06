programa {
  funcao inicio() {
    inteiro inicio,fim,soma=0
    escreva ("Digite um numero incicial:")
    leia (inicio)

    escreva (" Digite o numero final:")
    leia (fim)

    para (inteiro i=inicio; i<=fim; i++){
      se(i%2 == 0){
        soma= soma + i
      }
   }
   escreva ("a soma dos pares é: ", soma)

  }
}
