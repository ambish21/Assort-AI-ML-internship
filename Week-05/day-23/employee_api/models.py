from pydantic import BaseModel, EmailStr, Field


class Employee(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=18, le=60)
    department: str
    salary: float = Field(gt=0)
    email: EmailStr