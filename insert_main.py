from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem 
from models.tipo_picole import TipoPicole 
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor

def insert_aditivo_nutritivo() -> None:
    print("Cadastrando aditivo nutritivo")

    nome: str = input('Informe o nome do aditivo nutrritivo: ')
    formula_quimica: str = input('Informe a fórmula química do aditivo: ')

    aditivo_nutritivo: AditivoNutritivo = AditivoNutritivo(nome = nome, formula_quimica = formula_quimica)

    # abrindo contexto: todas as operações serão efetivadas somente depois do commit. 
    with create_session() as session:
        session.add(aditivo_nutritivo)
        
        session.commit()

    print('Aditivo nutritivo adicionado com sucesso')
    print(f"ID: {aditivo_nutritivo.id}")
    print(f"Data: {aditivo_nutritivo.data_criacao}")
    print(f"Nome: {aditivo_nutritivo.nome}")
    print(f"Fórmula Química: {aditivo_nutritivo.formula_quimica}")

def insert_sabores() -> None:
    print("Cadastrando sabores")

    nome: str = input('Informe o nome do Sabor: ')
    sabor: Sabor = Sabor(nome)

    with create_session() as session:
        session.add(sabor)
        
        session.commit()

    print('Sabor cadastrado com sucesso')
    print(f"ID: {sabor.id}")
    print(f"Data: {sabor.data_criacao}")
    print(f"Nome: {sabor.nome}")

def insert_tipo_embalagem() -> None:
    print("Cadastrando Tipo Embalagem")

    nome: str = input('Informe o nome do Tipo Embalagem: ')

    tipo_embalagem: TipoEmbalagem = TipoEmbalagem(nome = nome)

    with create_session() as session:
        session.add(tipo_embalagem)
        
        session.commit()

    print('Tipo Embalagem cadastrado com sucesso')
    print(f"ID: {tipo_embalagem.id}")
    print(f"Data: {tipo_embalagem.data_criacao}")
    print(f"Nome: {tipo_embalagem.nome}")

def insert_tipo_picole() -> None:
    print("Cadastrando Tipo Picole")

    nome: str = input('Informe o nome do Tipo Picole: ')

    tipo_picole: TipoPicole = TipoPicole(nome = nome)

    with create_session() as session:
        session.add(tipo_picole)
        
        session.commit()

    print('Tipo Picole cadastrado com sucesso')
    print(f"ID: {tipo_picole.id}")
    print(f"Data: {tipo_picole.data_criacao}")
    print(f"Nome: {tipo_picole.nome}")

def insert_ingrediente() -> None:
    print("Cadastrando Ingrediente")

    nome: str = input('Informe o nome do Ingrediente: ')

    ingrediente: Ingrediente = Ingrediente(nome = nome)

    with create_session() as session:
        session.add(ingrediente)
        
        session.commit()

    print('Ingrediente cadastrado com sucesso')
    print(f"ID: {ingrediente.id}")
    print(f"Data: {ingrediente.data_criacao}")
    print(f"Nome: {ingrediente.nome}")

def insert_conservante() -> None:
    print("Cadastrando Conservante")

    nome: str = input('Informe o nome do Conservante: ')
    descricao: str = input('Informe a descrição do Conservante: ')

    conservante: Conservante = Conservante(nome = nome, descricao = descricao)

    with create_session() as session:
        session.add(conservante)
        
        session.commit()

    print('Ingrediente cadastrado com sucesso')
    print(f"ID: {conservante.id}")
    print(f"Data: {conservante.data_criacao}")
    print(f"Nome: {conservante.nome}")
    print(f"Descrição: {conservante.descricao}")

def insert_revendedor() -> None:
    print("Cadastrando Revendedor")

    CNPJ: str = input('Informe o CNPJ do revendedor: ')
    razao_social: str = input('Informe a razão social do revendedor: ')
    contato: str = input('Informe o contato do revendedor: ')

    revendedor: Revendedor = Revendedor(CNPJ = CNPJ, razao_social = razao_social, contato = contato)

    with create_session() as session:
        session.add(revendedor)
        
        session.commit()

    print('Revendedor cadastrado com sucesso')
    print(f"ID: {revendedor.id}")
    print(f"Data: {revendedor.data_criacao}")
    print(f"Nome: {revendedor.nome}")
    print(f"Razão Social: {revendedor.razao_social}")

if __name__ == '__main__':
    insert_aditivo_nutritivo()
    insert_sabores()
    insert_tipo_embalagem()
    insert_tipo_picole()
    insert_ingrediente()
    insert_conservante()
    insert_revendedor()