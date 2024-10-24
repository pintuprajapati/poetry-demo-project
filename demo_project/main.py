from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    print("Hello")
    return {"res": "res"}