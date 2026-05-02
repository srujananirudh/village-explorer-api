from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
from pydantic import BaseModel
import uuid
import os

# ✅ CREATE APP

app = FastAPI(
title="Village API",
docs_url="/docs",
redoc_url="/redoc"
)

# ✅ CORS

app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

# ✅ ROOT

@app.get("/")
def home():
return {"message": "API running 🚀"}

# ✅ DATABASE (ENV VARIABLE)

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

# ✅ USER MODEL

class User(BaseModel):
email: str
password: str

# ✅ TEMP USERS STORAGE

users = {}

# ✅ API KEY GENERATION

def generate_api_key():
return "ak_live_" + uuid.uuid4().hex[:24]

# ✅ VERIFY API KEY

def verify_api_key(x_api_key: str = Header(None)):
for u in users.values():
if u["api_key"] == x_api_key:
return True
raise HTTPException(status_code=401, detail="Invalid API key")

# ✅ SIGNUP

@app.post("/signup")
def signup(user: User):
if user.email in users:
raise HTTPException(status_code=400, detail="User already exists")

```
key = generate_api_key()
users[user.email] = {"password": user.password, "api_key": key}

return {"message": "Account created successfully"}
```

# ✅ LOGIN

@app.post("/login")
def login(user: User):
if user.email not in users:
raise HTTPException(status_code=401, detail="User not found")

```
if users[user.email]["password"] != user.password:
    raise HTTPException(status_code=401, detail="Wrong password")

return {"api_key": users[user.email]["api_key"]}
```

# ✅ STATES

@app.get("/states")
def states(auth=Depends(verify_api_key)):
with engine.connect() as conn:
res = conn.execute(text('SELECT DISTINCT "STATE" FROM locations ORDER BY "STATE";'))
return {"states": [r[0] for r in res]}

# ✅ DISTRICTS

@app.get("/districts")
def districts(state: str, auth=Depends(verify_api_key)):
with engine.connect() as conn:
res = conn.execute(text(
'SELECT DISTINCT "DISTRICT" FROM locations WHERE "STATE" ILIKE :s'
), {"s": f"%{state}%"})
return {"districts": [r[0] for r in res]}

# ✅ MANDALS

@app.get("/mandals")
def mandals(state: str, district: str, auth=Depends(verify_api_key)):
with engine.connect() as conn:
res = conn.execute(text(
'SELECT DISTINCT "MANDAL" FROM locations WHERE "STATE" ILIKE :s AND "DISTRICT" ILIKE :d'
), {"s": f"%{state}%", "d": f"%{district}%"})
return {"mandals": [r[0] for r in res]}

# ✅ VILLAGES

@app.get("/villages")
def villages(state: str, district: str, mandal: str, auth=Depends(verify_api_key)):
with engine.connect() as conn:
res = conn.execute(text(
'SELECT DISTINCT "VILLAGE" FROM locations WHERE "STATE" ILIKE :s AND "DISTRICT" ILIKE :d AND "MANDAL" ILIKE :m'
), {"s": f"%{state}%", "d": f"%{district}%", "m": f"%{mandal}%"})
return {"villages": [r[0] for r in res]}
