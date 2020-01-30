import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_word_count_figure(df, path_to_save):
    pass

def generate_room_type_figure(df, path_to_save):
    pass


def generate_neighbourhood_figure(df, path_to_save):
    df_manhattan = df[df['neighbourhood_group']=='Manhattan']
    df_brooklyn = df[df['neighbourhood_group'] == 'Brooklyn']
    df_queens = df[df['neighbourhood_group'] == 'Queens']
    df_bronx = df[df['neighbourhood_group'] == 'Bronx']
    df_staten_island = df[df['neighbourhood_group'] == 'Staten Island']

    name_list = ['Manhattan', 'Brooklyn', 'Queens', 'Staten_Island', 'Bronx']
    fig, axs = plt.subplots(figsize=(30, 10),ncols=5)

    sns.regplot(df_manhattan.groupby(['neighbourhood']).mean()['price'], df_manhattan.groupby(['neighbourhood']).mean()['reviews_per_month'], ax=axs[0]).set
    sns.regplot(df_brooklyn.groupby(['neighbourhood']).mean()['price'], df_brooklyn.groupby(['neighbourhood']).mean()['reviews_per_month'], ax=axs[1])
    sns.regplot(df_queens.groupby(['neighbourhood']).mean()['price'], df_queens.groupby(['neighbourhood']).mean()['reviews_per_month'],ax=axs[2])
    sns.regplot(df_staten_island.groupby(['neighbourhood']).mean()['price'], df_staten_island.groupby(['neighbourhood']).mean()['reviews_per_month'],ax=axs[3])
    sns.regplot(df_bronx.groupby(['neighbourhood']).mean()['price'], df_bronx.groupby(['neighbourhood']).mean()['reviews_per_month'], ax=axs[4])
    for i in range(5):
        axs[i].set_title(name_list[i])
        axs[i].set_xlabel('Price')
        axs[i].set_ylabel('Reviews Per Month')
        axs[i].set_xlim(0,500)
        axs[i].set_ylim(0,5)

    fig.savefig(path_to_save)

if __name__ == '__main__':
    df = pd.read_csv('AB_NYC_2019.csv')
    generate_neighbourhood_figure(df, 'images/neighbourhood.png')
