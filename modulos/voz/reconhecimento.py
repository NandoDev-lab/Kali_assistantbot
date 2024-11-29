import sounddevice as sd
import vosk
import json

class ReconhecimentoVoz:
    def __init__(self, model_path="modulos/voz/vosk_modelo_Brasil_pt/"):
        self.model = vosk.Model(model_path)
        self.rec = vosk.KaldiRecognizer(self.model, 16000)

    def ouvir_comando(self):
        print("Aguardando comando...")
        with sd.InputStream(samplerate=16000, channels=1, dtype="int16") as stream:
            while True:
                dados = stream.read(4000)[0]
                # Converte para bytes para ser compatível com o Vosk
                dados_bytes = dados.tobytes()
                if self.rec.AcceptWaveform(dados_bytes):
                    resultado = json.loads(self.rec.Result())
                    comando = resultado.get("text", "")
                    if comando:
                        print(f"Comando reconhecido: {comando}")
                        return comando