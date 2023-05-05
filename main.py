from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Order matters if we're going to have multiple paths with the same path operation (beginning of the path)
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

