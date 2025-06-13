from fastapi import FastAPI, Path, Query

from api import users, courses, sections
from db.db_setup import engine
from db.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Abhilash",
        "email": "abhilashchutia1999@gmail.com"
    },
    license_info={
        "name": "MIT"
    }
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)

@app.get("/")
async def read_root():
    return {"message":"Hello World"}

