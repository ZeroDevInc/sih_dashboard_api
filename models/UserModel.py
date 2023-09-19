from pydantic import BaseModel
# User model
class User(BaseModel):
    username: str
    email: str
    vehicles: list
