import numpy as np
import os, inspect

from joblib import load
from src.dataset import oddEvenPatterns, lowHighPatterns

from itertools import combinations

# this function get the path where the model is saved and load it
def loadModel():
    """
    This function get the path where the model is saved and load it

    Args:
        No args are needed

    Returns:
        load the model
    """ 
    # get the current directory dir
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    # get parent dir to get model
    parentdir = os.path.dirname(currentdir)
    
    # call the function load with the path to load the prediction model
    return load(parentdir + '/src/data/model/model.jolib')



# This function take as input the number of draw to generate and create them.
def generateRandomDraws(n : int = 5000):
    """
    This function take as input the number of draw to generate and create Draw type draws


    Args:
       n (int) : the number of Draw type draws to predict. If the value is given, n is 5000

    Returns:
        res (np.array) : res contain all the draws generated.
    """ 
    
    # init the list that will contain all the generated draws
    res = []
    
    # generate a draw randomly
    firstDraw = np.concatenate( (np.random.choice(np.arange(1, 51), replace=False, size=(5,)) ,np.random.choice(np.arange(1, 13), replace=False, size=(2,))) , axis = 0)
    
    # split the draw in two to calculate the feature that we add for the prediction (see oddEvenPatterns and lowHighPatterns in src.dataset for more info)
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

    
