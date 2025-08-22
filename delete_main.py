from typing import Optional
from conf.db_session import create_session
from models.revendedor import Revendedor
from models.picole import Picole

def deletar_picole(id_picole: int) -> None:
    with create_session() as session:
        picole: Picole = session.query(Picole).filter(Picole.id == id_picole).one_or_none()
        
        if picole:
            session.delete(picole)
            session.commit()
        else:
            print(f"O picolé com ID {id_picole} não foi encontrado.")

def deletar_revendedor(id_revendedor: int) -> None:
    with create_session() as session:
        revendedor: Optional[Revendedor] = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()
        
        if revendedor:
            session.delete(revendedor)
            session.commit()
        else:
            print(f"O picolé com ID {id_revendedor} não foi encontrado.")

if __name__ == "__main__":
    deletar_picole(2)
    deletar_revendedor(2)