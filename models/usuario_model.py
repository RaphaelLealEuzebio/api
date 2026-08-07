from sqlalchemy import String,
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from core.database_core import Base

class EnderecoModel(Base):
    rua: Mapped[str] = mapped_column(String(30))
    n:  Mapped[int] = mapped_column(Integer())
    bairro:
    estado:
    pais:

class UsuarioModel(Base):
    __tablename__ = 'user_account'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30))
    endereco: EnderecoModel
    produto:
    orcamento:
    