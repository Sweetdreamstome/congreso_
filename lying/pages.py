from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Send(Page):
    """This page is only for P1
    P1 sends the numbers to P2"""

    form_model = 'group'
    form_fields = ['message_if_1', 'message_if_2', 'message_if_3', 'message_if_4', 'message_if_5', 'message_if_6']

    def is_displayed(self):
        return self.player.id_in_group == 1

class Follow(Page):
    """This page is only for P2
    P2 decides to believe or not P1 message for each possible message"""

    form_model = 'group'
    form_fields = ['follow_if_1', 'follow_if_2', 'follow_if_3', 'follow_if_4', 'follow_if_5', 'follow_if_6']

    def is_displayed(self):
        return self.player.id_in_group == 2

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

class Results(Page):
    def before_next_page(self):
        self.player.participant.vars['payoff_points_lying']=self.player.payoff
        
    """This page displays the earnings of each player"""

    def vars_for_template(self):
        return dict(
            zahl=self.group.zahl,
            message_if_1=self.group.message_if_1,
            message_if_2=self.group.message_if_2,
            message_if_3=self.group.message_if_3,
            message_if_4=self.group.message_if_4,
            message_if_5=self.group.message_if_5,
            message_if_6=self.group.message_if_6,
            participant_id = self.participant.label,
            payoff=self.player.payoff,
        )



page_sequence = [
    Introduction,
    Send,
    Follow,
    ResultsWaitPage,
    Results,
]
