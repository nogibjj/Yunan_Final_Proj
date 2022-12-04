from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    
    return "Hello World"

@app.post("/topfive")
async def topfive():
    """Print the top five ranking stackoverflow posts"""

    result = topFivePosts()
    print(result)
    # return {result.to_json(orient='table')}
    return result.to_string()

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")