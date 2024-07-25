from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import bebida
from modelos.cardapio.prato import prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = bebida('Suco de melancia', 5.00, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = prato('pãozinho', 2.00, 'o melhor pão da cidade')
prato_paozinho.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
   restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()