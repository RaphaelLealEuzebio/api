from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database_core import Base

class StatusOrcamento(Base):
    __tablename__ = 'status_orcamento'
    
    id:           Mapped[int] = mapped_column(primary_key=True)
    pendente:     Mapped[str] = mapped_column(String(20))
    aprovado:     Mapped[str] = mapped_column(String(20))
    reprovado:    Mapped[str] = mapped_column(String(20))
    expirado:     Mapped[str] = mapped_column(String(20))
    orcamento_id: Mapped[int] = mapped_column(ForeignKey('orcamento.id'))
    orcamento:    Mapped['Orcamento'] = relationship(back_populates='status',uselist=False)
    
class Orcamento(Base):
    __tablename__ = 'orcamento'

    id:                Mapped[int] = mapped_column(primary_key=True)
    valor:             Mapped[int] = mapped_column(Integer())
    valor_total_juros: Mapped[float] = mapped_column(Float())
    valor_parcela:     Mapped[float] = mapped_column(Float())
    valor_entrada:     Mapped[float] = mapped_column(Float())
    quantidade_parcela:Mapped[int] = mapped_column(Integer())
    taxa_juros:        Mapped[Float] = mapped_column(Float())
    data_criacao:      Mapped[datetime] = mapped_column(DateTime())
    data_validade:     Mapped[datetime] = mapped_column(DateTime())
    status:            Mapped['StatusOrcamento'] = relationship(back_populates='orcamento',uselist=False)
    usuario_id:        Mapped[int] = mapped_column(ForeignKey('usuarios.id'))