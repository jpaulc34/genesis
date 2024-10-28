from fastapi import Request
from typing import List, Optional, Dict

from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserResponse

class UserService:
    def __init__(self, request: Request):
        # Inject the UserRepository, which uses the MongoDB collection from the app state
        self.user_repository = UserRepository(request)

    async def create_user(self, user_data: UserCreate) -> str:
        return await self.user_repository.create_user(user_data.model_dump())

    async def get_all_users(self) -> List[UserResponse]:
        return await self.user_repository.get_all_users()

    async def get_user_by_id(self, user_id: str) -> Optional[UserResponse]:
        return await self.user_repository.get_user_by_id(user_id)
    
    async def update_user(self, user_id: str, update_data: Dict) -> UserResponse:
        return await self.user_repository.update_user(user_id, update_data)
    
    async def delete_user(self, user_id: str):
        return await self.user_repository.delete_user(user_id)