from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
from pydantic import BaseModel
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "postgresql://postgres:Srujananirudh8@localhost:5432/India_location"
engine = create_engine(DATABASE_URL)

class User(BaseModel):
    email: str
    password: str

users = {}

def generate_api_key():
    return "ak_live_" + uuid.uuid4().hex[:24]

def verify_api_key(x_api_key: str = Header(None)):
    for u in users.values():
        if u["api_key"] == x_api_key:
            return True
    raise HTTPException(status_code=401, detail="Invalid API key")

@app.post("/signup")
def signup(user: User):
    if user.email in users:
        raise HTTPException(status_code=400, detail="User exists")

    key = generate_api_key()
    users[user.email] = {"password": user.password, "api_key": key}

    return {"message": "Account created"}

@app.post("/login")
def login(user: User):
    if user.email not in users:
        raise HTTPException(status_code=401, detail="User not found")

    if users[user.email]["password"] != user.password:
        raise HTTPException(status_code=401, detail="Wrong password")

    return {"api_key": users[user.email]["api_key"]}

@app.get("/states")
def states(auth=Depends(verify_api_key)):
    with engine.connect() as conn:
        res = conn.execute(text('SELECT DISTINCT "STATE" FROM locations ORDER BY "STATE";'))
        return {"states": [r[0] for r in res]}

@app.get("/districts")
def districts(state: str, auth=Depends(verify_api_key)):
    with engine.connect() as conn:
        res = conn.execute(text(
            'SELECT DISTINCT "DISTRICT" FROM locations WHERE "STATE" ILIKE :s'
        ), {"s": f"%{state}%"})
        return {"districts": [r[0] for r in res]}

@app.get("/mandals")
def mandals(state: str, district: str, auth=Depends(verify_api_key)):
    with engine.connect() as conn:
        res = conn.execute(text(
            'SELECT DISTINCT "MANDAL" FROM locations WHERE "STATE" ILIKE :s AND "DISTRICT" ILIKE :d'
        ), {"s": f"%{state}%", "d": f"%{district}%"})
        return {"mandals": [r[0] for r in res]}

@app.get("/villages")
def villages(state: str, district: str, mandal: str, auth=Depends(verify_api_key)):
    with engine.connect() as conn:
        res = conn.execute(text(
            'SELECT DISTINCT "VILLAGE" FROM locations WHERE "STATE" ILIKE :s AND "DISTRICT" ILIKE :d AND "MANDAL" ILIKE :m'
        ), {"s": f"%{state}%", "d": f"%{district}%", "m": f"%{mandal}%"})
        return {"villages": [r[0] for r in res]}