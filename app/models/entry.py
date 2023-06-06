from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class EntryModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    description: str = Field(...)
    faction: Optional[str] = Field(...)

    class Config:
        allow_population_by_field_name = True,
        arbitrary_types_allowed = True,
        json_encoders = { ObjectId: str }
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "description": "Just some random murder victim",
                "faction": "Students for Communism"
            }
        }

class UpdateEntryModel(BaseModel):
    name: Optional[str]
    description: Optional[str]
    faction: Optional[str]

    class Config:
        allow_population_by_field_name = True,
        arbitrary_types_allowed = True,
        json_encoders = { ObjectId: str }
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "description": "Just some random murder victim",
                "faction": "Students for Communism"
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}