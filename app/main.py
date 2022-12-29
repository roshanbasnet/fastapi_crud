from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from . import models, config
from .database import engine
from .routers import post, user, auth, vote


models.Base.metadata.create_all(bind=engine)


# create a new instance of FastAPI
app = FastAPI()

origins = [
    "*"
    # "http://localhost",
    # "http://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routing
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Welcome to my API"}
