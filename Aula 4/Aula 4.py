#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Ciência de Dados e Inteligência Artificial

# Passo 1: Entendimento do Desafio

# Passo 2: Entendimento da Área/Empresa

# Passo 3: Extração/Obtenção de Dados

# Passo 4: Ajuste de Dados (Tratamento/Limpeza)

# Passo 5: Análise Exploratória

# Passo 6: Modelagem + Algoritmos (Aqui que entra a Inteligência Artificial, se necessário)

# Passo 7: Interpretação de Resultados


# In[3]:


# Passo 3

import pandas as pd

bd = pd.read_csv("advertising.csv")

display(bd)


# In[8]:


import matplotlib.pyplot as plt
import seaborn as sns

sns.heatmap(bd.corr(), cmap="Wistia", annot=True)
plt.show()

sns.pairplot(bd)
plt.show()


# In[14]:


from sklearn.model_selection import train_test_split

# separar dados de x e de y

# y - é quem a gente quer descobrir
y = bd["Vendas"]

# x - é o resto
x = bd.drop("Vendas", axis=1)

# aplicar o train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, random_state = 1)


# In[15]:


#Testar os modelos 

#Regressão Linear
#RandomForest(Árvore de decisão)

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

modelo_regressaolinear = LinearRegression()
modelo_randomforest = RandomForestRegressor()

modelo_regressaolinear.fit(x_treino, y_treino)
modelo_randomforest.fit(x_treino, y_treino)


# In[16]:


previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_randomforest = modelo_randomforest.predict(x_teste)

# R² vai de 0 a 100%, quanto maior melhor

from sklearn import metrics

print(metrics.r2_score(y_teste, previsao_regressaolinear))
print(metrics.r2_score(y_teste, previsao_randomforest))


# In[20]:


# RandomForest é o modelo vencedor 
bd_auxiliar = pd.DataFrame()
bd_auxiliar["y_teste"] = y_teste
bd_auxiliar["regressao linear"] = previsao_regressaolinear
bd_auxiliar["random forest"] = previsao_randomforest

plt.figure(figsize=(15,7))
sns.lineplot(data=bd_auxiliar)
plt.show()


# In[22]:


sns.barplot(x=x_treino.columns, y=modelo_randomforest.feature_importances_)
plt.show()


# In[25]:


# Qual a importância?

#importar a nova_tabela com o pandas

#import pandas as pd

#novo_bd = pd.read_excel("novo_bd.xlsx")

#previsao = modelo_randomforest.predict(novo_bd)

#print(previsao)


# In[ ]:




