from modulos.resposta_usuario import RespostaUsuario
import pyttsx3

class InteracaoUsuario:
    def __init__(self):
        self.resposta_usuario = RespostaUsuario()

    def falar(self, texto):
        """Método para falar com o usuário."""
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()

    def perguntar_acao(self):
        """Pergunta ao usuário o que ele deseja fazer e retorna o comando."""
        self.falar("O que você deseja fazer?")
        comando = self.resposta_usuario.ouvir_resposta()
        return comando

    def confirmar_acao(self, comando):
        """Confirma com o usuário se o comando está correto."""
        while True:
            self.falar(f"Você disse: {comando}. Está correto?")
            resposta = self.resposta_usuario.ouvir_resposta()
            if "sim" in resposta:
                return True
            elif "não" in resposta:
                self.falar("Por favor, diga novamente o que deseja fazer.")
                comando = self.perguntar_acao()
            else:
                self.falar("Desculpe, não entendi. Responda com sim ou não.")
