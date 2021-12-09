from typing import Any
import numpy as np

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

from sklearn.svm import SVC

from joblib import dump

def formatData(tirages):
    """[summary]

    Args:
        tirages ([type]): [description]

    Returns:
        [type]: [description]
    """
    X = []
    y = []
    
    for i in range(tirages.shape[0]):
        X.append((tirages[i][0:-1]).tolist())
        y.append(tirages[i][-1].tolist())

    X = np.array(X)
    y = np.array(y)
    
    return X, y

def splitData(X, y):
    """[summary]

    Args:
        X ([type]): [description]
        y ([type]): [description]

    Returns:
        [type]: [description]
    """
    X, y = shuffle(X, y, random_state=0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=13)
    
    return X_train, X_test, y_train, y_test

def model(X_train, y_train) -> SVC:
    """[summary]

    Args:
        X_train ([type]): [description]
        y_train ([type]): [description]

    Returns:
        SVC: [description]
    """
    model = SVC(probability=True)
    model.fit(X_train, y_train)
    
    return model

def saveModel(model) -> None:
    dump(model, '/home/eisti/Documents/ING3-IA/Architecture Microservice/euromillions/app/src/data/model/model.jolib')
    

def getF1score(y_test, y_pred) -> float:
    """[summary]

    Args:
        y_test ([type]): [description]
        y_pred ([type]): [description]

    Returns:
        float: [description]
    """
    return f1_score(y_test, y_pred)
    
def getPrecision(y_test, y_pred) -> float:
    """[summary]

    Args:
        y_test ([type]): [description]
        y_pred ([type]): [description]

    Returns:
        float: [description]
    """
    return accuracy_score(y_test, y_pred)