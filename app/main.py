from typing import Optional
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    # Doc String 1
    return {"Hellooo1": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, question: Optional[str] = None):
    # Doc String 1
    return {"item_id": item_id, "q": question}
