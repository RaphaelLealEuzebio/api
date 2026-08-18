from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from core.database_core import Base

class EnderecoModel(Base):
    __tablename__ = 'endereco_usuario'
    
    id :        Mapped[int] = mapped_column(primary_key=True)
    rua:        Mapped[str] = mapped_column(String(30))
    n:          Mapped[int] = mapped_column(Integer())
    bairro:     Mapped[str] = mapped_column(String(50))
    estado:     Mapped[str] = mapped_column(String(10))
    pais:       Mapped[str] = mapped_column(String(10))

    usuario_id: Mapped[int] = mapped_column(ForeignKey('usuarios.id'))
    usuario:    Mapped['UsuarioModel'] = relationship(back_populates='endereco',uselist=False)

class UsuarioModel(Base):
    __tablename__ = 'usuarios'
    
    id:        Mapped[int] = mapped_column(primary_key=True)
    nome:      Mapped[str] = mapped_column(String(30))
    senha_hash:Mapped[str] = mapped_column(String(255))
    email:     Mapped[str] = mapped_column(String(255), unique=True, index=True)
    endereco:  Mapped['EnderecoModel'] = relationship(back_populates='usuario',uselist=False)