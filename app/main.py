from fastapi import APIRouter
import uvicorn
from fastapi import FastAPI
import pickle
from routers import predict, model
from src.run import run

# Create the app object
app = FastAPI()

# Index route
@app.get('/')
async def index():
    """[summary]

    Returns:
        [type]: [description]
    """
    return {'message': 'Hello, stranger'}

app.include_router(predict.router)

app.include_router(model.router)