from fastapi import FastAPI

app = FastAPI()

# File to test
@app.get("/")
def read_root():
    """
    Get endpoint for the root path.
    """
    return {"Hello": "World!"}
