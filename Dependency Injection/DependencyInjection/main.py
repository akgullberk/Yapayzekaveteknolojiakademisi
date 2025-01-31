from fastapi import FastAPI,Depends
from typing import Annotated

app = FastAPI()

def hello_world():
    return "Hello World!"

HelloDependency = Annotated[str,Depends(hello_world)]

def get_hello_world(hello: HelloDependency):
    return f"Hello {hello}"

@app.get("/hello")
def hello(message: str = Depends(get_hello_world)):
    return {"message": message}