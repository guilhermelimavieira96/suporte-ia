from pydantic import BaseModel, EmailStr

class Ticket(BaseModel):
    name: str
    email: EmailStr
    description: str
    category: str
    attempts: int
    summary: str
    priority: str
