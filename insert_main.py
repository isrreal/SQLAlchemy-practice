from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem 
from models.tipo_picole import TipoPicole 
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor


from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole 

def insert_aditivo_nutritivo() -> AditivoNutritivo:
    print("Cadastrando aditivo nutritivo")

    nome: str = input('Informe o nome do aditivo nutrritivo: ')
    formula_quimica: str = input('Informe a fórmula química do aditivo: ')

    aditivo_nutritivo: AditivoNutritivo = AditivoNutritivo(nome = nome, formula_quimica = formula_quimica)

    # abrindo contexto: todas as operações serão efetivadas somente depois do commit. 
    with create_session() as session:
        session.add(aditivo_nutritivo)
        
        session.commit()

    return aditivo_nutritivo

def insert_sabor() -> Sabor:
    print("Cadastrando sabores")

    nome: str = input('Informe o nome do Sabor: ')
    sabor: Sabor = Sabor(nome)

    with create_session() as session:
        session.add(sabor)
        
        session.commit()

    return sabor

def insert_tipo_embalagem() -> TipoEmbalagem:
    print("Cadastrando Tipo Embalagem")

    nome: str = input('Informe o nome do Tipo Embalagem: ')

    tipo_embalagem: TipoEmbalagem = TipoEmbalagem(nome = nome)

    with create_session() as session:
        session.add(tipo_embalagem)
        
        session.commit()

    return TipoEmbalagem

def insert_tipo_picole() -> TipoPicole:
    print("Cadastrando Tipo Picole")

    nome: str = input('Informe o nome do Tipo Picole: ')

    tipo_picole: TipoPicole = TipoPicole(nome = nome)

    with create_session() as session:
        session.add(tipo_picole)
        
        session.commit()

    return TipoPicole

def insert_ingrediente() -> Ingrediente:
    print("Cadastrando Ingrediente")

    nome: str = input('Informe o nome do Ingrediente: ')

    ingrediente: Ingrediente = Ingrediente(nome = nome)

    with create_session() as session:
        session.add(ingrediente)
        
        session.commit()

    return Ingrediente

def insert_conservante() -> Conservante:
    print("Cadastrando Conservante")

    nome: str = input('Informe o nome do Conservante: ')
    descricao: str = input('Informe a descrição do Conservante: ')

    conservante: Conservante = Conservante(nome = nome, descricao = descricao)

    with create_session() as session:
        session.add(conservante)
        
        session.commit()

    return conservante

def insert_revendedor() -> Revendedor:
    print("Cadastrando Revendedor")

    CNPJ: str = input('Informe o CNPJ do revendedor: ')
    razao_social: str = input('Informe a razão social do revendedor: ')
    contato: str = input('Informe o contato do revendedor: ')

    revendedor: Revendedor = Revendedor(CNPJ = CNPJ, razao_social = razao_social, contato = contato)

    with create_session() as session:
        session.add(revendedor)
        
        session.commit()

    return revendedor

def insert_lote() -> Lote:
    print("Cadastrando Lote")

    id_tipo_picole: int = input('Informe o ID tipo do picolé: ')
    quantidade: int = input('Informe a quantidade de picolé: ')

    lote: Lote = Lote(id_tipo_picole = id_tipo_picole, quantidade = quantidade)

    with create_session() as session:
        session.add(lote)
        
        session.commit()

    return lote

def insert_nota_fiscal() -> None:
    print("Cadastrando Nota Fiscal")

    valor: float = input("Informe o valor da nota fiscal: ")
    numero_serie: str = input("Informe o número de série: ")
    descricao: str = input("Informe a descrição: ")

    revendedor: Revendedor = insert_revendedor()
    id_revendedor: int = revendedor.id 

    nota_fiscal: NotaFiscal = NotaFiscal(valor = valor, numero_serie = numero_serie, descricao = descricao, id_revendedor = id_revendedor)
    
    lote1 = insert_lote()
    lote2 = insert_lote()
    
    nota_fiscal.lotes.append(lote1)
    nota_fiscal.lotes.append(lote2)

    with create_session() as session:
        session.add(nota_fiscal)
        
        session.commit()

    print('Nota Fiscal cadastrada com sucesso')
    print(f"ID: {nota_fiscal.id}")
    print(f"Data: {nota_fiscal.data_criacao}")
    print(f"Valor: {nota_fiscal.valor}")
    print(f"Número de série: {nota_fiscal.numero_serie}")
    print(f"Descrição: {nota_fiscal.descricao}")
    print(f"ID Revendedor: {nota_fiscal.id_revendedor}")

# 10 Picole
def insert_picole() -> None:
    print('Cadastrando Picole')

    preco: float = input('Informe o preço do picole: ')
    id_sabor: int = input('Informe o ID do sabor: ')
    id_tipo_picole: int = input('Informe o ID do tipo de picole: ')
    id_tipo_embalagem: int = input('Informe o ID do tipo da embalagem: ')

    picole: Picole = Picole(id_sabor=id_sabor, id_tipo_embalagem=id_tipo_embalagem, id_tipo_picole=id_tipo_picole, preco=preco)

    ingrediente1 = insert_ingrediente()
    picole.ingredientes.append(ingrediente1)

    ingrediente2 = insert_ingrediente()
    picole.ingredientes.append(ingrediente2)

    # Tem conservantes?
    conservante = insert_conservante()
    picole.conservantes.append(conservante)

    # Tem aditivos nutritivos?
    aditivo_nutritivo = insert_aditivo_nutritivo()
    picole.aditivos_nutritivos.append(aditivo_nutritivo)

    with create_session() as session:
        session.add(picole)

        session.commit()
    
        print('Picole cadastrado com sucesso')
        print(f'ID: {picole.id}')
        print(f'Data: {picole.data_criacao}')
        print(f'Preço: {picole.preco}')
        print(f'Sabor: {picole.sabor.nome}')
        print(f'Tipo Picole: {picole.tipo_picole.nome}')
        print(f'Tipo Embalagem: {picole.tipo_embalagem.nome}')
        print(f'Ingredientes: {picole.ingredientes}')
        print(f'Conservantes: {picole.conservantes}')
        print(f'Aditivos Nutritivos: {picole.aditivos_nutritivos}')


if __name__ == '__main__':
    insert_aditivo_nutritivo()

    insert_sabor()

    insert_tipo_embalagem()

    insert_tipo_picole()

    insert_ingrediente()

    insert_conservante()

    insert_revendedor()

    insert_lote()

    insert_nota_fiscal()

    insert_picole()