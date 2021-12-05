import pandas as pd
from src.dataset import createDraws
from src.model import formatData, splitData, model, saveModel

def run(csv: str):
    df = pd.read_csv(csv, sep=";")
    draws = df[["N1", "N2", "N3", "N4", "N5", "E1", "E2"]].to_numpy()
    draws = createDraws(draws)
    X, y = formatData(draws)
    X_train, X_test, y_train, y_test = splitData(X, y)
    clf = model(X_train, y_train)
    saveModel(clf)
    