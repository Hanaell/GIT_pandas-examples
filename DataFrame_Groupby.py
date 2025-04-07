# -*- coding: utf-8 -*-
__author__ = 'Florian'

import pandas as pd
import numpy as np

# Vérification du chemin et encodage
try:
    userHeader = ['user_id', 'gender', 'age', 'occupation', 'zip']
    users = pd.read_csv('/home/florian.ladreyt@Digital-Grenoble.local/Desktop/MonProjet/GIT_pandas-examples/dataSet/users.txt', engine='python',
                        sep='::', header=None, names=userHeader, encoding='ISO-8859-1')

    movieHeader = ['/home/florian.ladreyt@Digital-Grenoble.local/Desktop/MonProjet/GIT_pandas-examples/dataSet/movies.txt', 'title', 'genres']
    movies = pd.read_csv('dataSet/movies.txt', engine='python',
                         sep='::', header=None, names=movieHeader, encoding='ISO-8859-1')

    ratingHeader = ['/home/florian.ladreyt@Digital-Grenoble.local/Desktop/MonProjet/GIT_pandas-examples/dataSet/users.txt', 'movie_id', 'rating', 'timestamp']
    ratings = pd.read_csv('dataSet/ratings.txt', engine='python',
                          sep='::', header=None, names=ratingHeader, encoding='ISO-8859-1')
except FileNotFoundError as e:
    print(f"Erreur : Fichier non trouvé. Vérifiez le chemin.\n{e}")
    exit()
except UnicodeDecodeError as e:
    print(f"Erreur : Encodage incorrect. Essayez ISO-8859-1.\n{e}")
    exit()

# Fusion des données
try:
    mergeRatings = pd.merge(pd.merge(users, ratings), movies)
except KeyError as e:
    print(f"Erreur : Problème de fusion. Vérifiez les colonnes.\n{e}")
    exit()

# Films avec le plus de votes
try:
    numberRatings = mergeRatings.groupby('title').size().sort_values(ascending=False)
    print('Films with more votes: \n%s' % numberRatings[:10])
    print('\n==================================================================\n')
except Exception as e:
    print(f"Erreur lors du calcul des votes.\n{e}")

# Notes moyennes des films
try:
    avgRatings = mergeRatings.groupby(['movie_id', 'title'])['rating'].mean()
    print('Avg ratings: \n%s' % avgRatings[:10])
    print('\n==================================================================\n')
except Exception as e:
    print(f"Erreur lors du calcul des notes moyennes.\n{e}")

# Informations détaillées sur les films
try:
    dataRatings = mergeRatings.groupby(['movie_id', 'title'])['rating'].agg(['mean', 'sum', 'count', 'std'])
    print('Films ratings info: \n%s' % dataRatings[:10])
    print('\n==================================================================\n')
except Exception as e:
    print(f"Erreur lors du calcul des statistiques détaillées.\n{e}")

# Statistiques personnalisées avec lambda
try:
    myAvg = mergeRatings.groupby(['movie_id', 'title'])['rating'].agg(
        SUM=np.sum,
        COUNT=np.size,
        AVG=np.mean,
        myAVG=lambda x: x.sum() / float(x.count())
    )
    print('My info ratings: \n%s' % myAvg[:10])
    print('\n==================================================================\n')
except Exception as e:
    print(f"Erreur lors du calcul des statistiques personnalisées.\n{e}")

# Tri par nombre de votes
try:
    sortRatingsField = mergeRatings.groupby(['movie_id', 'title'])['rating'].agg(
        COUNT=np.size,
        myAVG=lambda x: x.sum() / float(x.count())
    ).sort_values(by='COUNT', ascending=False)
    print('My info sorted: \n%s' % sortRatingsField[:15])
except Exception as e:
    print(f"Erreur lors du tri des statistiques.\n{e}")
