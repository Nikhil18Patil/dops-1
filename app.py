from fastapi import FastAPI
import uvicorn



app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get('/hello')
def read_hello():
    return {"message": "Nikhil Patil"}


@app.get('/api')
def read_api():
    return {"message": "api is working"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)