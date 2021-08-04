from os import environ

SESSION_CONFIGS = [
     dict(
        name='presidencial_plur_pob1',
        display_name="presidencial_plur_pob1",
        num_demo_participants=6,
        app_sequence=['inicial','prac',
        'elec_plur_pob1','elec_runo_pob1',
        'inicial_jueguitos','dictator','trust','ultimatum','lying',
        'final'
        ],
        congreso=False,
        primera_regla="plur",
        poblacion=1,
        ),
     dict(
        name='presidencial_plur_pob2',
        display_name="presidencial_plur_pob2",
        num_demo_participants=6,
        app_sequence=['inicial','prac',
        'elec_plur_pob2','elec_runo_pob2',
        'inicial_jueguitos','dictator','trust','ultimatum','lying',
        'final'
        ],
        congreso=False,
        primera_regla="plur",
        poblacion=2,
        ),
     dict(
        name='presidencial_runo_pob1',
        display_name="presidencial_runo_pob1",
        num_demo_participants=6,
        app_sequence=['inicial','prac',
        'elec_runo_pob1','elec_plur_pob1',
        'inicial_jueguitos','dictator','trust','ultimatum','lying',
        'final'
        ],
        congreso=False,
        primera_regla="runo",
        poblacion=1,
        ),
     dict(
        name='presidencial_runo_pob2',
        display_name="presidencial_runo_pob2",
        num_demo_participants=6,
        app_sequence=['inicial','prac',
        'elec_runo_pob2','elec_plur_pob2',
        'inicial_jueguitos','dictator','trust','ultimatum','lying',
        'final'
        ],
        congreso=False,
        primera_regla="runo",
        poblacion=2,
        ),
     dict(
        name='congresal_plur_pob1',
        display_name="congresal_plur_pob1",
        num_demo_participants=6,
        app_sequence=['inicial','prac',
        'elec_plur_pob1','elec_runo_pob1',
        'inicial_jueguitos','dictator','trust','ultimatum','lying',
        'final'
        ],
        congreso=True,
        primera_regla="plur",
        poblacion=1,
        ),
     dict(
        name='congresal_plur_pob2',
        display_name="congresal_plur_pob2",
        num_demo_participants=6,
        app_sequence=['inicial','prac',
        'elec_plur_pob2','elec_runo_pob2',
        'inicial_jueguitos','dictator','trust','ultimatum','lying',
        'final'
        ],
        congreso=True,
        primera_regla="plur",
        poblacion=2,
        ),
     dict(
        name='congresal_runo_pob1',
        display_name="congresal_runo_pob1",
        num_demo_participants=6,
        app_sequence=['inicial','prac',
        'elec_runo_pob1','elec_plur_pob1',
        'inicial_jueguitos','dictator','trust','ultimatum','lying',
        'final'
        ],
        congreso=True,
        primera_regla="runo",
        poblacion=1,
        ),
     dict(
        name='congresal_runo_pob2',
        display_name="congresal_runo_pob2",
        num_demo_participants=6,
        app_sequence=['inicial','prac',
        'elec_runo_pob2','elec_plur_pob2',
        'inicial_jueguitos','dictator','trust','ultimatum','lying',
        'final'
        ],
        congreso=True,
        primera_regla="runo",
        poblacion=2,
        )
]

#En cada sesión, hay que cambiar:
#App sequence en settings
#App 'final': tabla en Pago_final.html y aleatorización en pages
#App de practica: ponerle el runoff y pob correcto

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

PARTICIPANT_FIELDS = ['congresal','primera_regla','poblacion',
    'total_payoff_plur_pob1','total_payoff_plur_pob2','total_payoff_runo_pob1','total_payoff_runo_pob2',
    'rol_plur_pob1','rol_plur_pob2','rol_runo_pob1','rol_runo_pob2',
    'paid_in','rol_demo1','rol_demo2','puntos_demo1','puntos_demo2',
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
