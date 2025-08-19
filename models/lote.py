import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from models.model_base import ModelBase
from models.tipo_picole import TipoPicole

class Lote(ModelBase):
    __tablename__ = 'lotes'

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.now, index=True)

    id_tipo_picole: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('tipos_picole.id'))
    tipo_picole: Mapped[TipoPicole] = relationship('TipoPicole', lazy='joined')

    quantidade: int = sa.Column(sa.Integer, nullable = False)

    def __repr__(self) -> str:
        return (
            f"<Lote ID: {self.id}, Tipo: {self.tipo_picole.nome if self.tipo_picole else 'N/A'}, "
            f"Data: {self.data_criacao},"
            f"Quantidade: {self.quantidade}"
        )
