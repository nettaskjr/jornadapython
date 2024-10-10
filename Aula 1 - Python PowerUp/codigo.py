# 1 - Abrir o navegador
# 2 - entrar o site ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
# 3 - Fazer o login
# 4 - Importar a base de dados
# 5 - Cadastrar os produtos

# instalar o pyautogui e pandas
# $ pip install pyautogui pandas

#importar o pyautogui, time, pandas, os e messagebox
import pyautogui
import time
import pandas as pd
import os
import tkinter.messagebox

# tempo entre os comando do pyautogui
pyautogui.PAUSE = 1

# cadastramento do endereço absoluto
path = "C:\\projetos\\jornadapython\\Aula 1 - Python PowerUp"
os.chdir(path)

# 1 - Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# 2 - entrar o site ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(5)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# 3 - Fazer o login
usuario = "nestor@bbts.com.br"
senha = "senha"
time.sleep(3)
pyautogui.press("tab")
pyautogui.write(usuario)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")

# 4 - Importar a base de dados
tabela = pd.read_csv("produtos.csv")

# 5 - Cadastrar os produtos
linha = 0
time.sleep(3)
for linha in tabela.index:
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")      
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")

    # move o cursor até o primeiro campo
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")

# mensagem de sucesso
tkinter.messagebox.showinfo(title="Confirmação", message="Cadastramentos realizados com sucesso!")

