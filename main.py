import logging
from services.speech_recognition import recognize_speech
from services.task_executor import execute_command

# Configurações de logs
logging.basicConfig(filename="logs/system.log", level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")

def main():
    print("Iniciando o assistente inteligente...")

    while True:
        command = recognize_speech()
        if command:
            logging.info(f"Comando reconhecido: {command}")
            execute_command(command)
        else:
            logging.info("Nenhum comando reconhecido.")

if __name__ == "__main__":
    main()
