from os import waitpid
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

#Instrucciones generales (solo en ronda 1)
class InitialPage(Page):
    pass

page_sequence = [InitialPage]