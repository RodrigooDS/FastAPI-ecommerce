from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"root"}


@app.get("/hello/{name}")
async def say_hello(name: int):
    return {"hello": name}
