from fastapi import FastAPI
import uvicorn
from typing import List
from db.base import database, notes, NoteIn, Note, movies, Movies, MoviesIn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Тест на русские символы"}


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/notes/", response_model=List[Note])
async def read_notes():
    query = notes.select()
    return await database.fetch_all(query)


@app.post("/notes/", response_model=Note)
async def create_note(note: NoteIn):
    query = notes.insert().values(text=note.text, completed=note.completed)
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}


@app.post("/movies/", response_model=Movies)
async def create_movie(movie: MoviesIn):
    query = movies.insert().values(title=movie.title, description=movie.description)
    last_record_id = await database.execute(query)
    return {**movie.dict(), "id": last_record_id}


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True)
