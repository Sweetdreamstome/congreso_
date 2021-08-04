from os import waitpid
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

import random

class Encuesta(Page):
    form_model = 'player'

    def get_form_fields(self): #Dependerá de si es con Congreso o no
        if self.session.config['congreso']==True:
            #return ['runo_like', 'runo_fair', 'cong_away','muylargo','instrucciones','sugerencias']
            return ['runo_like', 'runo_fair', 'cong_away', 'sexo']
        else:
            #return ['runo_like', 'runo_fair', 'cong_add','muylargo','instrucciones','sugerencias']
            return ['runo_like', 'runo_fair', 'cong_add', 'sexo']

    def before_next_page(self):
        if self.session.config['poblacion']==1:
            if self.session.config['primera_regla']=='plur':
                self.participant.vars['rol_demo1']=self.participant.vars['rol_plur_pob1']
                self.participant.vars['rol_demo2']=self.participant.vars['rol_runo_pob1']
                self.participant.vars['puntos_demo1']=self.participant.vars['total_payoff_plur_pob1']
                self.participant.vars['puntos_demo2']=self.participant.vars['total_payoff_runo_pob1']
            else:
                self.participant.vars['rol_demo1']=self.participant.vars['rol_runo_pob1']
                self.participant.vars['rol_demo2']=self.participant.vars['rol_plur_pob1']
                self.participant.vars['puntos_demo1']=self.participant.vars['total_payoff_runo_pob1']
                self.participant.vars['puntos_demo2']=self.participant.vars['total_payoff_plur_pob1']
        else:
            if self.session.config['primera_regla']=='plur':
                self.participant.vars['rol_demo1']=self.participant.vars['rol_plur_pob2']
                self.participant.vars['rol_demo2']=self.participant.vars['rol_runo_pob2']
                self.participant.vars['puntos_demo1']=self.participant.vars['total_payoff_plur_pob2']
                self.participant.vars['puntos_demo2']=self.participant.vars['total_payoff_runo_pob2']
            else:
                self.participant.vars['rol_demo1']=self.participant.vars['rol_runo_pob2']
                self.participant.vars['rol_demo2']=self.participant.vars['rol_plur_pob2']
                self.participant.vars['puntos_demo1']=self.participant.vars['total_payoff_runo_pob2']
                self.participant.vars['puntos_demo2']=self.participant.vars['total_payoff_plur_pob2']

        app = random.randint(1,2)
        if app==1:
            self.participant.vars['paid_in']='Primeras 5'
            self.participant.vars['pago_final_final']=self.participant.vars['puntos_demo1']/4
        else:
            self.participant.vars['paid_in']='Últimas 5'
            self.participant.vars['pago_final_final']=self.participant.vars['puntos_demo2']/4


        self.player.paid_in = self.player.participant.vars['paid_in']
        self.player.pago_final_final = self.player.participant.vars['pago_final_final']

        jueguito = random.randint(1,4)
        if jueguito==1:
            self.participant.vars['paid_in_jueguito']='Tarea corta 1'
            self.participant.vars['pago_final_de_jueguitos']=self.participant.vars['payoff_points_dictator']/50
        elif jueguito==2:
            self.participant.vars['paid_in_jueguito']='Tarea corta 2'
            self.participant.vars['pago_final_de_jueguitos']=self.participant.vars['payoff_points_trust']/50
        elif jueguito==3:
            self.participant.vars['paid_in_jueguito']='Tarea corta 3'
            self.participant.vars['pago_final_de_jueguitos']=self.participant.vars['payoff_points_ultimatum']/50
        else:
            self.participant.vars['paid_in_jueguito']='Tarea corta 4'
            self.participant.vars['pago_final_de_jueguitos']=self.participant.vars['payoff_points_lying']/10

        self.player.paid_in_jueguito = self.player.participant.vars['paid_in_jueguito']
        self.player.pago_final_de_jueguitos = self.player.participant.vars['pago_final_de_jueguitos']

        self.player.pago_final_final_experimento = self.player.pago_final_final + self.player.pago_final_de_jueguitos 


 




class Pago_final(Page):
    def vars_for_template(self):
        return dict(
            dictator_pago=self.participant.vars['payoff_points_dictator'],
            trust_pago=self.participant.vars['payoff_points_trust'],
            ultimatum_pago=self.participant.vars['payoff_points_ultimatum'],
            lying_pago=self.participant.vars['payoff_points_lying'],
        )


class Final_e2lab(Page):
    pass

page_sequence = [Encuesta,
    Pago_final,
    Final_e2lab]