SESSION_CONFIGS = [
     dict(
        name='presidencial',
        display_name="presidencial",
        num_demo_participants=6,
        app_sequence=['inicial','elec_plur_pob1', 'elec_plur_pob2', 'elec_runo_pob1', 'elec_runo_pob2'],
        group="presidencial"
        ),
     dict(
        name='congresal',
        display_name="congresal",
        num_demo_participants=6,
        app_sequence=['inicial','elec_plur_pob1', 'elec_plur_pob2', 'elec_runo_pob1', 'elec_runo_pob2'],
        group="congresal"
        )
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1, participation_fee=0, doc=""
)
```

#En cada sesión, hay que cambiar:
#App sequence en settings
#App 'final': tabla en Pago_final.html y aleatorización en pages

#En cada app hay que cambiar:
#Direcciones de los templates en Constants
#Population en Constants
#Runoff en Constants
#Orden de los roles en Constants