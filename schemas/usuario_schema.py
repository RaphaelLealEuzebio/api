from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

class EnderecoSchema(BaseModel):
    rua:    str
    n:      int
    bairro: str
    estado: str
    pais:   str

class UsuarioRequest(BaseModel):
    nome:      str
    email:     EmailStr
    endereco : EnderecoSchema
    produto:   str

class UsuarioResponse(BaseModel):
    nome:     str
    email:    EmailStr
    produto:  str
    createat: datetime
    

    