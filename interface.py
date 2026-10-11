import tkinter as tk
from main import organizador

janela = tk.Tk()

janela.title("Organize seus arquivos")
janela.geometry("400x300")

texto = tk.Label(janela, text="Clique no botão para organizar seus arquivos!", font=("Arial", 14))
texto.pack(pady=20)

botao = tk.Button(
    janela,
    text="Clique aqui",
    command=lambda: organizador(),
)
botao.pack(pady=10)

janela.mainloop()