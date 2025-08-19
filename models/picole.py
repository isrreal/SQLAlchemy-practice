import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import List, Optional

from models.model_base import ModelBase
from models.tipo_picole import TipoPicole
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.aditivo_nutritivo import AditivoNutritivo

# ==============================================
# Tabelas de associação Many-to-Many
# ==============================================

ingredientes_picole = sa.Table(
    'ingredientes_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id')),
    sa.Column('id_ingrediente', sa.Integer, sa.ForeignKey('ingredientes.id'))
)

conservantes_picole = sa.Table(
    'conservantes_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id')),
    sa.Column('id_conservante', sa.Integer, sa.ForeignKey('conservantes.id'))
)

aditivos_nutritivos_picole = sa.Table(
    'aditivos_nutritivos_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id')),
    sa.Column('id_aditivo_nutritivo', sa.Integer, sa.ForeignKey('aditivos_nutritivos.id'))
)

# ==============================================
# Modelo Picole
# ==============================================

class Picole(ModelBase):
    __tablename__ = 'picoles'

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.now, index=True)

    preco: float = sa.Column(sa.DECIMAL(8,2), nullable=False)

    id_sabor: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('sabores.id'))
    sabor: Mapped[Sabor] = relationship('Sabor', lazy='joined')

    id_tipo_embalagem: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('tipos_embalagem.id'))
    tipo_embalagem: Mapped[TipoEmbalagem] = relationship('TipoEmbalagem', lazy='joined')

    id_tipo_picole: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('tipos_picole.id'))
    tipo_picole: Mapped[TipoPicole] = relationship('TipoPicole', lazy='joined')

    ingredientes: Mapped[List[Ingrediente]] = relationship(
        'Ingrediente',
        secondary=ingredientes_picole,
        backref='picoles',
        lazy='joined'
    )

    conservantes: Mapped[Optional[List[Conservante]]] = relationship(
        'Conservante',
        secondary=conservantes_picole,
        backref='picoles',
        lazy='dynamic'
    )

    aditivos_nutritivos: Mapped[Optional[List[AditivoNutritivo]]] = relationship(
        'AditivoNutritivo',
        secondary=aditivos_nutritivos_picole,
        backref='picoles',
        lazy='dynamic'
    )

    def __repr__(self) -> str:
        return (
            f"<Picole: {self.tipo_picole.nome} "
            f"com sabor {self.sabor.nome} "
            f"e embalagem {self.tipo_embalagem.nome}>"
        )
