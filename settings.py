from os import environ

SESSION_CONFIGS = [
     dict(
        name='presidencial',
        display_name="presidencial",
        num_demo_participants=6,
        app_sequence=['inicial',
        'elec_plur_pob1','elec_runo_pob1',
        #'elec_plur_pob2','elec_runo_pob2',
        'inicial_jueguitos','dictator','trust','ultimatum','lying','measure_task',
        'final'
        ],
        congreso=False,
            ),
     dict(
        name='congresal',
        display_name="congresal",
        num_demo_participants=6,
        app_sequence=['inicial',
        'elec_runo_pob1','elec_plur_pob1',
        #'elec_plur_pob2','elec_runo_pob2',
        'inicial_jueguitos','dictator','trust','ultimatum','lying','measure_task',
        'final'
        ],
        congreso=True,
        )
]

#En cada sesión, hay que cambiar:
#App sequence en settings
#App 'final': tabla en Pago_final.html y aleatorización en pages

#En cada app hay que cambiar:
#Direcciones de los templates en Constants
#Population en Constants
#Runoff en Constants
#Orden de los roles en Constants
#name in url en Constants
#nombre del participant var "total payoff" en pages
#nombre del participant var "rol_...." en pages
#nombre de la carpeta en templates

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1, participation_fee=0, doc=""
)

PARTICIPANT_FIELDS = ['congresal',
    'total_payoff_plur_pob1','total_payoff_plur_pob2','total_payoff_runo_pob1','total_payoff_runo_pob2',
    'rol_plur_pob1','rol_plur_pob2','rol_runo_pob1','rol_runo_pob2',
    'paid_in',
    'pago_final_final']

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = ''
REAL_WORLD_CURRENCY_DECIMAL_POINTS = 2
USE_POINTS = False

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(
        name='e2labup',
        display_name='E2LabUP - Room para sesiones online',
        participant_label_file='_rooms/e2labup-room.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = 'lgxul9c+b0(y%q74&6*ww9-97j9y!m%qw!x_-y0*vpdd#!e_&0'

INSTALLED_APPS = ['otree']
