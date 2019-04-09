# Data manipulation
import numpy as np
import pandas as pd

# Data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Display propertice
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)

# Date
import datetime

# Maps
#import geopandas as gpd
#import pycountry

from math import pi

def analysis():
    df_fifa19 = pd.read_csv('/home/kalyan/PycharmProjects/fifa19/Home/data.csv')
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
    print(df.head())
    plt.rcParams['figure.figsize']=(25,16)
    hm=sns.heatmap(df[['Age', 'Overall', 'Potential', 'Value', 'Wage',
                    'Acceleration', 'Aggression', 'Agility', 'Balance', 'BallControl',
                    'Body Type','Composure', 'Crossing','Dribbling', 'FKAccuracy', 'Finishing',
                    'HeadingAccuracy', 'Interceptions','International Reputation',
                    'Joined', 'Jumping', 'LongPassing', 'LongShots',
                    'Marking', 'Penalties', 'Position', 'Positioning',
                    'ShortPassing', 'ShotPower', 'Skill Moves', 'SlidingTackle',
                    'SprintSpeed', 'Stamina', 'StandingTackle', 'Strength', 'Vision',
                    'Volleys']].corr(), annot = True, linewidths=.5, cmap='Blues')
    hm.set_title(label='Heatmap of dataset', fontsize=20)
    figure = hm.get_figure()
    figure.savefig("static/images/heatmap.png")
    #---------------------------------------------------------------------------
    sns.set(style ="dark", palette="colorblind", color_codes=True)
    x = df.Age
    plt.figure(figsize=(12,8))
    ax = sns.distplot(x, bins = 58, kde = False, color='g')
    ax.set_xlabel(xlabel="Player\'s age", fontsize=16)
    ax.set_ylabel(ylabel='Number of players', fontsize=16)
    ax.set_title(label='Histogram of players age', fontsize=20)
    plt.savefig("static/images/histogram.png")
    #---------------------------------------------------------------------------
    some_clubs = ('Juventus', 'Real Madrid', 'Paris Saint-Germain', 'FC Barcelona', 'Legia Warszawa', 'Manchester United')
    df_club = df.loc[df['Club'].isin(some_clubs) & df['Age']]

    fig, ax = plt.subplots()
    fig.set_size_inches(20, 10)
    ax = sns.violinplot(x="Club", y="Age", data=df_club);
    ax.set_title(label='Distribution of age in some clubs', fontsize=20);
    fig.savefig("static/images/distofages.png")
    #---------------------------------------------------------------------------
    # The clubs and their players overalls
    some_clubs = ('Juventus', 'Real Madrid', 'Paris Saint-Germain', 'FC Barcelona', 'Legia Warszawa', 'Manchester United')
    df_club = df.loc[df['Club'].isin(some_clubs) & df['Age'] & df['Overall'] ]

    ax = sns.barplot(x=df_club['Club'], y=df_club['Overall'], palette="rocket");
    ax.set_title(label='Distribution overall in several clubs', fontsize=20);
    barplot = ax.get_figure()
    barplot.savefig("static/images/overalls.png")
    #---------------------------------------------------------------------------
    # All of position
    ax = sns.countplot(x = 'Position', data = df, palette = 'hls');
    ax.set_title(label='Count of players on the position', fontsize=20);
    countplot = ax.get_figure()
    countplot.savefig("static/images/playerspos.png")
    #---------------------------------------------------------------------------
    player_features = (
    'Acceleration', 'Aggression', 'Agility',
    'Balance', 'BallControl', 'Composure',
    'Crossing', 'Dribbling', 'FKAccuracy',
    'Finishing', 'GKDiving', 'GKHandling',
    'GKKicking', 'GKPositioning', 'GKReflexes',
    'HeadingAccuracy', 'Interceptions', 'Jumping',
    'LongPassing', 'LongShots', 'Marking', 'Penalties'
    )

    idx = 1
    plt.figure(figsize=(15,45))
    for position_name, features in df.groupby(df['Position'])[player_features].mean().iterrows():
        top_features = dict(features.nlargest(5))

        # number of variable
        categories=top_features.keys()
        N = len(categories)

        # We are going to plot the first line of the data frame.
        # But we need to repeat the first value to close the circular graph:
        values = list(top_features.values())
        values += values[:1]

        # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        # Initialise the spider plot
        ax = plt.subplot(9, 3, idx, polar=True)

        # Draw one axe per variable + add labels labels yet
        plt.xticks(angles[:-1], categories, color='grey', size=8)

        # Draw ylabels
        ax.set_rlabel_position(0)
        plt.yticks([25,50,75], ["25","50","75"], color="grey", size=7)
        plt.ylim(0,100)

        plt.subplots_adjust(hspace = 0.5)

        # Plot data
        ax.plot(angles, values, linewidth=1, linestyle='solid')

        # Fill area
        ax.fill(angles, values, 'b', alpha=0.1)

        plt.title(position_name, size=11, y=1.1)

        idx += 1
    plt.savefig("static/images/cirgraph.png")

    #---------------------------------------------------------------------------
    # Relation dribbling and crossing with respected finishing of players
    plt.figure(figsize=(14,7))
    cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)

    ax = sns.scatterplot(x='Crossing', y='Dribbling',
                         hue='Finishing',
                         palette=cmap, sizes=(1, 1),
                         data=df)
    ax.set_title(label='Relation dribbling and crossing with respected finishing of players', fontsize=20);
    plt.savefig("static/images/dirb_vs_cross.png")
    #---------------------------------------------------------------------------
    # Relation stamina and age with respected sprint speed of players
    cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)

    ax = sns.scatterplot(x='Age', y='Stamina',
                         hue='SprintSpeed',
                         palette=cmap, sizes=(1, 1),
                         data=df)
    ax.set_title(label='Relation stamina and age with respected sprint speed of players', fontsize=20);
    scatterplot = ax.get_figure()
    scatterplot.savefig("static/images/stamina_vs_age.png")

if __name__ == "__main__":
    analysis()
