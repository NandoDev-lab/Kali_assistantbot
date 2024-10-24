import json
import pyaudio
from vosk import Model, KaldiRecognizer
from config import AUDIO_MODEL_PATH

# Carregar o modelo Vosk
model = Model(AUDIO_MODEL_PATH)
rec = KaldiRecognizer(model, 16000)

# Inicializar microfone
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

def recognize_speech():
    print("Estou ouvindo...")
    data = stream.read(4096)
    if rec.AcceptWaveform(data):
        result = json.loads(rec.Result())
        command = result.get('text', '')
        return command
    return ""
