# Usa uma imagem oficial do Python otimizada (leve)
FROM python:3.11-slim

# Impede a criação de arquivos .pyc e força o log direto no console
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala as dependências separadamente para aproveitar o cache de camadas do Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação (a pasta app/)
COPY . .

# Expõe a porta padrão do FastAPI
EXPOSE 8000

# Executa o servidor Uvicorn apontando para a instância 'app' dentro de 'app/main.py'
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]