import uvicorn
from pydantic import BaseModel

from fastapi import FastAPI


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


app = FastAPI()


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1", port=8000,
        reload=True, log_level="debug",
    )
