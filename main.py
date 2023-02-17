#instalando biblioteca de tradução
pip install googletrans==3.1.0a0

#importando imagens para o COLAB
import cv2
from google.colab.patches import cv2_imshow

!wget -O 'tela1.png' 'https://github.com/Group-5-Data4All/projeto-final/blob/iohana/images/tela1.png?raw=true'
!wget -O 'tela2.png' 'https://github.com/Group-5-Data4All/projeto-final/blob/iohana/images/tela2.png?raw=true'

#exibindo imagem 1
imagem = cv2.imread('tela1.png')
cv2_imshow(imagem)

#importando e exibindo o dataset
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Group-5-Data4All/projeto-final/iohana/dataset.csv')
print(df.info())
df

#traduzindo as colunas para pt
from googletrans import Translator

colunas = []
tradutor = Translator()

for i in df.columns:
  traduzido = tradutor.translate(i, src='en', dest= 'pt')
  colunas.append(traduzido.text.capitalize())

df.columns = colunas
print(df.info())

#exibindo colunas que serão analisadas
df = df[['Curso', 'Qualificação anterior', 'Atendimento diurno/noturno', 
   'Qualificação da mãe', 'Qualificação do pai', 'Ocupação da mãe', 
   'Ocupação do pai', 'Gênero', 'Idade na inscrição', 'Alvo']]
df

#exibindo imagem 2
imagem2 = cv2.imread('tela2.png')
cv2_imshow(imagem2)