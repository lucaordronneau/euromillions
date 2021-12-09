from fastapi import APIRouter

import sys
import csv   
import pandas as pd
import numpy as np

sys.path.append('/../classes/Draw.py')
from classes.Draw import Draw

from src.model import getF1score, getPrecision, formatData, splitData, model, saveModel
from src.dataset import createDraws
from src.help_functions import  getCSV, getTestFile, loadModel
   
csv_path = getCSV()
test_path = getTestFile()

router = APIRouter()

@router.get('/model')
async def getInfos():

    # call the function "loadModel" in src/predict.py to load the prediction model located in src/data/model
    model = loadModel()

    with open(test_path, 'rb') as f:
        X_test = np.load(f)
        y_test = np.load(f)
        
    y_pred = model.predict(X_test)
    
    return {
        "F1 Score" : round(getF1score(y_test, y_pred)*100,2),
        "Accuracy Score" : round(getPrecision(y_test, y_pred)*100,2),
        "Model Name": type(model).__name__,
        "Parameters" : "A compléter"
    }

@router.put('/model')
async def addDraw(draw: Draw):
    
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        lines= len(list(reader))-1
    
    with open(csv_path, 'a+', newline='') as write_obj:
        writer = csv.writer(write_obj, delimiter=';')
        draw=[lines,draw.Date, draw.N1, draw.N2,draw.N3,draw.N4,draw.N5,draw.E1,draw.E2,draw.Gain]
        writer.writerow(draw)
        
@router.post('/model/retrain')
async def retrain():
    
    df = pd.read_csv(csv_path, sep=";")
    draws = df[["N1", "N2", "N3", "N4", "N5", "E1", "E2"]].to_numpy()
    draws = createDraws(draws)
    X, y = formatData(draws)
    X_train, X_test, y_train, y_test = splitData(X, y)
    clf = model(X_train, y_train)
    saveModel(clf)
    
    with open(test_path, 'wb') as f:
        np.save(f, np.array(X_test))
        np.save(f, np.array(y_test))
    