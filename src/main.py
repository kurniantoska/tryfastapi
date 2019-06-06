import uvicorn

from fastapi import FastAPI


app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(
        item_id: str, needy: str, skip: int=0, limit: int=None
):
    item = {
        "item_id": item_id, "needy": needy,
        "skip": skip, "limit": limit
    }
    return item

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1", port=8000,
        reload=True, log_level="debug",
    )
