programa {
  funcao inicio() {
    inteiro numero, fatorial=1

    escreva("Digite um numero: ")
    leia (numero)

    para(inteiro i=numero;i>=1;i--){
      fatorial = fatorial*i
    }
   escreva ("O valor deesse fatorial é : ",fatorial)
 
   }
 }
}