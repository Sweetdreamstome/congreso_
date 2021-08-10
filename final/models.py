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
import random
#from otree.db.models import StringField


doc = """
Páginas finales del experimento
"""


class Constants(BaseConstants):
    name_in_url = 'final'
    players_per_group = 6
    num_rounds = 1 #tbd

    contact_template = "final/Contactenos.html"
class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #Pago de juego principal
    paid_in = models.StringField()
    pago_final_final = models.CurrencyField()

    #Pago de jueguitos
    paid_in_jueguito = models.StringField()
    pago_final_de_jueguitos = models.CurrencyField()

    #Pago final del experimento
    pago_final_final_experimento = models.CurrencyField()

    #Encuesta final
    sexo = models.IntegerField(
        choices=[
            [0, 'Femenino'],
            [1, 'Masculino']
        ],
        widget=widgets.RadioSelect,
        label="¿Cuál es tu sexo?"
    )
    runo_like = models.IntegerField(
        choices=[
            [0, 'Sin segunda vuelta'],
            [1, 'Con segunda vuelta']
        ],
        widget=widgets.RadioSelect,
        label="¿Qué tipo de gobierno te gustó más?"
    )
    runo_fair = models.IntegerField(
        choices=[
            [0, 'Sin segunda vuelta'],
            [1, 'Con segunda vuelta']
        ],
        widget=widgets.RadioSelect,
        label="¿Qué tipo de gobierno te pareció más justo?"
    )
    cong_away = models.IntegerField(
        choices=[
            [0, 'No'],
            [1, 'Sí'],
            [3, 'Sería igual'],
            [4, 'No sé']
        ],
        widget=widgets.RadioSelect,
        label="En este juego de elecciones, ¿crees que sin Congreso (solo presidente que decida la distribución del presupuesto) se lograrían mejores resultados?"
    )
    cong_add = models.IntegerField(
        choices=[
            [0, 'No'],
            [1, 'Sí'],
            [2, 'No sé'],
            [3, 'Sería igual']
        ],
        widget=widgets.RadioSelect,
        label="En este juego de elecciones, ¿crees que con la aparición de un Congreso compuesto por varios partidos y que pueda modificar las propuestas del presidente se lograrían mejores resultados?"
    )

    #Las que son para el piloto
    muylargo = models.IntegerField(
        choices=[
            [0, 'Corta'],
            [1, 'Justa'],
            [2, 'Larga']
        ],
        widget=widgets.RadioSelect,
        label="La duración del experimento te pareció..."
    )
    instrucciones = models.IntegerField(
        choices=[
            [0, 'Mayormente confusas'],
            [1, 'Un poco confusas'],
            [2, 'Mayormente claras']
        ],
        widget=widgets.RadioSelect,
        label="Las instrucciones a lo largo del juego fueron..."
    )
    sugerencias = models.LongStringField(
        label="¿Qué sugerencias nos darías para mejorar el experimento? Tu respuesta aquí es MUY valiosa para nosotros.")
    
    sexo = models.IntegerField(
        choices=[
            [0, 'Femenino'],
            [1, 'Masculino']
        ],
        widget=widgets.RadioSelect,
        label="¿Cuál es tu sexo?"
    )