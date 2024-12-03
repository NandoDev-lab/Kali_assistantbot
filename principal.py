from modulos.usuarios.gerenciador_usuarios import GerenciadorUsuarios
from modulos.usuarios.saudacoes import Saudacao
from modulos.voz.reconhecimento import ReconhecimentoVoz
from modulos.interacao_usuario import InteracaoUsuario
import pyttsx3

def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def processar_comando(comando, nome_usuario, saudacao):
    if "saudação" in comando:
        saudacao.obter_saudacao(nome_usuario)
    # Adicione aqui outros comandos e ações

def solicitar_nome(reconhecimento):
    falar("Olá! Qual é o seu nome?")
    return reconhecimento.ouvir_comando()

def iniciar():
    gerenciador_usuarios = GerenciadorUsuarios()
    saudacao = Saudacao()
    reconhecimento = ReconhecimentoVoz()
    interacao = InteracaoUsuario()

    # Solicita o nome do usuário e verifica no banco de dados
    nome_usuario = solicitar_nome(reconhecimento)

    if not gerenciador_usuarios.usuario_existe(nome_usuario):
        mensagem = f"Novo usuário detectado: {nome_usuario}. Registrando..."
        falar(mensagem)
        gerenciador_usuarios.adicionar_usuario(nome_usuario, "você", status="novo")
        saudacao_mensagem = f"Seja bem-vindo ao sistema, {nome_usuario}!"
    else:
        saudacao_mensagem = f"Bem-vindo de volta, {nome_usuario}!"
        gerenciador_usuarios.atualizar_status(nome_usuario, "existente")

    # Saudação inicial com período do dia
    saudacao.obter_saudacao(nome_usuario)

    # Loop contínuo para reconhecimento de voz e execução de comandos
    while True:
        comando = interacao.perguntar_acao()
        if interacao.confirmar_acao(comando):
            processar_comando(comando, nome_usuario, saudacao)

    # Fechar conexão com banco ao final
    gerenciador_usuarios.fechar_conexao()

if __name__ == "__main__":
    iniciar()
