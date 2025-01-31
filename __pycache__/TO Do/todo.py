from fastapi import FastAPI
from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select


class ToDo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    task: str = Field(index=True)




app = FastAPI()


@app.get("/")
def home():
    return{"New": "Page"}