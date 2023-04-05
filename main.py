from fastapi import FastAPI
from db.db_setup import engine,Base
from db.models import user,course
import uvicorn

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI()

uvicorn.run(app)