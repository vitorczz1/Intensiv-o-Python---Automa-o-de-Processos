#!/usr/bin/env python
# coding: utf-8

# In[46]:


# Automação na Web

# Passo 1 - Entrar na internet
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()

# Passo 2 - Pegar a cotação do Dolar
#entrar no google

navegador.get("https://www.google.com/")

#pesquisar "cotação dólar"

navegador.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")

navegador.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")

print(cotacao_dolar)


# Passo 3 - Pegar a cotação do Euro

navegador.get("https://www.google.com/")

navegador.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")

navegador.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")

print(cotacao_euro)


# Passo 4 - Pegar a cotação do Ouro

navegador.get("https://www.melhorcambio.com/ouro-hoje")

cotacao_ouro = navegador.find_element_by_xpath('//*[@id="comercial"]').get_attribute("value")

cotacao_ouro = cotacao_ouro.replace(",",".")

print(cotacao_ouro)


# In[47]:


# Passo 5 - Importar e atualizar a base de dados

import pandas as pd 

bd = pd.read_excel("Produtos.xlsx")

display(bd)


# In[44]:


#atualizar a cotação
#aonde a coluna "Moeda" = Dólar
# bd.loc[linha, coluna]

bd.loc[bd["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)

bd.loc[bd["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)

bd.loc[bd["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

#atualizar o preco de compra -> Preço original * Cotação
#bd["Preço Base Reais"] = bd["Cotação"] * bd["Preço Base Original"]

#atualizar o preço de venda -> Pre
#bd["Preço Final"] = bd["Percentual Preço Base"] * tabela["Preço Base Reais"]

# .map() para formatação

display(bd)


# In[45]:


# Passo 6 - Exportar a base de dados atualizada
bd.to_excel("Produtos Novo.xlsx", index=False)

