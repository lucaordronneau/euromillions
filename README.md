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
## Project Architecture
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