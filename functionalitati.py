import pandas as pd
import random

# Configurare functie preluare valori din ./data/Frequency list-en-ro.csv

data = pd.read_csv('./data/Frequency list-en-ro.csv')
learn = data.to_dict('records')


def afisare():
    """Functie preluare random valoare din ./data/Frequency list-en-ro.csv"""
    ran_choice = random.choice(learn)
    return ran_choice

