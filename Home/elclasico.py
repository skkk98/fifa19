import numpy as np
import pandas as pd

df_fifa19 = pd.read_csv('data.csv')
chosen_columns = [
        'Name',
        'Age',
        'Nationality',
        'Overall',
        'Potential',
        'Special',
        'Acceleration',
        'Aggression',
        'Agility',
        'Balance',
        'BallControl',
        'Body Type',
        'Composure',
        'Crossing',
        'Curve',
        'Club',
        'Dribbling',
        'FKAccuracy',
        'Finishing',
        'GKDiving',
        'GKHandling',
        'GKKicking',
        'GKPositioning',
        'GKReflexes',
        'HeadingAccuracy',
        'Interceptions',
        'International Reputation',
        'Jersey Number',
        'Jumping',
        'Joined',
        'LongPassing',
        'LongShots',
        'Marking',
        'Penalties',
        'Position',
        'Positioning',
        'Preferred Foot',
        'Reactions',
        'ShortPassing',
        'ShotPower',
        'Skill Moves',
        'SlidingTackle',
        'SprintSpeed',
        'Stamina',
        'StandingTackle',
        'Strength',
        'Value',
        'Vision',
        'Volleys',
        'Wage',
        'Weak Foot',
        'Work Rate'
    ]
df = pd.DataFrame(df_fifa19, columns = chosen_columns)

barca = df[df['Club'] == 'FC Barcelona']
madrid = df[df['Club'] == 'Real Madrid']
frames = [barca, madrid]
clasico = pd.concat(frames)

print(clasico)

clasico.to_csv('elclasico.csv')
