from fastapi import APIRouter, Query
from schemas.users import registration
from services.users import auth_obj

router = APIRouter(tags=["User"])

@router.post('/registration')
def Registration(data: registration):
    return auth_obj.Registration(data)

@router.put('/avtorization')
def Avtorization(mail: str = Query(max_length=50), password: str = Query(max_length=50)):
    return auth_obj.Avtorization(mail, password)