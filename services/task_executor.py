from scripts.browser_automation import open_browser, close_browser
from scripts.file_conversion import convert_file
from services.nlp_processor import process_command

def execute_command(command):
    action = process_command(command)

    if action == "open_browser":
        open_browser()
    elif action == "close_browser":
        close_browser()
    elif action == "convert_file":
        convert_file("document.pdf")
    else:
        print("Comando não reconhecido.")
