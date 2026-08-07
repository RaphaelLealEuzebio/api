from pydantic import BaseModel, Field


class ProdutoRequest(BaseModel):
    nome: str
    valor: float = Field(gt=0)
    descricao: str
    
class ProdutoResponse(BaseModel):
    nome: str
    valor: float