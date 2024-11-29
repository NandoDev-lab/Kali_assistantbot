import sqlite3

class GerenciadorUsuarios:
    def __init__(self, db_name="usuarios.db"):
        self.conexao = sqlite3.connect(db_name)
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        # Adiciona a coluna 'status' para registrar se o usuário é novo ou existente
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                nome TEXT PRIMARY KEY,
                tratamento TEXT,
                status TEXT
            )
        ''')
        self.conexao.commit()

    def adicionar_usuario(self, nome, tratamento, status="novo"):
        # Ajustado para aceitar o parâmetro status
        self.cursor.execute(
            "INSERT OR REPLACE INTO usuarios (nome, tratamento, status) VALUES (?, ?, ?)",
            (nome, tratamento, status)
        )
        self.conexao.commit()

    def usuario_existe(self, nome):
        self.cursor.execute("SELECT * FROM usuarios WHERE nome = ?", (nome,))
        return self.cursor.fetchone() is not None

    def atualizar_status(self, nome, status):
        self.cursor.execute(
            "UPDATE usuarios SET status = ? WHERE nome = ?", (status, nome)
        )
        self.conexao.commit()

    def fechar_conexao(self):
        self.conexao.close()
