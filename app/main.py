from fastapi import FastAPI

app = FastAPI()
# Adding comment
@app.get("/")
def read_root():
    """
    Get endpoint for the root path.
    """
    return {"XXXXX": "World!"}
