from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel , EmailStr

class UserChecker(BaseModel):
    id:int
    email:EmailStr
    is_active:bool

app = FastAPI()
@app.get("/")
def home():
    return "sjfd"

@app.get("/user/{user_id}")
def user(user_id:int):
    return user_id

@app.post("/users")
def create_user(user:UserChecker):
    return user

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000,reload=True)