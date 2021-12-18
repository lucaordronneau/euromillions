from typing import Any
import numpy as np

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

from sklearn.svm import SVC

from joblib import dump

from typing import Union

def formatData(tirages: np.array) -> Union[np.array, np.array]:
    """Allows formatting of data for training

    Args:
        tirages (np.array)

    Returns:
        Union[np.array, np.array]
    """
    X = []
    y = []
    
    for i in range(tirages.shape[0]):
        X.append((tirages[i][0:-1]).tolist())
        y.append(tirages[i][-1].tolist())

    X = np.array(X)
    y = np.array(y)
    
    return X, y

def splitData(X: np.array, y:  np.array) -> Union[np.array, np.array, np.array, np.array]:
    """Allows data to be separated into training and test data

    Args:
        X (np.array)
        y (np.array)

    Returns:
        Union[np.array, np.array, np.array, np.array]
    """
    X, y = shuffle(X, y, random_state=0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=13)
    
    return X_train, X_test, y_train, y_test

def model(X_train: np.array, y_train: np.array) -> SVC:
    """Allows the model to be trained with SVC

    Args:
        X_train (np.array)
        y_train (np.array)

    Returns:
        SVC: model
    """
    model = SVC(probability=True)
    model.fit(X_train, y_train)
    
    return model

def saveModel(model) -> None:
    """Allows the model to be separated 

    Args:
        model : model
    """
    dump(model, '/home/eisti/Documents/ING3-IA/Architecture Microservice/euromillions/app/src/data/model/model.jolib')
    

def getF1score(y_test: np.array, y_pred: np.array) -> float:
    """Returns the f1 score of the model 

    Args:
        y_test (np.array)
        y_pred (np.array)

    Returns:
        float: f1 score
    """
    return f1_score(y_test, y_pred)
    
def getPrecision(y_test: np.array, y_pred: np.array) -> float:
    """Returns the precision score of the model 

    Args:
        y_test (np.array)
        y_pred (np.array)

    Returns:
        float: precision
    """
    return accuracy_score(y_test, y_pred)