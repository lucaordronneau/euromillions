from fastapi import APIRouter


router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Luca Ordronneau"}, {"username": "Julian Ettarian"}]


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
