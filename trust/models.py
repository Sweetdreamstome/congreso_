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
This is a standard 2-player trust game where the amount sent by player 1 gets
tripled. The trust game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'trust'
    players_per_group = 2
    num_rounds = 1

    instructions_template = 'trust/instructions.html'
    contact_template = "trust/Contactenos.html"

    # Initial amount allocated to each player
    endowment = c(100)
    multiplier = 3


class Subsession(BaseSubsession):

    def creating_session(self):
        #Creating the groups: 
        new_structure= [[2,4],[3,5],[1,6]]
        self.set_group_matrix(new_structure)
        print(self.get_group_matrix())

class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        doc="""Amount sent by P1""",
        label="Por favor, ingresa una cantidad entre 0 y 100:",
    )

    sent_back_amount = models.CurrencyField(doc="""Amount sent back by P2""", min=c(0), label="Cantidad a devolver")

    def sent_back_amount_max(self):
        return self.sent_amount * Constants.multiplier

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
        p2.payoff = self.sent_amount * Constants.multiplier - self.sent_back_amount


class Player(BasePlayer):
    pass
