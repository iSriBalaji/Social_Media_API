from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World API - Python"}

@app.get("/login")
async def login():
    return {"message": "Login to the platform"}


@app.get("/newpage")
async def page():
    return {"message": "Powerful Backend is Python - So POWERFUL"}

@app.post("/content")
async def content():
    return {"content_post_million": "Made one million dollar with the API that I built"}
