from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "world"}

@app.get("/say/{hello}")
def read_item(hello: str):
    return {"hello": hello}

