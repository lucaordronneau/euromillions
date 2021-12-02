from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

def predict(model, draw):
    """[summary]

    Args:
        model ([type]): [description]
        draw ([type]): [description]

    Returns:
        [type]: [description]
    """
    return model.predict_proba(draw)

def getF1score(y_test, y_pred):
    """[summary]

    Args:
        y_test ([type]): [description]
        y_pred ([type]): [description]

    Returns:
        [type]: [description]
    """
    return f1_score(y_test, y_pred)
    
def getPrecision(y_test, y_pred):
    """[summary]

    Args:
        y_test ([type]): [description]
        y_pred ([type]): [description]

    Returns:
        [type]: [description]
    """
    return accuracy_score(y_test, y_pred)
    
    
    