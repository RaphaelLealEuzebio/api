from datetime import datetime
from enum     import Enum
from pydantic import BaseModel, Field

class StatusOrcamento(str, Enum):
    pendente  = 'pendente'
    aprovado  = 'aprovado'
    reprovado = 'reprovado'
    expirado  = 'expirado'

class OrcamentoRequest(BaseModel):
    usuario_id:        int = Field(gt=0)
    valor:             float = Field(gt=0)
    valor_total_juros: float = Field(ge=0)
    valor_parcela:     float = Field(gt=0)
    valor_entrada:     float = Field(ge=0)
    quantidade_parcela:int = Field(gt=0)
    taxa_juros:        float = Field(ge=0)
    data_criacao:      datetime
    data_validade:     datetime
    status:            StatusOrcamento
    

class OrcamentoResponse(BaseModel):
    usuario_id:        int = Field(gt=0)
    valor:             float = Field(gt=0)
    valor_total_juros: float = Field(ge=0)
    valor_parcela:     float = Field(gt=0)
    valor_entrada:     float = Field(ge=0)
    status:            StatusOrcamento
    