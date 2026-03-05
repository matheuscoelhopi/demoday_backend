import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import router

load_dotenv()

app = FastAPI(title="Simulador de Investimentos API")

cors_origins = os.getenv("CORS", "http://localhost:3000").split(",")

# Configuração de CORS para permitir chamadas do seu front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    return {"status": "online", "uptime": "OK", "version": "1.0.0"}


app.include_router(router, prefix="/api")
