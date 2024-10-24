import os
from config import PROGRAM_PATHS

def open_program(program_name):
    """
    Abre um programa no Windows usando o caminho configurado.

    Args:
        program_name (str): Nome do programa a ser aberto.
    """
    if program_name in PROGRAM_PATHS:
        os.startfile(PROGRAM_PATHS[program_name])

def close_program(program_name):
    """
    Fecha um programa no Windows utilizando o comando taskkill.

    Args:
        program_name (str): Nome do programa a ser fechado.
    """
    os.system(f"taskkill /IM {program_name}.exe /F")
