programa {
  funcao inicio() {
    real raio,altura,area,volume,pi=3.14

    escreva("digite o raio:")
    leia(raio)

    escreva("digite a altura:")
    leia(altura)

    area=2*pi*raio*(raio+altura)
    escreva("A área é:",area)

    volume=pi*raio*raio*altura
    escreva("O volume é:", volume)
  }
}
