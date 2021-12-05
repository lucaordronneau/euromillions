import pandas as pd
from src.dataset import createDraws
from src.model import formatData, splitData, model, saveModel
import numpy as np

def run(csv: str):
    df = pd.read_csv(csv, sep=";")
    draws = df[["N1", "N2", "N3", "N4", "N5", "E1", "E2"]].to_numpy()
    draws = createDraws(draws)
    X, y = formatData(draws)
    X_train, X_test, y_train, y_test = splitData(X, y)
    clf = model(X_train, y_train)
    saveModel(clf)
    with open('test.npy', 'wb') as f:
        np.save(f, np.array(X_test))
        np.save(f, np.array(y_test))
        

# if __name__ == "__main__":
#     run("/home/eisti/Documents/ING3-IA/Architecture Microservice/euromillions/app/src/data/EuroMillions_numbers.csv")
    