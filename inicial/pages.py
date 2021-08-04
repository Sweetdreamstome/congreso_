from os import waitpid
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

class InitialPage(Page):
    def before_next_page(self):
        self.player.voter_total=100
        if self.session.config['poblacion'] == 1:
            self.player.voter1multip=45
            self.player.voter2multip=30
            self.player.voter3multip=25
        else:
            self.player.voter1multip=35
            self.player.voter2multip=33
            self.player.voter3multip=32

class Instrucciones(Page):
    pass

page_sequence = [InitialPage,Instrucciones]