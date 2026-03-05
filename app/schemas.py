from pydantic import BaseModel
from typing import List

class SimulationRequest(BaseModel):
    valorInicial: float
    aporteMensal: float
    taxaAnual: float
    periodo: int  # Anos

class DataPoint(BaseModel):
    mes: int
    valor: float
    investido: float

class SimulationResponse(BaseModel):
    data: List[DataPoint]