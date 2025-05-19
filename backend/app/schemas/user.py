from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    email: EmailStr | None = None
    name: str | None = None
    password: str | None = None
