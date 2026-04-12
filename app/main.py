from fastapi import FastAPI
import os

app = FastAPI()

AWS_SECRET_KEY = "AKIA1234567890ABCD12"

@app.get("/")
def read_root():
    return {"message": "User Management API is running"}

@app.get("/users")
def get_users():
    return [{"id": 1, "username": "admin"}, {"id": 2, "username": "dev_user"}]

@app.get("/calculate")
def insecure_calc(expression: str):
    return {"result":eval(expression)}

@app.post("/login")
def login():
    return {"status": "Logged in", "token": "dummy-session-token"}