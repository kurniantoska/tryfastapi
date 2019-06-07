import uvicorn
from pydantic import BaseModel

from fastapi import FastAPI


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1", port=8000,
        reload=True, log_level="debug",
    )
