import os
from tkinter.filedialog import askdirectory
def organizador():
    caminho = askdirectory(title="Selecione uma pasta")

    list_arquivo = os.listdir(caminho) 

    locais = {
        "imagens": [".png", ".jpg", ".jpeg"],
        "planilha": [".xlsx"],
        "pdfs": [".pdf"],
        "audio": [".mp3"],
        "video": [".mp4"]
    }

    for arquivo in list_arquivo:
        #fdigital-pdv-estoque .png
        nome, extensao = os.path.splitext(arquivo)
        for pasta in locais:
            if extensao in locais[pasta]:
                try:
                    if not os.path.exists(f"{caminho}/{pasta}"):
                        os.mkdir(f"{caminho}/{pasta}")
                    os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
                except FileNotFoundError as e:
                    print(f"Não foi possivel criar pasta ou mover arquivo {e}")

    print("Pasta criada com sucesso")
                