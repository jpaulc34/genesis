from fastapi import APIRouter, Request, Depends
from typing import List, Dict

from app.schemas.user_schema import UserResponse, UserCreate
from app.services.user_service import UserService

router = APIRouter(
        prefix="/users",
        tags= ["Users"],
        # dependencies= [Depends(validate_token)]
    )

def get_user_service(request: Request) -> UserService:
    return UserService(request)

@router.get("/")
async def list_users(service: UserService = Depends(get_user_service)) -> List[UserResponse]:
    return await service.get_all_users()

@router.post("/")
async def create_user(user_data: UserCreate, service: UserService = Depends(get_user_service)):
    return await service.create_user(user_data)

@router.get("/{id}")
async def get_user( user_id: str, service: UserService = Depends(get_user_service)) -> UserResponse:
    return await service.get_user_by_id(user_id)

@router.put("/{user_id}")
async def update_user( user_id: str, user_data: Dict, service: UserService = Depends(get_user_service)) -> UserResponse:
    return await service.update_user(user_id, user_data)

@router.delete("/{user_id}")
async def delete_user(user_id: str, service: UserService = Depends(get_user_service)):
    return await service.delete_user(user_id)