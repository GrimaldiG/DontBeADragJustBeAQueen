from CDP.Peca import peca

__author__ = 'Gustavo'
class dama(peca):

    def set_cor(self, cor):
        super(peca).cor = cor

    def get_cor(self):
        return super(peca).cor
