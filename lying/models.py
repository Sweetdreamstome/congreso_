from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


doc = """
This is a 2-player lying aversoin game. This is based on "Measuring lying aversion" by Gneezy, Rockenbach and Serra-Garcia (2013) in JEBO.
"""

import random
import statistics 


class Constants(BaseConstants):
    name_in_url = 'lying'
    players_per_group = 2
    num_rounds = 1

    instructions_template = 'lying/instructions.html'
    contact_template = "lying/Contactenos.html"


class Subsession(BaseSubsession):

    def creating_session(self):
        #Creating the groups: 
        new_structure= [[4,1],[5,2],[6,3]]
        self.set_group_matrix(new_structure)
        print(self.get_group_matrix())

class Group(BaseGroup):

    zahl = models.IntegerField()

    message_if_1 = models.IntegerField(min=1, max=6, label= "Si se te asigna el número 1 tu mensaje al otro participante es:")
    message_if_2 = models.IntegerField(min=1, max=6, label= "Si se te asigna el número 2 tu mensaje al otro participante es:")
    message_if_3 = models.IntegerField(min=1, max=6, label= "Si se te asigna el número 3 tu mensaje al otro participante es:")
    message_if_4 = models.IntegerField(min=1, max=6, label= "Si se te asigna el número 4 tu mensaje al otro participante es:")
    message_if_5 = models.IntegerField(min=1, max=6, label= "Si se te asigna el número 5 tu mensaje al otro participante es:")
    message_if_6 = models.IntegerField(min=1, max=6, label= "Si se te asigna el número 6 tu mensaje al otro participante es:")

    follow_if_1 = models.IntegerField(label = "Si el otro participante te dice que el número asignado es 1, tu decisión es", choices=[
            [1, 'Creer en el mensaje'],
            [2, 'No creer en el mensaje'],
        ],
        widget = widgets.RadioSelect
    )
    follow_if_2 = models.IntegerField(label = "Si el otro participante te dice que el número asignado es 2, tu decisión es", choices=[
            [1, 'Creer en el mensaje'],
            [2, 'No creer en el mensaje'],
        ],
        widget = widgets.RadioSelect
    )
    follow_if_3 = models.IntegerField(label = "Si el otro participante te dice que el número asignado es 3, tu decisión es", choices=[
            [1, 'Creer en el mensaje'],
            [2, 'No creer en el mensaje'],
        ],
        widget = widgets.RadioSelect
    )
    follow_if_4 = models.IntegerField(label = "Si el otro participante te dice que el número asignado es 4, tu decisión es", choices=[
            [1, 'Creer en el mensaje'],
            [2, 'No creer en el mensaje'],
        ],
        widget = widgets.RadioSelect
    )
    follow_if_5 = models.IntegerField(label = "Si el otro participante te dice que el número asignado es 5, tu decisión es", choices=[
            [1, 'Creer en el mensaje'],
            [2, 'No creer en el mensaje'],
        ],
        widget = widgets.RadioSelect
    )
    follow_if_6 = models.IntegerField(label = "Si el otro participante te dice que el número asignado es 6, tu decisión es", choices=[
            [1, 'Creer en el mensaje'],
            [2, 'No creer en el mensaje'],
        ],
        widget = widgets.RadioSelect
    )

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        self.zahl = random.randint(1,6)

        if self.zahl==1:
            p1.payoff = c(10) + 2*c(self.message_if_1) 
            if self.message_if_1 == 1 and self.follow_if_1 == 1:
                p2.payoff = c(10)
            elif self.message_if_1 != 1 and self.follow_if_1 == 1:
                p2.payoff = c(0)
            elif self.follow_if_1 == 2:
                p2.payoff = c(3)
        elif self.zahl == 2:
            p1.payoff = c(10) + 2*c(self.message_if_2) 
            if self.message_if_2 == 2 and self.follow_if_2 == 1:
                p2.payoff = c(10)
            elif self.message_if_2 != 2 and self.follow_if_2 == 1:
                p2.payoff = c(0)
            elif self.follow_if_2 == 2:
                p2.payoff = c(3)
        elif self.zahl == 3:
            p1.payoff = c(10) + 2*c(self.message_if_3) 
            if self.message_if_3 == 3 and self.follow_if_3 == 1:
                p2.payoff = c(10)
            elif self.message_if_3 != 3 and self.follow_if_3 == 1:
                p2.payoff = c(0)
            elif self.follow_if_3 == 2:
                p2.payoff = c(3)
        elif self.zahl == 4:
            p1.payoff = c(10) + 2*c(self.message_if_4) 
            if self.message_if_4 == 4 and self.follow_if_4 == 1:
                p2.payoff = c(10)
            elif self.message_if_4 != 4 and self.follow_if_4 == 1:
                p2.payoff = c(0)
            elif self.follow_if_4 == 2:
                p2.payoff = c(3)
        elif self.zahl == 5:
            p1.payoff = c(10) + 2*c(self.message_if_5) 
            if self.message_if_5 == 5 and self.follow_if_5 == 1:
                p2.payoff = c(10)
            elif self.message_if_5 != 5 and self.follow_if_5 == 1:
                p2.payoff = c(0)
            elif self.follow_if_5 == 2:
                p2.payoff = c(3)
        elif self.zahl == 6:
            p1.payoff = c(10) + 2*c(self.message_if_6) 
            if self.message_if_6 == 6 and self.follow_if_6 == 1:
                p2.payoff = c(10)
            elif self.message_if_6 != 6 and self.follow_if_6 == 1:
                p2.payoff = c(0)
            elif self.follow_if_6 == 2:
                p2.payoff = c(3)

class Player(BasePlayer):
    pass
