# app/main.py
from fastapi import FastAPI, Request
from routes.user import user_router
from database.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
import subprocess

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React 포트
    allow_methods=["*"],
    allow_headers=["*"],
)

# 데이터베이스 초기화
Base.metadata.create_all(bind=engine)

# 라우트 등록
app.include_router(user_router, prefix="/api/users", tags=["Users"])
# React 앱 빌드
@app.get("/")
def root():
    return {"message": "FastAPI backend is running."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
