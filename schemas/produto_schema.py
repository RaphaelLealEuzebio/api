from datetime import datetime

from pydantic import BaseModel, Field


class ProdutoRequest(BaseModel):
    nome:         str
    valor:        float = Field(gt=0)
    descricao:    str
    data_criacao: datetime
    
    
class ProdutoResponse(BaseModel):
    nome:         str
    valor:        float
    data_criacao: datetime
    