from fastapi import FastAPI
from app.api.auth.routes import router as auth_router

app = FastAPI(title="Todo Shared App API", version="1.0.0")

# ルーターを登録
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo Shared App API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
