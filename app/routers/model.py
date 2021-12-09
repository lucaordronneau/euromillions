from fastapi import APIRouter, Body
import sys
import os
import inspect
import pandas as pd
sys.path.append('/../classes/Draw.py')
from classes.Draw import Draw, DrawPredict
from joblib import load
import numpy as np
from src.model import getF1score, getPrecision, formatData, splitData, model, saveModel
from src.dataset import createDraws
import csv      

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

@router.put('/model')
async def addDraw(draw: Draw):
    
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    path = parentdir + '/src/data/EuroMillions_numbers.csv'
    
    with open(path, 'r') as f:
        reader = csv.reader(f)
        lines= len(list(reader))-1
    
    with open(path, 'a+', newline='') as write_obj:
        writer = csv.writer(write_obj, delimiter=';')
        draw=[lines,draw.Date, draw.N1, draw.N2,draw.N3,draw.N4,draw.N5,draw.E1,draw.E2,draw.Gain]
        writer.writerow(draw)
        
@router.post('/model/retrain')
async def retrain():
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    csv_path = parentdir + '/src/data/EuroMillions_numbers.csv'
    
    df = pd.read_csv(csv_path, sep=";")
    draws = df[["N1", "N2", "N3", "N4", "N5", "E1", "E2"]].to_numpy()
    draws = createDraws(draws)
    X, y = formatData(draws)
    X_train, X_test, y_train, y_test = splitData(X, y)
    clf = model(X_train, y_train)
    saveModel(clf)
    
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    path = parentdir + '/src/data/test/test.npy'
    
    with open(path, 'wb') as f:
        np.save(f, np.array(X_test))
        np.save(f, np.array(y_test))
    