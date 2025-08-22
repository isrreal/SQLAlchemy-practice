from typing import List

from sqlalchemy import func
from conf.db_session import create_session

# Select Simples
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.revendedor import Revendedor

# Select Compostos / Complexos
from models.picole import Picole

def select_todos_aditivos_nutritivos() -> None:
    with create_session() as session:
        # Forma 1: avaliação preguiçosa 
        # aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo)

        # Forma 2: retorna todos de um vez
        aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo).all()
        
        for an in aditivos_nutritivos:
           print(f"\nID: {an.id}") 
           print(f"Data: {an.data_criacao}") 
           print(f"Nome: {an.nome}") 
           print(f"Fórmula Química: {an.formula_quimica}") 

def select_filtro_sabor(id_sabor: int) -> None:
    with create_session() as session:
        # Forma 1:  retorna o objeto requerido ou null
        #sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).first()

        # Forma 2: Gera uma excessão exec.NoResultFound caso não encontre
        #sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one()

        # Forma 3:
        #sabor: Sabor = session.query(Sabor).where(Sabor.id == id_sabor)

        # Forma 4: Recomendado, retorna o objeto requerido, caso não exista, retorna null.
        # Lança uma excessão MultipleResultsFound caso haja valores replicado caso haja valores replicados. 
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()

        print(f"\nID: {sabor.id}") 
        print(f"Data: {sabor.data_criacao}") 
        print(f"Nome: {sabor.nome}") 

def select_complexo_picole() -> None:
    with create_session() as session:
        picoles: List[Picole] = session.query(Picole).all()

        for picole in picoles:
            print(f"\nID: {picole.id}") 
            print(f"Data: {picole.data_criacao}") 
            print(f"Preço: {picole.preco}") 

            print(f"ID Sabor: {picole.id_sabor}") 
            print(f"Sabor: {picole.sabor}") 

            print(f"ID Embalagem: {picole.id_tipo_embalagem}") 
            print(f"Embalagem: {picole.tipo_embalagem}") 

            print(f"ID Tipo Picole: {picole.id_tipo_picole}") 
            print(f"Tipo Picole: {picole.tipo_picole}") 

            print(f"Ingredientes: {picole.ingredientes}") 
            print(f"Aditivos Nutritivos: {picole.aditivos_nutritivos}") 
            print(f"Conservantes: {picole.conservantes}") 

def select_order_by_sabor() -> None:
    with create_session() as session:
        sabores: List[Sabor] = session.query(Sabor).order_by(Sabor.data_criacao.desc()).all()

        for sabor in sabores:
            print(f"ID:  {sabor.id}")
            print(f"Nome:  {sabor.nome}")


def select_group_by_picole() -> None:
    with create_session() as session:
        picoles: List[Picole] = session.query(Picole).group_by(Picole.id, Picole.id_tipo_picole).all()

        for picole in picoles:
            print(f"\nID: {picole.id}") 
            print(f"Data: {picole.data_criacao}") 
            print(f"Tipo Picole: {picole.tipo_picole}") 
            print(f"Preço: {picole.preco}") 

def select_limit() -> None:
    with create_session() as session:
        sabores: List[Sabor] = session.query(Sabor).limit(5)

        for sabor in sabores:
            print(f"\nID: {sabor.id}") 
            print(f"Nome: {sabor.nome}") 
def select_count_revendedores() -> None:
    with create_session() as session:
        qtd: int = session.query(Revendedor).count()

        print(f"Quantidade de revendedores: {qtd}")

def select_agregacao() -> None:
    with create_session() as session:
        resultado: List = session.query(
            func.sum(Picole.preco).label('soma'),
            func.avg(Picole.preco).label('media'),
            func.min(Picole.preco).label('mais_barato'),
            func.max(Picole.preco).label('mais_caro')
        ).all()

        print(f"A soma dos preços dos picolés é: {resultado[0][0]}")
        print(f"A média dos preços dos picolés é: {resultado[0][1]:.3f}")
        print(f"O picolé mais barato é: {resultado[0][2]}")
        print(f"O picolé mais caro é: {resultado[0][3]}")

if __name__ == "__main__":
    select_todos_aditivos_nutritivos()
    select_complexo_picole()
    select_order_by_sabor()
    select_limit()
    select_count_revendedores()
    select_agregacao()