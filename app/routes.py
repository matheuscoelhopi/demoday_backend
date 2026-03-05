from fastapi import APIRouter
from app.schemas import SimulationRequest, SimulationResponse
from app.services import calcular_simulacao

router = APIRouter()

@router.post("/simular", response_model=SimulationResponse)
async def post_simular(request: SimulationRequest):
    resultado = calcular_simulacao(
        request.valorInicial,
        request.aporteMensal,
        request.taxaAnual,
        request.periodo
    )
    return {"data": resultado}