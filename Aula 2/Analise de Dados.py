#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Análise de dados 

# Passo 1 - Importar a base de dados pro Python

import pandas as pd

bd = pd.read_csv(r"telecom_users.csv")

display(bd)


# In[3]:


# Passo 2 - Visualizar a base de dados 
#Entender as informações disponíveis)
#Formatar a base de dados

bd = bd.drop("Unnamed: 0", axis = 1) #0 é linha e 1 é coluna 

display(bd)


# In[4]:


# Passo 3 - Tratamento da base de dados

#Valores numéricos identificados como texto
bd["TotalGasto"] = pd.to_numeric(bd["TotalGasto"], errors ="coerce")

#Valores que estão vazios
bd = bd.dropna(how="all", axis=1) 

#all é quando quer excluir colunas completamente vazias
#any é quando quer excluir colunas que tem PELO MENOS 1 valor vazio

#Excluir Informações inúteis 
bd = bd.dropna(how="any", axis=0) 

print(bd.info())


# In[5]:


# Passo 4 - Análise exploratória -> Ver como estão os cancelamentos

count = bd["Churn"].value_counts(normalize=True).map("{:.1%}".format) #Conta a quantidade

display(count) 


# In[9]:


# Passo 5 - Olhando as colunas da nossa base de dados -> Identificar o motivo

import plotly.express as px

for column in bd.columns:
    grafico = px.histogram(bd, x=column, color="Churn")
    grafico.show()


# In[ ]:




