import uvicorn

from fastapi import FastAPI


app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str=None, short: bool=False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "decription": "This is an amazing item "
                              "that has a long description "
            }
        )
    return item

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1", port=8000,
        reload=True, log_level="debug",
    )
