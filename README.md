# EUROMILLIONS
## By Ordronneau Luca and Ettarian Julian
![alt text](images/logo_euromillion.png)
## Description

Creation of a FastAPI application for the euromillions which predicts whether a sequence of 5 numbers and 2 star numbers is winning.
## Launch the app
```
create your virtualenv
cd euromillions/
pip install -r requirements.txt
cd app/
uvicorn main:app --reload
```

## Model construction
### Dataset
To build our model, we took the data from the csv file `EuroMillions_numbers.csv` and augmented this dataset by adding 4 losing draws for each winning draw (80-20). Then, we did some feature engineering by adding two additional probabilities to each draw.

Indeed, a probability of **even and odd** numbers: 
- *Example: there is less chance of having only even numbers in the draw (~0.02) than 2 odd numbers and 3 even numbers (~0.32).*

In the same way, we added the probability of **low and high** :
- *Example: there is less chance of having only numbers below 25 (~0.02) than two numbers below 25 and three above 25 (~0.32).* 
### Model
For the prediction we used the scikit learn module SVC.
## Project Architecture
### Description and technical choices

We have chosen to separate the different routes (/routers), classes (/classes) and model construction files (/src) for better readability. You can see the architecture of the project below
```
euromillions
│   README.md
└─── app
│    │   main.py
│    └─── classes
│    │   │   Draw.py
│    │ 
│    └─── routers
│    │   │   model.py
│    │   │   predict.py
│    │ 
│    └─── src
│    │   │   dataset.py
│    │   │   hel_functions.py
│    │   │   model.py
│    │   │   predict.py
│    │   │
│    │   └─── data
│    │   │   │   EuroMillions_numbers.csv
│    │   │   │   model/model.joblib
│    │   │   │   test/test.npy
│    │   │
└─── notebooks 
│    │  data-exploration-julian.ipynb
│    │  data-exploration-julian.ipynb
│
└─── images
│    │  logo_euromillion.png
│
│   TP MoneyMoneyMoney.pdf
```

`app` : FastAPI app
- `main.py` : file to be launch
- `classes` :
    - `Draw.py` : Class of a draw, representation of a draw for CSV and prediction
- `routers` : routers to interact with the predictive model and separate the code
- `src` : Code to prepare the dataset, the model ans put the data files

`notebooks` : Notebooks to explore the data before python script