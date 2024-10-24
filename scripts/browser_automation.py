import subprocess
from config import PROGRAM_PATHS

def open_browser():
    """
    Abre o navegador Google Chrome usando o caminho configurado.
    """
    subprocess.Popen([PROGRAM_PATHS['chrome']])

def close_browser():
    """
    Fecha o navegador Google Chrome utilizando o comando taskkill no Windows.
    """
    subprocess.call("taskkill /IM chrome.exe /F", shell=True)
