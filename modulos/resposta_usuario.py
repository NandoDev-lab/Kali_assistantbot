from modulos.voz.reconhecimento import ReconhecimentoVoz
import pyttsx3

class RespostaUsuario:
    def __init__(self):
        self.reconhecimento = ReconhecimentoVoz()

    def falar(self, texto):
        """Método para falar com o usuário."""
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()

    def ouvir_resposta(self):
        """Captura a resposta do usuário através do reconhecimento de voz."""
        resposta = self.reconhecimento.ouvir_comando()
        return resposta.lower()  # Retorna a resposta em minúsculas para facilitar comparações

    def confirmar_resposta(self, comando):
        """Confirma a resposta do usuário. Se a resposta não for sim ou não, repete a pergunta."""
        while True:
            self.falar(f"Você disse: {comando}. Está correto?")
            resposta = self.ouvir_resposta()
            if "sim" in resposta:
                return True
            elif "não" in resposta:
                return False
