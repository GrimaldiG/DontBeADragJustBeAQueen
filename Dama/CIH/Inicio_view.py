from CCI.Controle_partida import controle_partida
from CIH.Jogo_view import Jogo

__author__ = 'Gustavo'
class Inicio:
    def __init__(self):
        self.opcao()

    def opcao(self):
        print("Escolha  1 - Jogar 2- visualizar jogadores e seus scores(nao disponivel ate o momento):")
        escolha = int( input())
        if escolha==1:
             controle_partida().iniciar_partida()
        elif escolha == 2:
            return False
        else:
            return False

