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
Esta app es para que los participantes voten.
Cada elector uno tiene un peso diferente.
Gana el candidato con más votos.
"""


class Constants(BaseConstants):
    name_in_url = 'elec_plur_pob2'
    players_per_group = 6
    num_rounds = 5 #tbd

    #Ejecutar las funciones del runoff?
    runoff = False

    #Presupuesto por ronda (no usar currency):
    budget = 100

    #masas de votantes: comentar y descomentar según corresponda
    #voter1multip = 45
    #voter2multip = 30
    #voter3multip = 25
    voter1multip = 35
    voter2multip = 33
    voter3multip = 32
    voter_total = 100

    #ego rent
    egorent = 4
    castigo = 4

    #Roles (debe terminar en _role)
    voter1_role = 'Votante tipo A'
    voter2_role = 'Votante tipo B'
    voter3_role = 'Votante tipo C'
    politiciana_role = 'Político A'
    politicianb_role = 'Político B'
    politicianc_role = 'Político C'

    #para mostrar en cada página
    instructions_template_voter = 'elec_plur_pob2/instructions_voter.html'
    instructions_template_politician = 'elec_plur_pob2/instructions_politician.html'
    contact_template = "elec_plur_pob2/Contactenos.html"
    mapa_eleccion = "elec_plur_pob2/Mapita_eleccion.html"
    mapa_gestion = "elec_plur_pob2/Mapita_gestion.html"
    desplegable = "elec_plur_pob2/Desplegable.html"
    mapa_juego = "elec_plur_pob2/Mapita_juego.html"


#Por acá va la matriz

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
    #Reasignación de roles
  #  def reasignar_roles(group):
       # jugadores = group.get_players() #jala players
        #for jugador in jugadores:
            #prev_jug = jugador.in_round(jugador.round_number-1)

    #PRESIDENTE
    #Promesas del político A a tipos 1, 2, 3
    promesa_a1 = models.IntegerField(min=0, max=Constants.budget, label="Como PRESIDENTE, ¿cuánto le asignarías al Votante tipo A?")
    promesa_a2 = models.IntegerField(min=0, max=Constants.budget, label="Como PRESIDENTE, ¿cuánto le asignarías al Votante tipo B?")
    promesa_a3 = models.IntegerField(min=0, max=Constants.budget, label="Como PRESIDENTE, ¿cuánto le asignarías al Votante tipo C?")
    #Promesas del político B a tipos 1, 2, 3
    promesa_b1 = models.IntegerField(min=0, max=Constants.budget, label="Como PRESIDENTE, ¿cuánto le asignarías al Votante tipo A?")
    promesa_b2 = models.IntegerField(min=0, max=Constants.budget, label="Como PRESIDENTE, ¿cuánto le asignarías al Votante tipo B?")
    promesa_b3 = models.IntegerField(min=0, max=Constants.budget, label="Como PRESIDENTE, ¿cuánto le asignarías al Votante tipo C?")
    #Promesas del político C a tipos 1, 2, 3
    promesa_c1 = models.IntegerField(min=0, max=Constants.budget, label="Como PRESIDENTE, ¿cuánto le asignarías al Votante tipo A?")
    promesa_c2 = models.IntegerField(min=0, max=Constants.budget, label="Como PRESIDENTE, ¿cuánto le asignarías al Votante tipo B?")
    promesa_c3 = models.IntegerField(min=0, max=Constants.budget, label="Como PRESIDENTE, ¿cuánto le asignarías al Votante tipo C?")
    #Forms: Validating multiple fields together (para Page)

    #CONGRESO
    #Promesas del político A a tipos 1, 2, 3
    promesa_a1c = models.IntegerField(min=0, max=Constants.budget, label="Como CONGRESISTA, ¿cuál es la mínima cantidad que el presidente le debe dar al Votante tipo A para que tú aceptes su propuesta?")
    promesa_a2c = models.IntegerField(min=0, max=Constants.budget, label="Como CONGRESISTA, ¿cuál es la mínima cantidad que el presidente le debe dar al Votante tipo B para que tú aceptes su propuesta?")
    promesa_a3c = models.IntegerField(min=0, max=Constants.budget, label="Como CONGRESISTA, ¿cuál es la mínima cantidad que el presidente le debe dar al Votante tipo C para que tú aceptes su propuesta?")
    #Promesas del político B a tipos 1, 2, 3
    promesa_b1c = models.IntegerField(min=0, max=Constants.budget, label="Como CONGRESISTA, ¿cuál es la mínima cantidad que el presidente le debe dar al Votante tipo A para que tú aceptes su propuesta?")
    promesa_b2c = models.IntegerField(min=0, max=Constants.budget, label="Como CONGRESISTA, ¿cuál es la mínima cantidad que el presidente le debe dar al Votante tipo B para que tú aceptes su propuesta?")
    promesa_b3c = models.IntegerField(min=0, max=Constants.budget, label="Como CONGRESISTA, ¿cuál es la mínima cantidad que el presidente le debe dar al Votante tipo C para que tú aceptes su propuesta?")
    #Promesas del político C a tipos 1, 2, 3
    promesa_c1c = models.IntegerField(min=0, max=Constants.budget, label="Como CONGRESISTA, ¿cuál es la mínima cantidad que el presidente le debe dar al Votante tipo A para que tú aceptes su propuesta?")
    promesa_c2c = models.IntegerField(min=0, max=Constants.budget, label="Como CONGRESISTA, ¿cuál es la mínima cantidad que el presidente le debe dar al Votante tipo B para que tú aceptes su propuesta?")
    promesa_c3c = models.IntegerField(min=0, max=Constants.budget, label="Como CONGRESISTA, ¿cuál es la mínima cantidad que el presidente le debe dar al Votante tipo C para que tú aceptes su propuesta?")

    #PRESIDENTE: voto del votante
    voto1 = models.IntegerField(
        choices=[
            [1, 'Partido A'],
            [2, 'Partido B'],
            [3, 'Partido C'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Votante A: ¿A qué candidato PRESIDENCIAL le darás tus votos? Mira el cuadro de abajo si quieres recordar cuántos votos te corresponde dar."
    )
    voto2 = models.IntegerField(
        choices=[
            [1, 'Partido A'],
            [2, 'Partido B'],
            [3, 'Partido C'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Votante B: ¿A qué candidato PRESIDENCIAL le darás tus votos? Mira el cuadro de abajo si quieres recordar cuántos votos te corresponde dar."
    )
    voto3 = models.IntegerField(
        choices=[
            [1, 'Partido A'],
            [2, 'Partido B'],
            [3, 'Partido C'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Votante C: ¿A qué candidato PRESIDENCIAL le darás tus votos? Mira el cuadro de abajo si quieres recordar cuántos votos te corresponde dar."
    )

    #CONGRESo: voto del votante
    voto1_cong = models.IntegerField(
        choices=[
            [1, 'Partido A'],
            [2, 'Partido B'],
            [3, 'Partido C'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Votante A: ¿A qué bancada CONGRESAL le darás tus votos? Mira el cuadro de abajo si quieres recordar cuántos votos te corresponde dar."
    )
    voto2_cong = models.IntegerField(
        choices=[
            [1, 'Partido A'],
            [2, 'Partido B'],
            [3, 'Partido C'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Votante B: ¿A qué bancada CONGRESAL le darás tus votos? Mira el cuadro de abajo si quieres recordar cuántos votos te corresponde dar."
    )
    voto3_cong = models.IntegerField(
        choices=[
            [1, 'Partido A'],
            [2, 'Partido B'],
            [3, 'Partido C'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Votante C: ¿A qué bancada CONGRESAL le darás tus votos? Mira el cuadro de abajo si quieres recordar cuántos votos te corresponde dar."
    )

    #votos para cada político (jala de "votos que el votante le da a cada candidato")
    votos_a = models.IntegerField()
    votos_b = models.IntegerField()
    votos_c = models.IntegerField()
    votos_primero = models.IntegerField()
    votos_segundo = models.IntegerField()
    votos_tercero = models.IntegerField()
    primero = models.StringField()
    segundo = models.StringField()
    tercero = models.StringField()
    #Congreso:
    votos_a_cong = models.IntegerField()
    votos_b_cong = models.IntegerField()
    votos_c_cong = models.IntegerField()
    #Quién votó por quién
    voto1_str = models.StringField()
    voto2_str = models.StringField()
    voto3_str = models.StringField()
    voto1_cong_str = models.StringField()
    voto2_cong_str = models.StringField()
    voto3_cong_str = models.StringField()
    #Identificador de si habrá segunda vuelta
    habra_segunda = models.BooleanField()







    #OJO: ESTA FUNCIÓN TIENE 327 LÍNEAS
    def multiplicar_votos(group):
        jugadorcitos = group.get_players()
        for jugadorcito in jugadorcitos:
            if Constants.runoff == False:
                group.habra_segunda = False
                #1. MULTIPLICA VOTOS
                #Registrar el voto del votante tipo 1
                if group.voto1 == 1:
                    group.votos_a = Constants.voter1multip
                else:
                    group.votos_a = 0
                if group.voto1 == 2:
                    group.votos_b = Constants.voter1multip
                else:
                    group.votos_b = 0
                if group.voto1 == 3:
                    group.votos_c = Constants.voter1multip
                else:
                    group.votos_c = 0
                #Registrar el voto del votante tipo 2
                if group.voto2 == 1:
                    group.votos_a = group.votos_a + Constants.voter2multip
                else:
                    group.votos_a = group.votos_a
                if group.voto2 == 2:
                    group.votos_b = group.votos_b + Constants.voter2multip
                else:
                    group.votos_b = group.votos_b
                if group.voto2 == 3:
                    group.votos_c = group.votos_c + Constants.voter2multip
                else:
                    group.votos_c = group.votos_c
                #Registrar el voto del votante tipo 3
                if group.voto3 == 1:
                    group.votos_a = group.votos_a + Constants.voter3multip
                else:
                    group.votos_a = group.votos_a
                if group.voto3 == 2:
                    group.votos_b = group.votos_b + Constants.voter3multip
                else:
                    group.votos_b = group.votos_b
                if group.voto3 == 3:
                    group.votos_c = group.votos_c + Constants.voter3multip
                else:
                    group.votos_c = group.votos_c

                #CUENTA VOTOS
                group.votos_primero = max(group.votos_a,group.votos_b,group.votos_c)
                group.votos_tercero = min(group.votos_a,group.votos_b,group.votos_c)
                group.votos_segundo = group.votos_a+group.votos_b+group.votos_c-group.votos_primero-group.votos_tercero

                #3. DETERMINA PUESTOS
                if group.votos_primero == group.votos_a:
                    group.primero = Constants.politiciana_role
                elif group.votos_primero == group.votos_b:
                    group.primero = Constants.politicianb_role
                else:
                    group.primero = Constants.politicianc_role

                if group.votos_segundo == group.votos_a:
                    group.segundo = Constants.politiciana_role
                elif group.votos_segundo == group.votos_b:
                    group.segundo = Constants.politicianb_role
                else:
                    group.segundo = Constants.politicianc_role

                if group.primero != Constants.politiciana_role and group.segundo != Constants.politiciana_role:
                    group.tercero = Constants.politiciana_role
                elif group.primero != Constants.politicianb_role and group.segundo != Constants.politicianb_role:
                    group.tercero = Constants.politicianb_role
                else:
                    group.tercero = Constants.politicianc_role

                jugadores = group.get_players() #jala "ganador" de players
                for jugador in jugadores:
                    if group.primero == jugador.role:
                        jugador.ganador = True
                    else:
                        jugador.ganador = False

            #ESTO ES PARA EL CONGRESO:
                if jugadorcito.congresal == True:
                    #Registrar el voto del votante tipo 1
                    if group.voto1_cong == 1:
                        group.votos_a_cong = Constants.voter1multip
                    else:
                        group.votos_a_cong = 0
                    if group.voto1_cong == 2:
                        group.votos_b_cong = Constants.voter1multip
                    else:
                        group.votos_b_cong = 0
                    if group.voto1_cong == 3:
                        group.votos_c_cong = Constants.voter1multip
                    else:
                        group.votos_c_cong = 0
                    #Registrar el voto del votante tipo 2
                    if group.voto2_cong == 1:
                        group.votos_a_cong = group.votos_a_cong + Constants.voter2multip
                    else:
                        group.votos_a_cong = group.votos_a_cong
                    if group.voto2_cong == 2:
                        group.votos_b_cong = group.votos_b_cong + Constants.voter2multip
                    else:
                        group.votos_b_cong = group.votos_b_cong
                    if group.voto2_cong == 3:
                        group.votos_c_cong = group.votos_c_cong + Constants.voter2multip
                    else:
                        group.votos_c_cong = group.votos_c_cong
                    #Registrar el voto del votante tipo 3
                    if group.voto3_cong == 1:
                        group.votos_a_cong = group.votos_a_cong + Constants.voter3multip
                    else:
                        group.votos_a_cong = group.votos_a_cong
                    if group.voto3_cong == 2:
                        group.votos_b_cong = group.votos_b_cong + Constants.voter3multip
                    else:
                        group.votos_b_cong = group.votos_b_cong
                    if group.voto3_cong == 3:
                        group.votos_c_cong = group.votos_c_cong + Constants.voter3multip
                    else:
                        group.votos_c_cong = group.votos_c_cong

            #Quién votó por quién
                #Presidente
                if group.voto1 == 1:
                    group.voto1_str = Constants.politiciana_role
                elif group.voto1 == 2:
                    group.voto1_str = Constants.politicianb_role
                else:
                    group.voto1_str = Constants.politicianc_role
                if group.voto2 == 1:
                    group.voto2_str = Constants.politiciana_role
                elif group.voto2 == 2:
                    group.voto2_str = Constants.politicianb_role
                else:
                    group.voto2_str = Constants.politicianc_role
                if group.voto3 == 1:
                    group.voto3_str = Constants.politiciana_role
                elif group.voto3 == 2:
                    group.voto3_str = Constants.politicianb_role
                else:
                    group.voto3_str = Constants.politicianc_role
                #Congreso
                if jugadorcito.congresal == True:
                    if group.voto1_cong == 1:
                        group.voto1_cong_str = 'Partido A'
                    elif group.voto1_cong == 2:
                        group.voto1_cong_str = 'Partido B'
                    else:
                        group.voto1_cong_str = 'Partido C'
                    if group.voto2_cong == 1:
                        group.voto2_cong_str = 'Partido A'
                    elif group.voto2_cong == 2:
                        group.voto2_cong_str = 'Partido B'
                    else:
                        group.voto2_cong_str = 'Partido C'
                    if group.voto3_cong == 1:
                        group.voto3_cong_str = 'Partido A'
                    elif group.voto3_cong == 2:
                        group.voto3_cong_str = 'Partido B'
                    else:
                        group.voto3_cong_str = 'Partido C'

            else: #SI ESTAMOS EN DEMOCRACIA CON SEGUNDA VUELTA
                #1. MULTIPLICA VOTOS
                #Registrar el voto del votante tipo 1
                if group.voto1 == 1:
                    group.votos_a = Constants.voter1multip
                else:
                    group.votos_a = 0
                if group.voto1 == 2:
                    group.votos_b = Constants.voter1multip
                else:
                    group.votos_b = 0
                if group.voto1 == 3:
                    group.votos_c = Constants.voter1multip
                else:
                    group.votos_c = 0
                #Registrar el voto del votante tipo 2
                if group.voto2 == 1:
                    group.votos_a = group.votos_a + Constants.voter2multip
                else:
                    group.votos_a = group.votos_a
                if group.voto2 == 2:
                    group.votos_b = group.votos_b + Constants.voter2multip
                else:
                    group.votos_b = group.votos_b
                if group.voto2 == 3:
                    group.votos_c = group.votos_c + Constants.voter2multip
                else:
                    group.votos_c = group.votos_c
                #Registrar el voto del votante tipo 3
                if group.voto3 == 1:
                    group.votos_a = group.votos_a + Constants.voter3multip
                else:
                    group.votos_a = group.votos_a
                if group.voto3 == 2:
                    group.votos_b = group.votos_b + Constants.voter3multip
                else:
                    group.votos_b = group.votos_b
                if group.voto3 == 3:
                    group.votos_c = group.votos_c + Constants.voter3multip
                else:
                    group.votos_c = group.votos_c

                #CUENTA VOTOS
                group.votos_primero = max(group.votos_a,group.votos_b,group.votos_c)
                group.votos_tercero = min(group.votos_a,group.votos_b,group.votos_c)
                group.votos_segundo = group.votos_a+group.votos_b+group.votos_c-group.votos_primero-group.votos_tercero

                #3. DETERMINA PUESTOS
                if group.votos_primero == group.votos_a:
                    group.primero = Constants.politiciana_role
                elif group.votos_primero == group.votos_b:
                    group.primero = Constants.politicianb_role
                else:
                    group.primero = Constants.politicianc_role

                if group.votos_segundo == group.votos_a:
                    group.segundo = Constants.politiciana_role
                elif group.votos_segundo == group.votos_b:
                    group.segundo = Constants.politicianb_role
                else:
                    group.segundo = Constants.politicianc_role

                if group.primero != Constants.politiciana_role and group.segundo != Constants.politiciana_role:
                    group.tercero = Constants.politiciana_role
                elif group.primero != Constants.politicianb_role and group.segundo != Constants.politicianb_role:
                    group.tercero = Constants.politicianb_role
                else:
                    group.tercero = Constants.politicianc_role

                if group.voto1 != group.voto2 and group.voto1 != group.voto3 and group.voto2 != group.voto3:
                    group.habra_segunda = True
                else:
                    group.habra_segunda = False
                
                if group.habra_segunda == False:
                    jugadores = group.get_players() #jala "ganador" de players
                    for jugador in jugadores:
                        if group.primero == jugador.role:
                            jugador.ganador = True
                        else:
                            jugador.ganador = False

            #ESTO ES PARA EL CONGRESO:
                if jugadorcito.congresal == True:
                    #Registrar el voto del votante tipo 1
                    if group.voto1_cong == 1:
                        group.votos_a_cong = Constants.voter1multip
                    else:
                        group.votos_a_cong = 0
                    if group.voto1_cong == 2:
                        group.votos_b_cong = Constants.voter1multip
                    else:
                        group.votos_b_cong = 0
                    if group.voto1_cong == 3:
                        group.votos_c_cong = Constants.voter1multip
                    else:
                        group.votos_c_cong = 0
                    #Registrar el voto del votante tipo 2
                    if group.voto2_cong == 1:
                        group.votos_a_cong = group.votos_a_cong + Constants.voter2multip
                    else:
                        group.votos_a_cong = group.votos_a_cong
                    if group.voto2_cong == 2:
                        group.votos_b_cong = group.votos_b_cong + Constants.voter2multip
                    else:
                        group.votos_b_cong = group.votos_b_cong
                    if group.voto2_cong == 3:
                        group.votos_c_cong = group.votos_c_cong + Constants.voter2multip
                    else:
                        group.votos_c_cong = group.votos_c_cong
                    #Registrar el voto del votante tipo 3
                    if group.voto3_cong == 1:
                        group.votos_a_cong = group.votos_a_cong + Constants.voter3multip
                    else:
                        group.votos_a_cong = group.votos_a_cong
                    if group.voto3_cong == 2:
                        group.votos_b_cong = group.votos_b_cong + Constants.voter3multip
                    else:
                        group.votos_b_cong = group.votos_b_cong
                    if group.voto3_cong == 3:
                        group.votos_c_cong = group.votos_c_cong + Constants.voter3multip
                    else:
                        group.votos_c_cong = group.votos_c_cong

            #Quién votó por quién
                #Presidente
                if group.voto1 == 1:
                    group.voto1_str = Constants.politiciana_role
                elif group.voto1 == 2:
                    group.voto1_str = Constants.politicianb_role
                else:
                    group.voto1_str = Constants.politicianc_role
                if group.voto2 == 1:
                    group.voto2_str = Constants.politiciana_role
                elif group.voto2 == 2:
                    group.voto2_str = Constants.politicianb_role
                else:
                    group.voto2_str = Constants.politicianc_role
                if group.voto3 == 1:
                    group.voto3_str = Constants.politiciana_role
                elif group.voto3 == 2:
                    group.voto3_str = Constants.politicianb_role
                else:
                    group.voto3_str = Constants.politicianc_role
                #Congreso
                if jugadorcito.congresal == True:
                    if group.voto1_cong == 1:
                        group.voto1_cong_str = 'Partido A'
                    elif group.voto1_cong == 2:
                        group.voto1_cong_str = 'Partido B'
                    else:
                        group.voto1_cong_str = 'Partido C'
                    if group.voto2_cong == 1:
                        group.voto2_cong_str = 'Partido A'
                    elif group.voto2_cong == 2:
                        group.voto2_cong_str = 'Partido B'
                    else:
                        group.voto2_cong_str = 'Partido C'
                    if group.voto3_cong == 1:
                        group.voto3_cong_str = 'Partido A'
                    elif group.voto3_cong == 2:
                        group.voto3_cong_str = 'Partido B'
                    else:
                        group.voto3_cong_str = 'Partido C'









    #PRESIDENTE - SEGUNDA VUELTA: voto del votante SEGUNDA VUELTA
    voto1_2da = models.IntegerField(
        choices=[
            [1, 'Para el ganador de la primera vuelta'],
            [2, 'Para el segundo puesto de la primera vuelta'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Votante A: En esta SEGUNDA VUELTA PRESIDENCIAL, ¿para quién son tus votos? Mira el cuadro de abajo si quieres recordar cuántos votos te corresponde dar."
    )
    voto2_2da = models.IntegerField(
        choices=[
            [1, 'Para el ganador de la primera vuelta'],
            [2, 'Para el segundo puesto de la primera vuelta'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Votante B: En esta SEGUNDA VUELTA PRESIDENCIAL, ¿para quién son tus votos? Mira el cuadro de abajo si quieres recordar cuántos votos te corresponde dar."
    )
    voto3_2da = models.IntegerField(
        choices=[
            [1, 'Para el ganador de la primera vuelta'],
            [2, 'Para el segundo puesto de la primera vuelta'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Votante C: En esta SEGUNDA VUELTA PRESIDENCIAL, ¿para quién son tus votos? Mira el cuadro de abajo si quieres recordar cuántos votos te corresponde dar."
    )

    #votos para cada político SEGUNDA VUELTA
    votos_1ro_1ra = models.IntegerField()
    votos_2do_1ra = models.IntegerField()
    votos_primero_2da = models.IntegerField()
    votos_segundo_2da = models.IntegerField()
    primero_2da = models.StringField()
    segundo_2da = models.StringField()
    #Quién votó por quién
    voto1_2da_str = models.StringField()
    voto2_2da_str = models.StringField()
    voto3_2da_str = models.StringField()

    def definir_ganador_2da(group):
        if group.habra_segunda == True:
            #1. MULTIPLICA VOTOS
            #Registrar el voto del votante tipo 1
            if group.voto1_2da == 1:
                group.votos_1ro_1ra = Constants.voter1multip
            else:
                group.votos_1ro_1ra = 0
            if group.voto1_2da == 2:
                group.votos_2do_1ra = Constants.voter1multip
            else:
                group.votos_2do_1ra = 0
            #Registrar el voto del votante tipo 2
            if group.voto2_2da == 1:
                group.votos_1ro_1ra = group.votos_1ro_1ra + Constants.voter2multip
            else:
                group.votos_1ro_1ra = group.votos_1ro_1ra
            if group.voto2_2da == 2:
                group.votos_2do_1ra = group.votos_2do_1ra + Constants.voter2multip
            else:
                group.votos_2do_1ra = group.votos_2do_1ra
            #Registrar el voto del votante tipo 3
            if group.voto3_2da == 1:
                group.votos_1ro_1ra = group.votos_1ro_1ra + Constants.voter3multip
            else:
                group.votos_1ro_1ra = group.votos_1ro_1ra
            if group.voto3_2da == 2:
                group.votos_2do_1ra = group.votos_2do_1ra + Constants.voter3multip
            else:
                group.votos_2do_1ra = group.votos_2do_1ra

            #CUENTA VOTOS
            group.votos_primero_2da = max(group.votos_2do_1ra,group.votos_1ro_1ra)
            group.votos_segundo_2da = min(group.votos_2do_1ra,group.votos_1ro_1ra)

            #3. DETERMINA PUESTOS
            if group.votos_primero_2da == group.votos_1ro_1ra:
                group.primero_2da = group.primero
            else:
                group.primero_2da = group.segundo

            if group.votos_segundo_2da == group.votos_1ro_1ra:
                group.segundo_2da = group.primero
            else:
                group.segundo_2da = group.segundo

            jugadores = group.get_players() #jala "ganador" de players
            for jugador in jugadores:
                if group.primero_2da == jugador.role:
                    jugador.ganador = True
                else:
                    jugador.ganador = False

        #Quién votó por quién
            #Presidente
            if group.voto1_2da == 1:
                group.voto1_2da_str = group.primero
            else:
                group.voto1_2da_str = group.segundo
            if group.voto2_2da == 1:
                group.voto2_2da_str = group.primero
            else:
                group.voto2_2da_str = group.segundo
            if group.voto3_2da == 1:
                group.voto3_2da_str = group.primero
            else:
                group.voto3_2da_str = group.segundo


    #Allocations del político ganador a tipos 1, 2, 3
    allocation_1 = models.IntegerField(min=0, max=Constants.budget, label="¿Cuánto le asignarás al Votante tipo A?")
    allocation_2 = models.IntegerField(min=0, max=Constants.budget, label="¿Cuánto le asignarás al Votante tipo B?")
    allocation_3 = models.IntegerField(min=0, max=Constants.budget, label="¿Cuánto le asignarás al Votante tipo C?")
    #Forms: Validating multiple fields together (para Page)

    #Acción del Congreso de aceptar o rechazar. Como integer para luego solo multiplicar y sumar
    accion_a_cong = models.IntegerField(
        choices=[
            [0, 'Rechazar'],
            [1, 'Aceptar']
        ],
        widget=widgets.RadioSelect,
        label="Partido A: ¿Votas por aceptar o por rechazar la propuesta del presidente?"
    )
    accion_b_cong = models.IntegerField(
        choices=[
            [0, 'Rechazar'],
            [1, 'Aceptar']
        ],
        widget=widgets.RadioSelect,
        label="Partido B: ¿Votas por aceptar o por rechazar la propuesta del presidente?"
    )
    accion_c_cong = models.IntegerField(
        choices=[
            [0, 'Rechazar'],
            [1, 'Aceptar']
        ],
        widget=widgets.RadioSelect,
        label="Partido C: ¿Votas por aceptar o por rechazar la propuesta del presidente?"
    )

    #Contrapropuesta del Congreso
    #Allocation del político A a tipos 1, 2, 3
    alloc_a1c = models.IntegerField(min=0, max=Constants.budget, label="Si el Congreso rechaza la propuesta, ¿cuánto le asignarás al Votante tipo A?")
    alloc_a2c = models.IntegerField(min=0, max=Constants.budget, label="Si el Congreso rechaza la propuesta, ¿cuánto le asignarás al Votante tipo B?")
    alloc_a3c = models.IntegerField(min=0, max=Constants.budget, label="Si el Congreso rechaza la propuesta, ¿cuánto le asignarás al Votante tipo C?")
    #Allocation del político B a tipos 1, 2, 3
    alloc_b1c = models.IntegerField(min=0, max=Constants.budget, label="Si el Congreso rechaza la propuesta, ¿cuánto le asignarás al Votante tipo A?")
    alloc_b2c = models.IntegerField(min=0, max=Constants.budget, label="Si el Congreso rechaza la propuesta, ¿cuánto le asignarás al Votante tipo B?")
    alloc_b3c = models.IntegerField(min=0, max=Constants.budget, label="Si el Congreso rechaza la propuesta, ¿cuánto le asignarás al Votante tipo C?")
    #Allocation del político C a tipos 1, 2, 3
    alloc_c1c = models.IntegerField(min=0, max=Constants.budget, label="Si el Congreso rechaza la propuesta, ¿cuánto le asignarás al Votante tipo A?")
    alloc_c2c = models.IntegerField(min=0, max=Constants.budget, label="Si el Congreso rechaza la propuesta, ¿cuánto le asignarás al Votante tipo B?")
    alloc_c3c = models.IntegerField(min=0, max=Constants.budget, label="Si el Congreso rechaza la propuesta, ¿cuánto le asignarás al Votante tipo C?")
    #Validate multiple forms together en el page

    #Decidir si se acepta o rechaza la propuesta y si se implementa contrapropuesta
    accion_a_cong_str = models.StringField()
    accion_b_cong_str = models.StringField()
    accion_c_cong_str = models.StringField()

    decision_congreso = models.StringField()

    final_alloc_1 = models.FloatField()
    final_alloc_2 = models.FloatField()
    final_alloc_3 = models.FloatField()

    def accion_congreso_pagos(group): #Pagos va separado en el presidencial
        jugadorcitos = group.get_players()
        for jugadorcito in jugadorcitos:
            if jugadorcito.congresal == True:
                #String para la acción de cada partido
                if group.accion_a_cong == 1:
                    group.accion_a_cong_str = 'Aceptar'
                else:
                    group.accion_a_cong_str = 'Rechazar'
                if group.accion_b_cong == 1:
                    group.accion_b_cong_str = 'Aceptar'
                else:
                    group.accion_b_cong_str = 'Rechazar'
                if group.accion_c_cong == 1:
                    group.accion_c_cong_str = 'Aceptar'
                else:
                    group.accion_c_cong_str = 'Rechazar'
                #Decidir si aceptar o rechazar
                if group.accion_a_cong*group.votos_a_cong + group.accion_b_cong*group.votos_b_cong + group.accion_c_cong*group.votos_c_cong > 50:
                    group.decision_congreso = 'Aceptar'
                else:
                    group.decision_congreso = 'Rechazar'
                #Si aceptaron, se implementa lo del presidente
                if group.decision_congreso == 'Aceptar':
                    group.final_alloc_1 = group.allocation_1
                    group.final_alloc_2 = group.allocation_2
                    group.final_alloc_3 = group.allocation_3
                #Si rechazaron, se implementa lo del Congreso
                else:
                    group.final_alloc_1 = (group.alloc_a1c*group.votos_a_cong + group.alloc_b1c*group.votos_b_cong + group.alloc_c1c*group.votos_c_cong)/100
                    group.final_alloc_2 = (group.alloc_a2c*group.votos_a_cong + group.alloc_b2c*group.votos_b_cong + group.alloc_c2c*group.votos_c_cong)/100
                    group.final_alloc_3 = (group.alloc_a3c*group.votos_a_cong + group.alloc_b3c*group.votos_b_cong + group.alloc_c3c*group.votos_c_cong)/100

                #Pagos: esto se separa en el presidencial como un set_payoffs y ya
                jugadores = group.get_players() #jala players
                for jugador in jugadores:
                    if jugador.role == Constants.voter1_role or jugador.role == Constants.politiciana_role:
                        jugador.payoff = math.sqrt(group.final_alloc_1)
                    elif jugador.role == Constants.voter2_role or jugador.role == Constants.politicianb_role:
                        jugador.payoff = math.sqrt(group.final_alloc_2)
                    else:
                        jugador.payoff = math.sqrt(group.final_alloc_3)
                    if jugador.ganador == True:
                        jugador.payoff = jugador.payoff + Constants.egorent
                        if group.decision_congreso == 'Rechazar':
                            jugador.payoff = jugador.payoff - Constants.castigo
            else:
                group.final_alloc_1 = group.allocation_1
                group.final_alloc_2 = group.allocation_2
                group.final_alloc_3 = group.allocation_3
                #Pagos: esto se separa en el presidencial como un set_payoffs y ya
                jugadores = group.get_players() #jala players
                for jugador in jugadores:
                    if jugador.role == Constants.voter1_role or jugador.role == Constants.politiciana_role:
                        jugador.payoff = math.sqrt(group.final_alloc_1)
                    elif jugador.role == Constants.voter2_role or jugador.role == Constants.politicianb_role:
                        jugador.payoff = math.sqrt(group.final_alloc_2)
                    else:
                        jugador.payoff = math.sqrt(group.final_alloc_3)
                    if jugador.ganador == True:
                        jugador.payoff = jugador.payoff + Constants.egorent


class Player(BasePlayer):
    #variable de ganador de las elecciones
    ganador = models.BooleanField()

    #Participant vars que se guardan al final del experimento
    congresal = models.BooleanField()
    primera_regla = models.StringField()
    poblacion = models.IntegerField()

    #Crees que el presidente cumplirá su promesa?
    cumplira_promesa = models.IntegerField(
        choices=[
            [1, 'Muy poco'],
            [2, 'Poco'],
            [3, 'Neutral'],
            [4, 'Mucho'],
            [5, 'Muchísimo'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="¿Qué tan probable crees que sea que el presidente cumpla su promesa?"
    )

    #Aprobación del gobierno
    aprueba = models.IntegerField(
        choices=[
            [1, 'Muy poco'],
            [2, 'Poco'],
            [3, 'Neutral'],
            [4, 'Mucho'],
            [5, 'Muchísimo'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="¿Apruebas la labor del presidente en esta ronda?"
    )

    aprueba_cong = models.IntegerField(
        choices=[
            [1, 'Muy poco'],
            [2, 'Poco'],
            [3, 'Neutral'],
            [4, 'Mucho'],
            [5, 'Muchísimo'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="¿Apruebas la labor del Congreso en esta ronda?"
    )

    aprueba_cong_own = models.IntegerField(
        choices=[
            [1, 'Muy poco'],
            [2, 'Poco'],
            [3, 'Neutral'],
            [4, 'Mucho'],
            [5, 'Muchísimo'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="¿Apruebas la labor del congresista por quien votaste en esta ronda?"
    )

    aprueba_resultado = models.IntegerField(
        choices=[
            [1, 'Muy poco'],
            [2, 'Poco'],
            [3, 'Neutral'],
            [4, 'Mucho'],
            [5, 'Muchísimo'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="¿Estás satisfecho con el resultado de esta ronda?"
    )