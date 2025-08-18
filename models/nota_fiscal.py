import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DECIMAL, String, BigInteger, Integer
from datetime import datetime
from typing import List, Optional

from models.model_base import ModelBase
from models.revendedor import Revendedor
from models.lote import Lote

# ==============================================
# Tabela de associação Many-to-Many
# ==============================================

lotes_nota_fiscal = sa.Table(
    'lotes_nota_fiscal', 
    ModelBase.metadata,
    sa.Column('id_nota_fiscal', Integer, sa.ForeignKey('notas_fiscais.id')),
    sa.Column('id_lote', Integer, sa.ForeignKey('lotes.id'))
)

# ==============================================
# Modelo NotaFiscal
# ==============================================

class NotaFiscal(ModelBase):
    __tablename__ = 'notas_fiscais'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.now, index=True)

    valor: Mapped[float] = mapped_column(DECIMAL(8, 2), nullable=False)
    numero_serie: Mapped[str] = mapped_column(String(45), unique=True, nullable=False)

    id_revendedor: Mapped[int] = mapped_column(Integer, sa.ForeignKey('revendedores.id'))
    revendedor: Mapped[Revendedor] = relationship('Revendedor', lazy='joined')

    lotes: Mapped[List[Lote]] = relationship(
        'Lote',
        secondary=lotes_nota_fiscal,
        backref='notas_fiscais',
        lazy='dynamic'
    )

    def __repr__(self) -> str:
        return (
            f"<NotaFiscal ID={self.id}, Série={self.numero_serie}, "
            f"Revendedor={self.revendedor.nome if self.revendedor else 'N/A'}, "
            f"Valor={self.valor}>"
        )
