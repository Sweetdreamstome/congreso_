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

    #masas de votantes: comentar y descomentar según corresponda
    #voter1multip = 45
    #voter2multip = 30
    #voter3multip = 25
    #voter1multip = 35
    #voter2multip = 33
    #voter3multip = 32
    #voter_total = 100

class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            if self.session.config['congreso']==True:
                player.participant.vars['congresal'] = True
            else:
                player.participant.vars['congresal'] = False
            if self.session.config['primera_regla']=="plur":
                player.participant.vars['primera_regla'] = "plur"
            else:
                player.participant.vars['primera_regla'] = "runo"
            if self.session.config['poblacion']==1:
                player.participant.vars['poblacion'] = 1
            else:
                player.participant.vars['poblacion'] = 2

class Group(BaseGroup):
    pass
class Player(BasePlayer):
    voter1multip = models.IntegerField()
    voter2multip = models.IntegerField()
    voter3multip = models.IntegerField()
    voter_total = models.IntegerField()