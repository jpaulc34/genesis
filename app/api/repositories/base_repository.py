from typing import TypeVar, Generic, List, Optional, Dict
from pymongo.collection import Collection
from bson import ObjectId
from fastapi import HTTPException, status

T = TypeVar('T')  # Generic type for the repository

class BaseRepository(Generic[T]):
    def __init__(self, collection: Collection):
        self.collection = collection

    async def find_all(self) -> List[Dict]:
        documents = self.collection.find()
        return [{"id": str(doc["_id"]), **doc} for doc in documents]

    async def find_by_id(self, id: str) -> Optional[Dict]:
        try:
            document = self.collection.find_one({"_id": ObjectId(id)})
            if not document:
                return None
            return {"id": str(document["_id"]), **document}
        except Exception:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ID format")

    async def insert_one(self, data: Dict) -> str:
        result = self.collection.insert_one(data)
        return str(result.inserted_id)
    
    async def update_one(self, id: str, data: Dict) -> Optional[Dict]:
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid product ID format")
        
        result = self.collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": data},
            return_document=True  # Ensures updated document is returned
        )
        
        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        
        result["id"] = str(result["_id"])  # Rename _id to id for JSON compatibility
        del result["_id"]                  # Remove the original _id key to avoid confusion
        return result


    async def delete_one(self, id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0