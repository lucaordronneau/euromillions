from fastapi import FastAPI
from routers import predict, model

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