from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('MexicanFood', 'Comida Mexicana')
retaurante_japones = Restaurante('Japa', 'Japones')

restaurante_mexicano.alternar_estado()

def __main__():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    __main__()