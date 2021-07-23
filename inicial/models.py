from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c
)
import math
#from otree.db.models import StringField


doc = """
Página inicial del experimento
"""


class Constants(BaseConstants):
    name_in_url = 'inicial'
    players_per_group = 6
    num_rounds = 1 #tbd
class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass
class Player(BasePlayer):
    pass