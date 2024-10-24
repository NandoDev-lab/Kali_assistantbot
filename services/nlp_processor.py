def process_command(command):
    if "abrir navegador" in command:
        return "open_browser"
    elif "fechar navegador" in command:
        return "close_browser"
    elif "converter arquivo" in command:
        return "convert_file"
    else:
        return "unknown"
