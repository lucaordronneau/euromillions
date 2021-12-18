import numpy as np

def oddEvenPatterns(t: np.array) -> float:
    """Feature engineering according to even and odd numbers.
    Output probabilities are applied.

    Args:
        t (np.array): array of 5 numbers

    Returns:
        float: probability of this draw 
    """
    nb = sum(1-n%2 for n in t)
    if ((nb==1) or (nb==4)):
        result = 0.1492618323925310
    elif ((nb == 3) or (nb==2)):
        result = 0.3256621797655230
    else:
        result = 0.0250759878419453
    return result

def lowHighPatterns(t: np.array) -> float:
    """Feature engineering according to low and high numbers.
    Output probabilities are applied.

    Args:
        t (np.array): array of 5 numbers

    Returns:
        float: probability of this draw 
    """
    nb = sum(n<26 for n in t)
    if ((nb==1) or (nb==4)):
        result = 0.1492618323925310
    elif ((nb == 3) or (nb==2)):
        result = 0.3256621797655230
    else:
        result = 0.0250759878419453
    return result

def createDraws(tirages: np.array, n=4) -> np.array:
    """Allows us to increment our dataset with new draws

    Args:
        tirages (np.array): dataset
        n (int, optional): Add n draw by draw. Defaults to 4.

    Returns:
        np.array: augmented dataset
    """
    tirages_tmp = np.copy(tirages)
    l = []
    for t in tirages_tmp:
        tmp = np.copy(t[:5])
        t = np.append(t, [oddEvenPatterns(tmp)], axis=0)
        t = np.append(t, [lowHighPatterns(tmp)], axis=0)
        t = np.append(t, [1], axis=0)
        l.append(t)
    tirages_tmp = np.array(l)
    
    for tirage in tirages:
        
        array_numeros = tirage[:5]
        array_etoiles = tirage[-2:]
        
        for i in range(n):
            # Generate 5 numbers different from the draw numbers and each numbers different between themselves
            numeros_generation = np.random.choice(np.arange(1, 51), replace=False, size=(5,))
            while (np.sort(array_numeros) == np.sort(numeros_generation)).all():
                numeros_generation = np.random.choice(np.arange(1, 51), replace=False, size=(5,))
            
            # Generate 2 stars different from the draw stars and each stars different between themselves
            etoiles_generation = np.random.choice(np.arange(1, 13), replace=False, size=(2,))
            while (np.sort(array_etoiles) == np.sort(etoiles_generation)).all():
                etoiles_generation = np.random.choice(np.arange(1, 13), replace=False, size=(2,))
            
            # Feature engineering on the generated draw
            row_to_append = np.concatenate((numeros_generation, etoiles_generation), axis=0)
            row_to_append = np.concatenate((row_to_append, [oddEvenPatterns(numeros_generation)]), axis=0)
            row_to_append = np.concatenate((row_to_append, [lowHighPatterns(numeros_generation)]), axis=0)
            row_to_append = np.concatenate((row_to_append, [0]), axis=0)
            
            tirages_tmp = np.append(tirages_tmp, [row_to_append], axis=0)
            
    return tirages_tmp