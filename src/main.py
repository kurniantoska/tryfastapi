import uvicorn

from fastapi import FastAPI


app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}
]


@app.get("/items/")
async def read_item(skip: int=0, limit: int=100):
    return fake_items_db[skip: skip + limit]

if __name__ == "__main__":
    uvicorn.run(
        app, host="127.0.0.1", port=8000,
        reload=True, log_level="debug",
    )
