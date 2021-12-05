from fastapi import APIRouter
import sys
sys.path.append('/../classes/Draw.py')
from classes.Draw import Draw

router = APIRouter()

@router.post('/predict')
async def predict_draw_probability(data:Draw):
    """[summary]

    Args:
        data (Draw): [description]

    Returns:
        [type]: [description]
    """
    data = data.dict()
    proba = 0.8
    return {
        'Proba gain': proba,
        'Proba perte': 1-proba
    }