from fastapi import FastAPI
import os
import ast
import operator as op

app = FastAPI()

AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", "")

operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
}

def safe_eval(expr):
    def eval_(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return operators[type(node.op)](eval_(node.left), eval_(node.right))
        else:
            raise Exception("Unsafe expression")

    return eval_(ast.parse(expr, mode='eval').body)

@app.get("/")
def read_root():
    return {"message": "User Management API is running"}

@app.get("/users")
def get_users():
    return [{"id": 1, "username": "admin"}, {"id": 2, "username": "dev_user"}]

@app.get("/calculate")
def secure_calc(expression: str):
    return {"result": safe_eval(expression)}

@app.post("/login")
def login():
    return {"status": "Logged in", "token": "dummy-session-token"}