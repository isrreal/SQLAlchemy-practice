import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DECIMAL, String, BigInteger, Integer
from datetime import datetime
from typing import List

from models.model_base import ModelBase
from models.revendedor import Revendedor
from models.lote import Lote

# ==============================================
# Tabela de associação Many-to-Many
# ==============================================

lotes_nota_fiscal = sa.Table(
    "lotes_nota_fiscal",
    ModelBase.metadata,
    sa.Column("id_nota_fiscal", Integer, sa.ForeignKey("notas_fiscais.id", ondelete="CASCADE")),
    sa.Column("id_lote", Integer, sa.ForeignKey("lotes.id", ondelete="CASCADE")),
)

# ==============================================
# Modelo NotaFiscal
# ==============================================

class NotaFiscal(ModelBase):
    __tablename__ = "notas_fiscais"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.now, index=True)

    valor: Mapped[float] = mapped_column(DECIMAL(8, 2), nullable=False)
    numero_serie: Mapped[str] = mapped_column(String(45), unique=True, nullable=False)
    descricao: Mapped[str] = mapped_column(String(200), nullable=False)

    id_revendedor: Mapped[int] = mapped_column(Integer, sa.ForeignKey("revendedores.id", ondelete="CASCADE"))
    revendedor: Mapped[Revendedor] = relationship("Revendedor", backref="notas_fiscais", lazy="joined")

    lotes: Mapped[List[Lote]] = relationship(
        "Lote",
        secondary=lotes_nota_fiscal,
        backref="notas_fiscais",
        lazy="selectin"
    )

    def __repr__(self) -> str:
        return (
            f"<NotaFiscal("
            f"id={self.id}, "
            f"numero_serie='{self.numero_serie}', "
            f"data_criacao='{self.data_criacao.strftime('%Y-%m-%d %H:%M:%S') if self.data_criacao else None}', "
            f"valor={float(self.valor):.2f}, "
            f"descricao='{self.descricao}', "
            f"revendedor='{self.revendedor.nome if self.revendedor else 'N/A'}'"
            f")>"
        )
