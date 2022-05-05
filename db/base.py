from databases import Database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean
from core.config import DATABASE_URL

from pydantic import BaseModel


database = Database(DATABASE_URL)
metadata = MetaData()


notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("text", String),
    Column("completed", Boolean),
)


movies = Table(
    "movies",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("description", String)
)


engine = create_engine(
    DATABASE_URL
)
metadata.create_all(engine)


class NoteIn(BaseModel):
    text: str
    completed: bool


class Note(BaseModel):
    id: int
    text: str
    completed: bool


class Movies(BaseModel):
    id: int
    title: str
    description: str


class MoviesIn(BaseModel):
    title: str
    description: str

