import numpy as np

def oddEvenPatterns(t: np.array):
    """[summary]

    Args:
        t (np.array): [description]

    Returns:
        [type]: [description]
    """
    nb = sum(1-n%2 for n in t)
    if ((nb==1) or (nb==4)):
        result = 0.1492618323925310
    elif ((nb == 3) or (nb==2)):
        result = 0.3256621797655230
    else:
        result = 0.0250759878419453
    return result

def lowHighPatterns(t: np.array):
    """[summary]

    Args:
        t (np.array): [description]

    Returns:
        [type]: [description]
    """
    nb = sum(n<26 for n in t)
    if ((nb==1) or (nb==4)):
        result = 0.1492618323925310
    elif ((nb == 3) or (nb==2)):
        result = 0.3256621797655230
    else:
        result = 0.0250759878419453
    return result

def createDraws(tirages: np.array, n=4):
    """[summary]

    Args:
        tirages (np.array): [description]
        n (int, optional): [description]. Defaults to 4.

    Returns:
        [type]: [description]
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
            numeros_generation = np.random.choice(np.arange(1, 51), replace=False, size=(5,))
            while (np.sort(array_numeros) == np.sort(numeros_generation)).all():
                numeros_generation = np.random.choice(np.arange(1, 51), replace=False, size=(5,))
            
            etoiles_generation = np.random.choice(np.arange(1, 13), replace=False, size=(2,))
            while (np.sort(array_etoiles) == np.sort(etoiles_generation)).all():
                etoiles_generation = np.random.choice(np.arange(1, 13), replace=False, size=(2,))
                
            row_to_append = np.concatenate((numeros_generation, etoiles_generation), axis=0)
            row_to_append = np.concatenate((row_to_append, [oddEvenPatterns(numeros_generation)]), axis=0)
            row_to_append = np.concatenate((row_to_append, [lowHighPatterns(numeros_generation)]), axis=0)
            row_to_append = np.concatenate((row_to_append, [0]), axis=0)
            
            tirages_tmp = np.append(tirages_tmp, [row_to_append], axis=0)
            
    return tirages_tmp