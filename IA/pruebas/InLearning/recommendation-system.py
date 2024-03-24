import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix

#Cargamos los datos
ratings = pd.read_csv("C:/Users/eiven/OneDrive/Documentos/Programacion/Python/IA/pruebas/InLearning/ratings.csv", encoding='latin1')
movies = pd.read_csv("C:/Users/eiven/OneDrive/Documentos/Programacion/Python/IA/pruebas/InLearning/movies.csv", encoding='latin1')

#Creamos una matrix de usuario-item

def create_matrix(df):
    N = len(df['userId'].unique())
    M = len(df['movieId'].unique())
    user_mapper = dict(zip(np.unique(df['userId']), list(range(N))))
    movie_mapper = dict(zip(np.unique(df['movieId']), list(range(M))))
    user_inv_mapper = dict(zip(list(range(N)), np.unique(df['userId'])))
    movie_inv_mapper = dict(zip(list(range(M)), np.unique(df['movieId'])))
    user_index = [user_mapper[i] for i in df['userId']]
    movie_index = [movie_mapper[i] for i in df['movieId']]
    x = csr_matrix((df['rating'], (movie_index, user_index)), shape = (M, N))
    return x, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper

x, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper = create_matrix(ratings)

#Creamos una funcion para encontrar peliculas similares
def find_similar_movies(movie_id, X, k, metric = 'cosine', show_distance = False):
    neighbour_ids = []
    movie_ind = movie_mapper[movie_id]
    movie_vec = X[movie_ind]
    k += 1
    KNN = NearestNeighbors(n_neighbors = k, algorithm = "brute", metric = metric)
    KNN.fit(X)
    movie_vec = movie_vec.reshape(1, -1)
    neighbour = KNN.kneighbors(movie_vec, return_distance = show_distance)
    for i in range (0, k):
        n = neighbour.item(i)
        neighbour_ids.append(movie_inv_mapper[n])
    neighbour_ids.pop(0)
    return neighbour_ids

#Pasamos a crear un diccionario para ubicar las ID's de los titulos
movie_titles = dict(zip(movies['movieId'], movies['title']))

#Creamos un test del sistema de recomendaciones
movie_id = 7
similar_ids = find_similar_movies(movie_id, x, k = 10)
movie_title = movie_titles[movie_id]

print (f"Dado que viste {movie_title}")
for i in similar_ids:
    print(movie_titles[i])