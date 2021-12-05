from fastapi import APIRouter, Body
import sys
import os
import inspect
import math
sys.path.append('/../classes/Draw.py')
from classes.Draw import Draw, DrawPredict
from joblib import load
import numpy as np
from src.model import getF1score, getPrecision


router = APIRouter()

@router.get('/model')
async def getInfos():
    
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    model = load(parentdir + '/src/data/model/model.jolib')

    with open(parentdir + '/src/data/test/test.npy', 'rb') as f:
        X_test = np.load(f)
        y_test = np.load(f)
        
    y_pred = model.predict(X_test)
    
    return {
        "F1 Score" : round(getF1score(y_test, y_pred)*100,2),
        "Accuracy Score" : round(getPrecision(y_test, y_pred)*100,2),
        "Model Name": type(model).__name__,
        "Parameters" : "A compléter"
    }