#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

# Como eu faria isso ?

# Passo 1 - Entrar no sistema (entrar no link: https://drive.google.com/drive/u/1/my-drive)

pyautogui.press("win")
pyautogui.write("Google Chrome")
pyautogui.press("enter")

link = "https://drive.google.com/drive/u/1/my-drive"
pyperclip.copy(link)

pyautogui.hotkey("ctrl", "v")

pyautogui.press("enter")


# Passo 2 - Navegar no sistema

time.sleep(3) #python espere 3 segundos

pyautogui.click(x=1104, y=882, clicks=2) #dar dois clique

# pyautogui.click(x=478, y=317, button = "right") click direito


# Passo 3 - Baixar o arquivo de vendas

time.sleep(3) #python espere 3 segundos

pyautogui.click(x=658, y=733) #dar um clique

pyautogui.click(x=1473, y=189) #dar um clique

pyautogui.click(x=1314, y=651) #dar um clique

time.sleep(3) #aguarda o download


# Passo 4 - Calcular o faturamento e quantidade de produtos vendidos

#instalar pandas, e openpyxl
import pandas as pd

tabela = pd.read_excel(r"C:\Users\Vitor\Downloads\Vendas.xlsx") #ler o formato

quantidade = tabela["Quantidade"].sum()
faturamento = tabela["Valor Final"].sum()


# Passo 5 - Enviar o email para a diretoria

pyautogui.hotkey("ctrl", "t")

email = "gmail.com"
pyperclip.copy(email)

pyautogui.hotkey("ctrl", "v")

pyautogui.press("enter")

time.sleep(5) #aguarda carregar

pyautogui.click(x=35, y=206) #dar um clique

time.sleep(1)

pyautogui.click(x=1478, y=412) #dar um clique

destino = "vaniavitor03@gmail.com" 
pyperclip.copy(destino)

pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab")

time.sleep(1)

assunto = "Relatório de Vendas"
pyperclip.copy(assunto)

pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab")

texto = f"""Prezada Deloitte,

O faturamento foi de R${faturamento:,.2f}
A quantidade de produtos foi de {quantidade:,} unidades.

At.te Vitor"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

time.sleep(1)

pyautogui.hotkey("ctrl", "enter")


# In[35]:


# Descobrir a localização do Mouse

time.sleep(5)

pyautogui.position() #descobre a posicao do mouse
#pyautogui.click(x=524, y=370) #dar um clique

