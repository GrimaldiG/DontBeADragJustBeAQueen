import os
from CGT.APL_partida import APL_partida
from CIH.Jogo_view import Jogo

__author__ = 'Gustavo'

class controle_partida:
    def iniciar_partida(self):

        Jogo().imprimeTabuleiro(APL_partida().iniciar_jogo())