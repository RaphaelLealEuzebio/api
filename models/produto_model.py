from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, String, Text
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm.base import Mapped

from core.database_core import Base
from models.usuario_model import UsuarioModel

class ProdutoModel(Base):
    __tablename__ = 'produto'

    id:           Mapped[int] = mapped_column(primary_key=True)
    nome:         Mapped[str] = mapped_column(String(50))
    valor:        Mapped[float] = mapped_column(Float(50))
    descricao:    Mapped[str] = mapped_column(String(255))
    data_criacao: Mapped[datetime] = mapped_column(DateTime())
    usuario_id:   Mapped[int] = mapped_column(ForeignKey('usuarios.id'))