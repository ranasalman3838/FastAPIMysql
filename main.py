from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from typing import Optional, Annotated
import models

from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

class UserBase(BaseModel):
    email: str
    password: str

class PostBase(BaseModel):
    title: str
    content: str
    owner_id: int


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]




