from fastapi import APIRouter
import uvicorn
from fastapi import FastAPI
import pickle
from routers import predict

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

# Route with a single parameter
@app.get('/{name}')
async def get_name(name: str):
    """[summary]

    Args:
        name (str): [description]

    Returns:
        [type]: [description]
    """
    return {'message': f'Hello, {name}'}

app.include_router(predict.router)
 
# Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)