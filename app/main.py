from fastapi import FastAPI
from routers import predict, model

# Create the app object
app = FastAPI()

# Index route
@app.get('/')
async def index() -> dict:
    """[summary]

    Returns:
        dict: [description]
    """
    return {'message': 'Hello, stranger'}

# include route : predict
app.include_router(predict.router)
# include route : model
app.include_router(model.router)