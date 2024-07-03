from fastapi import FastAPI

app = FastAPI()

@app.get("/get_item/{item_id}")
def get_item(item_id):
    return {"item_id": item_id}

@app.post("/post_item/{item_id}")
def post_item(item_id):
    return {"message": f"Saved the {item_id}"}