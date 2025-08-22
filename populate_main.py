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


def popular_dados():
    with create_session() as session:
        # --------- Sabores ----------
        sabores = [
            "Morango", "Chocolate", "Baunilha", "Limão", "Coco",
            "Uva", "Abacaxi", "Maracujá", "Açaí", "Melancia"
        ]
        objs_sabores = [Sabor(nome = s) for s in sabores]
        session.add_all(objs_sabores)

        # --------- Tipo de Embalagem ----------
        embalagens = ["Plástico", "Papel", "Caixa", "Saco Zip", "Cone"]
        objs_embalagens = [TipoEmbalagem(nome = e) for e in embalagens]
        session.add_all(objs_embalagens)

        # --------- Tipo de Picolé ----------
        tipos_picole = ["Tradicional", "Zero Açúcar", "Vegano", "Premium", "Infantil"]
        objs_tipos_picole = [TipoPicole(nome = t) for t in tipos_picole]
        session.add_all(objs_tipos_picole)

        # --------- Ingredientes ----------
        ingredientes = [
            "Leite", "Açúcar", "Água", "Cacau", "Frutas Vermelhas",
            "Castanha", "Amendoim", "Café", "Mel", "Suco Concentrado"
        ]
        objs_ingredientes = [Ingrediente(nome = i) for i in ingredientes]
        session.add_all(objs_ingredientes)

        # --------- Conservantes ----------
        conservantes = [
            ("Sorbato de Potássio", "Inibe crescimento de fungos"),
            ("Benzoato de Sódio", "Evita deterioração"),
            ("Ácido Cítrico", "Ajusta pH e conserva"),
        ]
        objs_conservantes = [Conservante(nome = c[0], descricao = c[1]) for c in conservantes]
        session.add_all(objs_conservantes)

        # --------- Aditivos Nutritivos ----------
        aditivos = [
            ("Vitamina C", "C6H8O6"),
            ("Ferro", "Fe"),
            ("Cálcio", "Ca"),
            ("Vitamina D", "C27H44O"),
            ("Zinco", "Zn")
        ]
        objs_aditivos = [AditivoNutritivo(nome = a[0], formula_quimica = a[1]) for a in aditivos]
        session.add_all(objs_aditivos)

        # --------- Revendedores ----------
        revs = [
            ("12345678000101", "Sorvetes do Brasil", "contato@sorvetes.com"),
            ("98765432000155", "Distribuidora Gelada", "vendas@gelada.com"),
            ("19283746000177", "Frutos Tropicais", "info@tropicais.com"),
        ]
        objs_revendedores = [Revendedor(CNPJ = r[0], razao_social = r[1], contato = r[2]) for r in revs]
        session.add_all(objs_revendedores)

        session.commit()

        # IDs criados
        sabores_ids = [s.id for s in objs_sabores]
        embalagens_ids = [e.id for e in objs_embalagens]
        tipos_picole_ids = [t.id for t in objs_tipos_picole]
        ingredientes_objs = objs_ingredientes
        conservantes_objs = objs_conservantes
        aditivos_objs = objs_aditivos
        revs_objs = objs_revendedores

        # --------- Criando 20 lotes ----------
        lotes = []
        for _ in range(20):
            lote = Lote(
                id_tipo_picole = random.choice(tipos_picole_ids),
                quantidade = random.randint(50, 500)
            )
            lotes.append(lote)
        session.add_all(lotes)
        session.commit()

        # --------- Criando 10 notas fiscais ----------
        notas = []
        for i in range(10):
            nf = NotaFiscal(
                valor = round(random.uniform(100, 2000), 2),
                numero_serie = f"NF{i + 1:04d}",
                descricao = f"Lote de picolés nº {i + 1}",
                id_revendedor = random.choice(revs_objs).id
            )
            nf.lotes.extend(random.sample(lotes, k=2))
            notas.append(nf)
        session.add_all(notas)

        # --------- Criando 20 picolés ----------
        for _ in range(20):
            picole = Picole(
                preco = round(random.uniform(2, 8), 2),
                id_sabor = random.choice(sabores_ids),
                id_tipo_embalagem = random.choice(embalagens_ids),
                id_tipo_picole = random.choice(tipos_picole_ids),
            )

            picole.ingredientes.extend(random.sample(ingredientes_objs, k=2))
            picole.conservantes.append(random.choice(conservantes_objs))
            picole.aditivos_nutritivos.append(random.choice(aditivos_objs))
            session.add(picole)

        session.commit()

    print("✅ Inserção concluída: 50+ dados fictícios adicionados.")