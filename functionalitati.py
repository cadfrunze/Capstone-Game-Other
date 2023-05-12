import pandas as pd
import random

data = pd.read_csv('./data/Frequency list-en-ro.csv')
learn = data.to_dict('records')


def afisare():
    """Functionalitate random cuvinte din Frequency list-en-ro.csv"""
    ran_choice = random.choice(learn)
    return ran_choice

