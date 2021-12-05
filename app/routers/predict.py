from fastapi import APIRouter
import sys
sys.path.append('/../classes/Draw.py')
from classes.Draw import Draw
from joblib import load
import numpy as np
from src.dataset import oddEvenPatterns, lowHighPatterns

router = APIRouter()

@router.post('/predict')
async def predict_draw_probability(data:Draw):
    """[summary]

    Args:
        data (Draw): [description]

    Returns:
        [type]: [description]
    """
    print("enculé")

    model = load('../src/data/model.joblib')

    
    
    
    # draw = np.array([data.N1,data.N2,data.N3,data.N4,data.N5, data.E1, data.E2])
    # lowHighProba = oddEvenPatterns(draw)
    # oddEvenProba = lowHighPatterns(draw)
    # draw = np.concatenate((draw, [lowHighProba,oddEvenProba ]), axis=0)
    
    # proba = model.predict_probal(draw)
    proba = 0.1
    print(data.dict())

    return {
        'aaa' : 'a',
        'Proba gain': proba,
        'Proba perte': 1-proba
    }