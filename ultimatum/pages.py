from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Offer(Page):
    form_model = 'group'
    form_fields = ['kept']

    def is_displayed(self):
        return self.player.id_in_group == 1

class OfferWaitPage(WaitPage):
    pass

class Decision(Page):
    """This page is only for P2
    Player 2 decide whether to accept or reject the offer from Player 1"""

    form_model = 'group'
    form_fields = ['decision']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        sent = Constants.endowment - self.group.kept        

        return dict(
            kept=self.group.kept,
            sent=sent,
        )


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    def before_next_page(self):
        self.player.participant.vars['payoff_points_ultimatum']=self.player.payoff
        
    def vars_for_template(self):
        return dict(offer=Constants.endowment - self.group.kept)


page_sequence = [Introduction, Offer, OfferWaitPage, Decision, ResultsWaitPage, Results]
