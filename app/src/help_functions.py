import os
import inspect
from typing import Any
from joblib import load

def getParentDir() -> str:
    """Get the parent dir of the current dir

    Returns:
        str: the path of the parent dir
    """
    # get the current directory dir
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    # get parent dir to get model
    parentdir = os.path.dirname(currentdir)
    return parentdir
    
def getCSV() -> str:
    """Get the csv path

    Returns:
        str: the path of the CSV file
    """
    parentdir = getParentDir()
    return parentdir + '/src/data/EuroMillions_numbers.csv'

def getTestFile() -> str:
    """Get the test file

    Returns:
        str: the path of the test file
    """
    parentdir = getParentDir()
    return parentdir + '/src/data/test/test.npy'

# this function get the path where the model is saved and load it
def loadModel() -> Any:
    """
    This function get the path where the model is saved and load it

    Args:
        No args are needed

    Returns:
        load the model
    """ 
    # get parent dir
    parentdir = getParentDir()
    
    # call the function load with the path to load the prediction model
    return load(parentdir + '/src/data/model/model.jolib')