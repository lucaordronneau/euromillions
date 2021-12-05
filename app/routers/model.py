from fastapi import APIRouter, Body
import sys
import os
import inspect
import math
sys.path.append('/../classes/Draw.py')
from classes.Draw import Draw, DrawPredict
from joblib import load
import numpy as np


router = APIRouter()