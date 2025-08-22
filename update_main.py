from conf.db_session import create_session

from models.sabor import Sabor 
from models.picole import Picole


def atualizar_sabor(id_sabor: int, novo_nome: str) -> None:
    with create_session() as session:
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()

        if sabor:
            sabor.nome = novo_nome
            session.commit()

        else:
            print(f"Não existe sabor com ID {id_sabor}")

def atualizar_picole(id_picole: int, novo_preco: float) -> None:
    with create_session() as session:
        picole: Picole = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

        if picole:
            picole.preco = novo_preco 
            session.commit()
        else:
            print(f"Não existe picolé com ID {id_picole}")

if __name__ == "__main__":
    from select_main import select_filtro_sabor

    id_sabor = 42
    #tipo_sabor = select_filtro_sabor(id_sabor = id_sabor)

    atualizar_sabor(id_sabor, "Cachaça")

