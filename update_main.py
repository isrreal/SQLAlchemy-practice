from conf.db_session import create_session
from models.sabor import Sabor 
from models.picole import Picole

def atualizar_sabor(id_sabor: int, novo_nome: str) -> None:
    with create_session() as session:
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()

        if sabor:
            sabor.nome = novo_nome
            session.commit()
            print(f"Sabor ID {id_sabor} atualizado para '{novo_nome}'")
        else:
            print(f"Não existe sabor com ID {id_sabor}")

def atualizar_picole(id_picole: int, novo_preco: float) -> None:
    with create_session() as session:
        picole: Picole = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

        if picole:
            picole.preco = novo_preco 
            session.commit()
            print(f"Picolé ID {id_picole} atualizado para preço R$ {novo_preco:.2f}")
        else:
            print(f"Não existe picolé com ID {id_picole}")

if __name__ == "__main__":
    id_sabor = 42
    id_picole = 15  

    atualizar_sabor(id_sabor, "Cachaça")
    atualizar_picole(id_picole, 9.99)
