import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from words_and_data.words import *


def generate_word_count_figure(words, word_count, path_to_save):
    # Instantiate figure
    fig, ax = plt.subplots(figsize=(30, 10))
    # Set labels
    ax.set_xlabel('Words')
    ax.set_ylabel('Times Found')
    ax.set_title('Most Popular Words')
    plt.bar(words, word_count)
    # Save figure
    plt.savefig(path_to_save)


def generate_room_type_figure(df, path_to_save):
    room_types = df['room_type'].value_counts().to_numpy()
    total = room_types.sum()
    labels = ['Entire home/apt', 'Private room', 'Shared room']
    # Instantiate figure
    fig, ax = plt.subplots(figsize=(30, 10))
    # Set labels
    ax.set_xlabel('Room Type')
    ax.set_ylabel('Percentage of Total')
    ax.set_title('Types of rooms in dataset')
    ax.set_ylim(0, 100)
    plt.bar(labels, (room_types/total)*100)
    # Save figure
    plt.savefig(path_to_save)


def generate_neighbourhood_figure(df, path_to_save):
    # Create neighbourhood subset dataframs
    df_manhattan = df[df['neighbourhood_group'] == 'Manhattan']
    df_brooklyn = df[df['neighbourhood_group'] == 'Brooklyn']
    df_queens = df[df['neighbourhood_group'] == 'Queens']
    df_bronx = df[df['neighbourhood_group'] == 'Bronx']
    df_staten_island = df[df['neighbourhood_group'] == 'Staten Island']

    name_list = ['Manhattan', 'Brooklyn', 'Queens', 'Staten_Island', 'Bronx']

    # Instantiate figure
    fig, axs = plt.subplots(figsize=(30, 10), ncols=5)

    # Plot
    sns.regplot(df_manhattan.groupby(['neighbourhood']).mean()['price'],
                df_manhattan.groupby(['neighbourhood']).mean()['reviews_per_month'],
                ax=axs[0])
    sns.regplot(df_brooklyn.groupby(['neighbourhood']).mean()['price'],
                df_brooklyn.groupby(['neighbourhood']).mean()['reviews_per_month'],
                ax=axs[1])
    sns.regplot(df_queens.groupby(['neighbourhood']).mean()['price'],
                df_queens.groupby(['neighbourhood']).mean()['reviews_per_month'],
                ax=axs[2])
    sns.regplot(df_staten_island.groupby(['neighbourhood']).mean()['price'],
                df_staten_island.groupby(['neighbourhood']).mean()['reviews_per_month'],
                ax=axs[3])
    sns.regplot(df_bronx.groupby(['neighbourhood']).mean()['price'],
                df_bronx.groupby(['neighbourhood']).mean()['reviews_per_month'],
                ax=axs[4])

    # Set labels
    for i in range(5):
        axs[i].set_title(name_list[i])
        axs[i].set_xlabel('Price')
        axs[i].set_ylabel('Reviews Per Month')
        axs[i].set_xlim(0, 500)
        axs[i].set_ylim(0, 5)

    # Save figure
    fig.savefig(path_to_save)

if __name__ == '__main__':

    # Read in data
    df = pd.read_csv('words_and_data/data/AB_NYC_2019.csv')

    generate_neighbourhood_figure(df, 'images/neighbourhood.png')

    top_words, counts = compute_word_counts(
        filepath='words_and_data/intermediate_files/counts.npz')
    # Remove punctuation from the word counts
    del top_words[1]
    del top_words[1]
    del counts[1]
    del counts[1]
    # Remove the number 1 from the list
    del top_words[9]
    del counts[9]

    generate_word_count_figure(top_words[:10],
                               counts[:10], 'images/word_count.png')

    generate_room_type_figure(df, 'images/room_types.png')
