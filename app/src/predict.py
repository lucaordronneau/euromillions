import numpy as np
import os, inspect, sys

from joblib import load
from src.dataset import oddEvenPatterns, lowHighPatterns

from itertools import combinations



def generateRandomDraws(n = 5000):
    res = []
    # generate a draw randomly
    firstDraw = np.concatenate( (np.random.choice(np.arange(1, 51), replace=False, size=(5,)) ,np.random.choice(np.arange(1, 13), replace=False, size=(2,))) , axis = 0)
    
    array_numeros = firstDraw[:5]
    array_etoiles = firstDraw[-2:]
    
    for i in range(n):
        numeros_generation = np.random.choice(np.arange(1, 51), replace=False, size=(5,))
        while (np.sort(array_numeros) == np.sort(numeros_generation)).all():
            numeros_generation = np.random.choice(np.arange(1, 51), replace=False, size=(5,))
        
        etoiles_generation = np.random.choice(np.arange(1, 13), replace=False, size=(2,))
        while (np.sort(array_etoiles) == np.sort(etoiles_generation)).all():
            etoiles_generation = np.random.choice(np.arange(1, 13), replace=False, size=(2,))
            
        row_to_append = np.concatenate((numeros_generation, etoiles_generation), axis=0)
        row_to_append = np.concatenate((row_to_append, [oddEvenPatterns(numeros_generation)]), axis=0)
        row_to_append = np.concatenate((row_to_append, [lowHighPatterns(numeros_generation)]), axis=0)
        
        res.append(row_to_append)
    return np.array(res)

    
