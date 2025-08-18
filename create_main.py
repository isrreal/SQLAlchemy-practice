from conf.db_session import create_tables

# A verificação abaixo garante que a função create_tables()
# será executada apenas se este arquivo for o script principal.
if __name__ == "__main__":
    create_tables()