import random
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


# ---------------- Funções de inserção ---------------- #

def inserir_sabores(session):
    sabores = [
        "Morango", "Chocolate", "Baunilha", "Limão", "Coco",
        "Uva", "Abacaxi", "Maracujá", "Açaí", "Melancia"
    ]
    objs = [Sabor(nome = s) for s in sabores]
    session.add_all(objs)
    session.commit()
    return objs


def inserir_embalagens(session):
    embalagens = ["Plástico", "Papel", "Caixa", "Saco Zip", "Cone"]
    objs = [TipoEmbalagem(nome = e) for e in embalagens]
    session.add_all(objs)
    session.commit()
    return objs


def inserir_tipos_picole(session):
    tipos = ["Tradicional", "Zero Açúcar", "Vegano", "Premium", "Infantil"]
    objs = [TipoPicole(nome = t) for t in tipos]
    session.add_all(objs)
    session.commit()
    return objs


def inserir_ingredientes(session):
    ingredientes = [
        "Leite", "Açúcar", "Água", "Cacau", "Frutas Vermelhas",
        "Castanha", "Amendoim", "Café", "Mel", "Suco Concentrado"
    ]
    objs = [Ingrediente(nome = i) for i in ingredientes]
    session.add_all(objs)
    session.commit()
    return objs


def inserir_revendedores(session):
    revs = [
        ("12345678000101", "Sorvetes Brasil Ltda", "Sorvetes do Brasil", "contato@sorvetes.com"),
        ("98765432000155", "Distribuidora Gelada LTDA", "Distribuidora Gelada", "vendas@gelada.com"),
        ("19283746000177", "Frutos Tropicais LTDA", "Frutos Tropicais", "info@tropicais.com"),
    ]
    objs = [
        Revendedor(CNPJ = r[0], razao_social = r[1], nome = r[2], contato = r[3])
        for r in revs
    ]
    session.add_all(objs)
    session.commit()
    return objs

def inserir_conservantes(session):
    conservantes = [
        ("Sorbato de Potássio", "Inibe crescimento de fungos"),
        ("Benzoato de Sódio", "Evita deterioração"),
        ("Ácido Cítrico", "Ajusta pH e conserva"),
    ]
    objs = [Conservante(nome = c[0], descricao = c[1]) for c in conservantes]
    session.add_all(objs)
    session.commit()
    return objs


def inserir_aditivos(session):
    aditivos = [
        ("Vitamina C", "C6H8O6"),
        ("Ferro", "Fe"),
        ("Cálcio", "Ca"),
        ("Vitamina D", "C27H44O"),
        ("Zinco", "Zn")
    ]
    objs = [AditivoNutritivo(nome = a[0], formula_quimica = a[1]) for a in aditivos]
    session.add_all(objs)
    session.commit()
    return objs


def inserir_revendedores(session):
    revs = [
        ("12345678000101", "Sorvetes do Brasil", "Sorvetes", "contato@sorvetes.com"),
        ("98765432000155", "Distribuidora Gelada", "Gelada", "vendas@gelada.com"),
        ("19283746000177", "Frutos Tropicais", "Tropicais", "info@tropicais.com"),
    ]

    objs = [Revendedor(CNPJ = r[0], razao_social = r[1], nome = r[2], contato = r[3]) for r in revs]

    session.add_all(objs)
    session.commit()
    return objs


def inserir_lotes(session, tipos_picole_ids, qtd = 20):
    lotes = []
    for _ in range(qtd):
        lote = Lote(
            id_tipo_picole = random.choice(tipos_picole_ids),
            quantidade = random.randint(50, 500)
        )
        lotes.append(lote)
    session.add_all(lotes)
    session.commit()
    return lotes


def inserir_notas_fiscais(session, lotes, revendedores, qtd = 10):
    notas = []
    for i in range(qtd):
        nf = NotaFiscal(
            valor = round(random.uniform(100, 2000), 2),
            numero_serie = f"NF{i + 1:04d}",
            descricao = f"Lote de picolés nº {i + 1}",
            id_revendedor = random.choice(revendedores).id
        )
        nf.lotes.extend(random.sample(lotes, k = 2))
        notas.append(nf)
    session.add_all(notas)
    session.commit()
    return notas


def inserir_picoles(session, sabores_ids, embalagens_ids, tipos_picole_ids,
                    ingredientes, conservantes, aditivos, qtd = 20):
    picoles = []
    for _ in range(qtd):
        picole = Picole(
            preco=round(random.uniform(2, 8), 2),
            id_sabor=random.choice(sabores_ids),
            id_tipo_embalagem=random.choice(embalagens_ids),
            id_tipo_picole=random.choice(tipos_picole_ids),
        )
        picole.ingredientes.extend(random.sample(ingredientes, k = 2))
        picole.conservantes.append(random.choice(conservantes))
        picole.aditivos_nutritivos.append(random.choice(aditivos))
        picoles.append(picole)
    session.add_all(picoles)
    session.commit()
    return picoles


# ---------------- Função principal ---------------- #

def popular():
    with create_session() as session:
        sabores = inserir_sabores(session)
        embalagens = inserir_embalagens(session)
        tipos_picole = inserir_tipos_picole(session)
        ingredientes = inserir_ingredientes(session)
        conservantes = inserir_conservantes(session)
        aditivos = inserir_aditivos(session)
        revendedores = inserir_revendedores(session)

        lotes = inserir_lotes(session, [t.id for t in tipos_picole])
        notas = inserir_notas_fiscais(session, lotes, revendedores)

        picoles = inserir_picoles(
            session,
            sabores_ids = [s.id for s in sabores],
            embalagens_ids = [e.id for e in embalagens],
            tipos_picole_ids = [t.id for t in tipos_picole],
            ingredientes = ingredientes,
            conservantes = conservantes,
            aditivos = aditivos
        )

    print("Banco populado com sucesso (50+ registros adicionados).")


if __name__ == "__main__":
    popular()
