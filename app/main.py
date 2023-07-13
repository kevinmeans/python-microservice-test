from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """
    Get endpoint for the root path.
    """
    return {"Goodeye": "World"}
