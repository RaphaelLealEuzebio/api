from datetime import datetime

from pydantic import BaseModel, EmailStr

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
    senha: str

class UsuarioResponse(BaseModel):
    nome:     str
    email:    EmailStr
    createat: datetime

class LoginRequest(BaseModel):
    email: EmailStr
    senha: str

class TokenResponse(BaseModel):
    acess_token: str
    token_type: str = 'bearer'

    

    