### Short Notes — Day 23

Pydantic is used for data validation and type checking in FastAPI.
BaseModel is used to create structured data models.
Type hints like str, int, and float define expected data types.
Field() adds extra validation rules such as minimum age or positive salary.
FastAPI automatically validates request data using Pydantic.
Invalid data returns a 422 Validation Error.
EmailStr validates email format.
Swagger UI (/docs) can be used to test API endpoints.