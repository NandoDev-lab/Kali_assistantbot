import random
import pyttsx3
from modulos.voz.reconhecimento import ReconhecimentoVoz

class Saudacao:
    def __init__(self):
        self.saudacoes = [
            "Olá, {nome}! Que bom te ver de novo!",
            "Oi, {nome}! Como você está hoje?",
            "Bem-vindo(a) de volta, {nome}! Vamos começar?",
            "Olá, {nome}! Sempre um prazer falar com você!"
        ]
        self.engine = pyttsx3.init()

    def obter_nome(self, nome):
        self.falar("Por favor, diga seu nome.")
        nome = ReconhecimentoVoz()
        return nome

    def obter_saudacao(self, nome):
        saudacao = random.choice(self.saudacoes).format(nome=nome)
        self.falar(saudacao)
        return saudacao

    def falar(self, texto):
        self.engine.say(texto)
        self.engine.runAndWait()
