from typing import Any
import numpy as np

from src.dataset import oddEvenPatterns, lowHighPatterns

# This function take as input the number of draw to generate and create them.
def generateRandomDraws(n : int = 5000) -> Any:
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
    # N1 to N5 numbers
    array_numeros = firstDraw[:5]
    # E1 and E2 numbers
    array_etoiles = firstDraw[-2:]
    
    # for the number of draw to generate
    for i in range(n):
        # generate a random 5 numbers between 1 and 50 included
        numeros_generation = np.random.choice(np.arange(1, 51), replace=False, size=(5,))
        
        # generate 5 new number until they are all different
        while (np.sort(array_numeros) == np.sort(numeros_generation)).all():
            numeros_generation = np.random.choice(np.arange(1, 51), replace=False, size=(5,))
        
        # generate 2 random number between 1 and 12 included 
        etoiles_generation = np.random.choice(np.arange(1, 13), replace=False, size=(2,))
        
        # generate 2 new numbers until they are all different
        while (np.sort(array_etoiles) == np.sort(etoiles_generation)).all():
            etoiles_generation = np.random.choice(np.arange(1, 13), replace=False, size=(2,))
        
        # the 5 numbers between 1 and 50 and the 2 between 1 and 12 are concatened in a same var
        row_to_append = np.concatenate((numeros_generation, etoiles_generation), axis=0)
        
        # calcul the oddEvenPattern probability and add it to the 7 numbers of the draw
        row_to_append = np.concatenate((row_to_append, [oddEvenPatterns(numeros_generation)]), axis=0)
        # calcul the lowHighPatterns probability and add it to the 7 numbers of the draw
        row_to_append = np.concatenate((row_to_append, [lowHighPatterns(numeros_generation)]), axis=0)
        
        # res append the generated draw
        res.append(row_to_append)
        
    # return res not as a list but as an np array
    return np.array(res)

    
