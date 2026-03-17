from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    with open("filesMachine/file.txt", "a") as file:
        file.write("\nHello world!")
        file.write("\nI edit this file, and still working")
        file.write("\n#########")
        file.write("\n@@@@@@@@@@")
    return {"msg":"Hello world!"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)