from fastapi import FastAPI
import os
import ast
import operator as op

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "User Management API is running"}

@app.get("/users")
def get_users():
    return [{"id": 1, "username": "admin"}, {"id": 2, "username": "dev_user"}]

@app.post("/login")
def login():
    return {"status": "Logged in", "token": "dummy-session-token"}