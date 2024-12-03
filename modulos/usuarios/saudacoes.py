import datetime
import pyttsx3

class Saudacao:
    def __init__(self):
        self.engine = pyttsx3.init()

    def falar(self, texto):
        self.engine.say(texto)
        self.engine.runAndWait()

    def obter_periodo_do_dia(self):
        hora_atual = datetime.datetime.now().hour
        if 6 <= hora_atual < 12:
            return "manhã"
        elif 12 <= hora_atual < 18:
            return "tarde"
        else:
            return "noite"

    def obter_saudacao(self, nome_usuario):
        periodo = self.obter_periodo_do_dia()
        if periodo == "manhã":
            saudacao = f"Bom dia, {nome_usuario}! Como você está nesta manhã?"
        elif periodo == "tarde":
            saudacao = f"Boa tarde, {nome_usuario}! Como está a sua tarde?"
        else:
            saudacao = f"Boa noite, {nome_usuario}! Como foi seu dia?"

        self.falar(saudacao)
        return saudacao
