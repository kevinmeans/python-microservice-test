from fastapi import FastAPI

app1 = FastAPI()


@app1.get("/")
def read_root():
    """
    Get endpoint for the root path.
    """
    return {"Goodeye": "World"}
