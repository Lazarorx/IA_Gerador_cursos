from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import re

def preprocessar_texto(texto):
    stop_words = set(stopwords.words('portuguese'))
    
    # Remover caracteres especiais e números
    texto = re.sub(r'[^a-zA-Z]', ' ', texto)
    
    # Converter para minúsculas e remover stopwords
    palavras = [word.lower() for word in texto.split() if word.lower() not in stop_words]
    
    # Juntar as palavras novamente
    texto_processado = ' '.join(palavras)
    
    return texto_processado

def vetorizar_texto(dados_texto):
    vectorizer = TfidfVectorizer(stop_words='portuguese')
    return vectorizer.fit_transform(dados_texto).toarray(), vectorizer
