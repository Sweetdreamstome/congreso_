from os import waitpid
#from posix import waitid_result
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

#Instrucciones generales (solo en ronda 1)
class IntroGeneral(Page):
    def is_displayed(player): #Solo mostrar en primera ronda
        return player.round_number == 1

#Intro para todos
class Introduction(Page):
    def before_next_page(self):
        #Acá guardo todas las participant.vars en fields, para que salgan en el Excel:
        self.player.congresal=self.player.participant.vars['congresal']

#Solo los políticos pasan a las promesas
class Promesa(Page):
    def is_displayed(self): #Solo para políticos
        return self.player.id_in_group > 3 #IDs 4, 5 y 6

    form_model = 'group'

    def get_form_fields(self): #A cada político, solo muéstrale su formfield
        if self.player.congresal == True:
            if self.player.role == Constants.politiciana_role:
                return ['promesa_a1', 'promesa_a2', 'promesa_a3','promesa_a1c','promesa_a2c','promesa_a3c']
            elif self.player.role == Constants.politicianb_role:
                return ['promesa_b1', 'promesa_b2', 'promesa_b3','promesa_b1c','promesa_b2c','promesa_b3c']
            else:
                return ['promesa_c1', 'promesa_c2', 'promesa_c3','promesa_c1c','promesa_c2c','promesa_c3c']
        else:
            if self.player.role == Constants.politiciana_role:
                return ['promesa_a1', 'promesa_a2', 'promesa_a3']
            elif self.player.role == Constants.politicianb_role:
                return ['promesa_b1', 'promesa_b2', 'promesa_b3']
            else:
                return ['promesa_c1', 'promesa_c2', 'promesa_c3']
    
    def error_message(self, values): #Las promesas deben sumar 100
        if self.player.congresal == True:
            if self.player.role == Constants.politiciana_role:
                if values['promesa_a1'] + values['promesa_a2'] + values['promesa_a3'] != Constants.budget and values['promesa_a1c'] + values['promesa_a2c'] + values['promesa_a3c'] <= Constants.budget:
                    return 'Las promesas presidenciales deben sumar el presupuesto.'
                if values['promesa_a1'] + values['promesa_a2'] + values['promesa_a3'] == Constants.budget and values['promesa_a1c'] + values['promesa_a2c'] + values['promesa_a3c'] > Constants.budget:
                    return 'Las promesas congresales no pueden sumar más que el presupuesto.'
                if values['promesa_a1'] + values['promesa_a2'] + values['promesa_a3'] != Constants.budget and values['promesa_a1c'] + values['promesa_a2c'] + values['promesa_a3c'] > Constants.budget:
                    return 'Las promesas presidenciales deben sumar el presupuesto y las promesas congresales no pueden sumar más que el presupuesto.'
            elif self.player.role == Constants.politicianb_role:
                if values['promesa_b1'] + values['promesa_b2'] + values['promesa_b3'] != Constants.budget and values['promesa_b1c'] + values['promesa_b2c'] + values['promesa_b3c'] <= Constants.budget:
                    return 'Las promesas presidenciales deben sumar el presupuesto.'
                if values['promesa_b1'] + values['promesa_b2'] + values['promesa_b3'] == Constants.budget and values['promesa_b1c'] + values['promesa_b2c'] + values['promesa_b3c'] > Constants.budget:
                    return 'Las promesas congresales no pueden sumar más que el presupuesto.'
                if values['promesa_b1'] + values['promesa_b2'] + values['promesa_b3'] != Constants.budget and values['promesa_b1c'] + values['promesa_b2c'] + values['promesa_b3c'] > Constants.budget:
                    return 'Las promesas presidenciales deben sumar el presupuesto y las promesas congresales no pueden sumar más que el presupuesto.'
            else:
                if values['promesa_c1'] + values['promesa_c2'] + values['promesa_c3'] != Constants.budget and values['promesa_c1c'] + values['promesa_c2c'] + values['promesa_c3c'] <= Constants.budget:
                    return 'Las promesas presidenciales deben sumar el presupuesto.'
                if values['promesa_c1'] + values['promesa_c2'] + values['promesa_c3'] == Constants.budget and values['promesa_c1c'] + values['promesa_c2c'] + values['promesa_c3c'] > Constants.budget:
                    return 'Las promesas congresales no pueden sumar más que el presupuesto.'
                if values['promesa_c1'] + values['promesa_c2'] + values['promesa_c3'] != Constants.budget and values['promesa_c1c'] + values['promesa_c2c'] + values['promesa_c3c'] > Constants.budget:
                    return 'Las promesas presidenciales deben sumar el presupuesto y las promesas congresales no pueden sumar más que el presupuesto.'
        else:
            if self.player.role == Constants.politiciana_role:
                if values['promesa_a1'] + values['promesa_a2'] + values['promesa_a3'] != Constants.budget:
                    return 'Las promesas presidenciales deben sumar el presupuesto.'
            elif self.player.role == Constants.politicianb_role:
                if values['promesa_b1'] + values['promesa_b2'] + values['promesa_b3'] != Constants.budget:
                    return 'Las promesas presidenciales deben sumar el presupuesto.'
            else:
                if values['promesa_c1'] + values['promesa_c2'] + values['promesa_c3'] != Constants.budget:
                    return 'Las promesas presidenciales deben sumar el presupuesto.'


#Votantes pasan de frente. También le aparece a los 2 políticos que prometen más rápido
class PromesaWait(WaitPage):
    pass

#Votantes pasan a votación. En el template mostramos las promesas
class Votacion(Page):

    form_model = 'group'

    def get_form_fields(self): #A cada votante, solo muéstrale su formfield
        if self.player.congresal == True:
            if self.player.role == Constants.voter1_role:
                return ['voto1','voto1_cong']
            elif self.player.role == Constants.voter2_role:
                return ['voto2','voto2_cong']
            elif self.player.role == Constants.voter3_role:
                return ['voto3','voto3_cong']
            else:
                return []
        else:
            if self.player.role == Constants.voter1_role:
                return ['voto1']
            elif self.player.role == Constants.voter2_role:
                return ['voto2']
            elif self.player.role == Constants.voter3_role:
                return ['voto3']
            else:
                return []

#Políticos pasarán más rápido pues no votan. También le aparece a los 2 votantes que votan más rápido
class VotacionWait(WaitPage):
    after_all_players_arrive = 'multiplicar_votos' #Multiplicamos los votos por las cantidades de los tipos

#Mostramos resultados de la votación a todos
class VotacionResults(Page):
    form_model = 'group'
    def get_form_fields(self): #A cada votante, solo muéstrale su formfield
        if self.player.role == Constants.voter1_role and self.group.habra_segunda == True:
            return ['voto1_2da']
        elif self.player.role == Constants.voter2_role and self.group.habra_segunda == True:
            return ['voto2_2da']
        elif self.player.role == Constants.voter3_role and self.group.habra_segunda == True:
            return ['voto3_2da']
        else:
            return []

class Votacion_runoff_Wait(WaitPage):
    def is_displayed(self):
        return self.group.habra_segunda == True
    after_all_players_arrive = 'definir_ganador_2da'

class Votacion_runoff_Results(Page):
    def is_displayed(self):
        return self.group.habra_segunda == True

#El presidente decide
class Allocation(Page):
    def is_displayed(self): #Solo para el ganador
        return self.player.ganador == True

    form_model = 'group'
    form_fields = ['allocation_1', 'allocation_2', 'allocation_3']

    def error_message(group, values): #Las promesas deben sumar 100
        if values['allocation_1'] + values['allocation_2'] + values['allocation_3'] != Constants.budget:
            return 'Los números deben sumar el presupuesto a asignar.'

#Todos esperan mientras el presidente decide
class AllocationWait1(WaitPage):
    pass

#El Congreso decide si aceptar o rechazar. También, preguntamos cuál sería su allocation en caso de Rechazo
class Allocation_cong(Page):
    def is_displayed(self): #Solo para políticos
        return self.player.id_in_group > 3 and self.player.congresal == True #IDs 4, 5 y 6

    form_model = 'group'

    def get_form_fields(self): #A cada político, solo muéstrale su formfield
        if self.player.role == Constants.politiciana_role:
            return ['accion_a_cong', 'alloc_a1c', 'alloc_a2c','alloc_a3c']
        elif self.player.role == Constants.politicianb_role:
            return ['accion_b_cong', 'alloc_b1c', 'alloc_b2c','alloc_b3c']
        else:
            return ['accion_c_cong', 'alloc_c1c', 'alloc_c2c','alloc_c3c']
    
    def error_message(self, values): #Las asignaciones deben sumar 100 y el presidente solo puede aceptar
        if self.player.ganador == True and self.player.role == Constants.politiciana_role:
            if values['accion_a_cong'] == 0:
                return 'Como también eres el presidente, debes aceptar tu propia propuesta.'
        elif self.player.ganador == True and self.player.role == Constants.politicianb_role:
            if values['accion_b_cong'] == 0:
                return 'Como también eres el presidente, debes aceptar tu propia propuesta.'
        elif self.player.ganador == True and self.player.role == Constants.politicianc_role:
            if values['accion_c_cong'] == 0:
                return 'Como también eres el presidente, debes aceptar tu propia propuesta.'
        if self.player.role == Constants.politiciana_role:
            if values['alloc_a1c'] + values['alloc_a2c'] + values['alloc_a3c'] != Constants.budget:
                return 'Las cantidades deben sumar el presupuesto.'
        elif self.player.role == Constants.politicianb_role:
            if values['alloc_b1c'] + values['alloc_b2c'] + values['alloc_b3c'] != Constants.budget:
                return 'Las cantidades deben sumar el presupuesto.'
        else:
            if values['alloc_c1c'] + values['alloc_c2c'] + values['alloc_c3c'] != Constants.budget:
                return 'Las cantidades deben sumar el presupuesto.'


#Los otros 3 esperan (pasan de frente):
class AllocationWait2(WaitPage):
    after_all_players_arrive = 'accion_congreso_pagos' #Se define cuál es la asignación final

#Mostramos final allocation
class Results(Page):
    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()

        return dict(
            total_payoff=sum([p.payoff for p in player_in_all_rounds]),
        )

    form_model = 'player'

    def get_form_fields(self): #A cada político, solo muéstrale su formfield
        if self.player.congresal == True:
            if self.player.id_in_group <= 3:
                return ['aprueba', 'aprueba_cong','aprueba_cong_own','aprueba_resultado']
            else:
                return ['aprueba_resultado']
        else:
            if self.player.id_in_group <= 3:
                return ['aprueba','aprueba_resultado']
            else:
                return ['aprueba_resultado']


#Página final (solo en ronda final)
class Final(Page):
    def is_displayed(player):
        return player.round_number == Constants.num_rounds

    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()

        return dict(
            total_payoff=sum([p.payoff for p in player_in_all_rounds]),
        )

    def before_next_page(self):
        self.player.participant.vars['total_payoff_runo_pob2']=sum([p.payoff for p in self.player.in_all_rounds()])
        self.player.participant.vars['rol_runo_pob2']=self.player.role


page_sequence = [IntroGeneral,
    Introduction,
    Promesa,
    PromesaWait,
    Votacion,
    VotacionWait,
    VotacionResults,
    Votacion_runoff_Wait,
    Votacion_runoff_Results,
    Allocation,
    AllocationWait1,
    Allocation_cong,
    AllocationWait2,
    Results,
    Final]