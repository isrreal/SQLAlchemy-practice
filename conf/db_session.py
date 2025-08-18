import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine

from pathlib import Path
from typing import Optional

from models.model_base import ModelBase

__engine: Optional[Engine] = None

#cria uma engine para o postgres ou para o SQLite
# Configuração de conexão do sqlalchemy com o banco de dados.
def create_engine(sqlite: bool = False):  
    global __engine

    if __engine:
        return
    if sqlite:
        arquivo_db = 'db/picoles.sqlite'
        folder = Path(arquivo_db).parent
        # Respeita a estrutura dita
        # Se exitir, não faz nada; caso não, o cria
        folder.mkdir(parents = True, exist_ok = True)

        conn_str = f"sqlite:///{arquivo_db}"

        __engine = sa.create_engine(url = conn_str,
                                    echo = False,
                                    connect_args = {"check_same_thread" : False}
                    )
    else:
        conn_str = "postgresql://postgres:senha@localhost:5432/picoles"
        __engine = sa.create_engine(url = conn_str, echo = False)

    return __engine

# Cria uma nova conexão com o banco de dados, uma nova thread
def create_session() -> Session:
    global __engine

    if not __engine:
        create_engine() # usando o postgres
    
    # engine 
    __session = sessionmaker(
        __engine,
        expire_on_commit = False,
        class_ = Session
    )

    return __session()

def create_tables() -> None:
    global __engine

    if not __engine:
        create_engine()
    
    import models.__all_models
    # Apaga e cria novas tabelas, respectivamente.
    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)