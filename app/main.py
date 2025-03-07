import asyncio
from time import sleep
from fastapi import FastAPI

app = FastAPI()

@app.get("/nonblocking")
async def nonblocking():
    print("Non-blocking request")
    await asyncio.sleep(5)
    return {"message": "Hello World"}

@app.get("/blocking")
async def blocking():
    print("Blocking request")
    sleep(5)
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)