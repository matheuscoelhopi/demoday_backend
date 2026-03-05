from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI(title="Simulador de Investimentos API")

# Configuração de CORS para permitir chamadas do seu front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # Porta padrão do Next.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")