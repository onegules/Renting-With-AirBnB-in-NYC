# Renting with Airbnb in NYC

## Project Overview

This is the github repository for a blog post found here ____________. This
repository contains all of my analysis and generated images that I used for the
post.

## Data

The data can be downloaded from [here](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data).
Put this data in words_and_data/data if you'd like to run any of the files in this
project.

## The files and folders

### images

The images folder contains all the generated images as well as the image I used
for the thumbnail.

### words_and_data

This folder contains another folder called data where the data should be saved.

Next, there is the intermediate_files folder that has all of the intermediate files
that were used such as counts.npz and df_cozy. These are used for analysis and are
saved here to be read in as this greatly improves run time for the python scripts.
You can see how these are generated in Exploratory_Data_Analysis.html.

Then there is the __init__.py file that is empty and is there for to allow
for words.py to be imported outside of this folder.

Finally, words.py generates word counts from the data csv to find the top 20
words and saves it in /intermediate_files/counts.npz to be read in later.

### Exploratory_Data_Analysis

This file contains all the information for the preliminary data analysis I did.
It contains all the intermediary steps I took in case you'd like to repeat the
process.

### generate_figures

Finally generate_figures is named such because it generates the figures saved to
the images folder. Run this file to generate them again in case they get lost.

## Difficulties

As stated when describing the folders, a big problem I had was the run time.
Individual cells would take a long time but I got around it by saving the intermediate
steps. This did make the folder a bit crowded however but it made the jupyter notebook
run much faster.

The next major difficulty I had was with the regressions. I performed many
regressions including single and multiple linear regressions using the various columns
available, however none of them had an R squared value of over 50% and thus I
didn't use them in the write up for the blog post.
