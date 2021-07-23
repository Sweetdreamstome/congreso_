# from ultimatum.pages import Decision
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
One player decides how to divide a certain amount between himself and the other
player.

See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.

"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum'
    players_per_group = 2
    num_rounds = 1

    instructions_template = 'ultimatum/instructions.html'
    contact_template = "ultimatum/Contactenos.html"

    # Initial amount allocated to the dictator
    endowment = c(100)


class Subsession(BaseSubsession):

    def creating_session(self):
        #Creating the groups: 
        new_structure= [[4,3],[5,1],[6,2]]
        self.set_group_matrix(new_structure)
        print(self.get_group_matrix())

class Group(BaseGroup):
    kept = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0,
        max=Constants.endowment,
        label="Me quedaré con",
    )

    decision = models.IntegerField(label="Aceptarás o rechazarás la propuesta del Participante A?", choices=[
            [1, 'Aceptar'],
            [2, 'Rechazar'],
        ],
        widget=widgets.RadioSelect
    )

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        if self.decision == 1 : 
            p1.payoff = self.kept
            p2.payoff = Constants.endowment - self.kept
        else:
            p1.payoff = c(0)
            p2.payoff = c(0)

class Player(BasePlayer):
    pass
