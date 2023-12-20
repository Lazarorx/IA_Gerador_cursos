from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from utils.preprocessamento import preprocessar_texto
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.model_selection import train_test_split
from utils.modelo import definir_modelo, treinar_modelo

app = Flask(__name__)
CORS(app)  # Permite solicitações de origens diferentes

# Inicialização de dados educacionais
dados_educacionais = pd.DataFrame({
    'texto': ['Gramática Portuguesa', 'Redação em Português', 'Literatura Brasileira', 'História da Língua Portuguesa'],
    'nivel': ['Intermediário', 'Avançado', 'Avançado', 'Intermediário']
})

# Pré-processamento e vetorização
dados_educacionais['texto_processado'] = dados_educacionais['texto'].apply(preprocessar_texto)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(dados_educacionais['texto_processado'])
y = pd.factorize(dados_educacionais['nivel'])[0]

# Ordenar os índices para evitar o erro esparsa no TensorFlow
X.sort_indices()

# Divisão de dados para treinamento do modelo
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Definir e treinar o modelo
modelo = definir_modelo(X.shape[1], len(set(y)))
treinar_modelo(modelo, X_train, y_train, X_val, y_val)

@app.route('/')
def index():
    # Renderizar o código HTML existente
    return render_template("index.html")

@app.route('/gerar-cursos', methods=['POST'])
def gerar_cursos():
    # Recebe dados da requisição
    dados = request.form
    topicos = dados.get('topicos', '').split('\n')
    numero_cursos = int(dados.get('numero_cursos', 1))

    # Verifica se a lista de tópicos não está vazia
    if not topicos:
        return jsonify({"erro": "A lista de tópicos está vazia."})

    # Pré-processamento e vetorização dos tópicos fornecidos
    topicos_processados = [preprocessar_texto(topico) for topico in topicos]
    X_novos = vectorizer.transform(topicos_processados)

    # Ordenar os índices para evitar o erro esparsa no TensorFlow
    X_novos = tf.sparse.reorder(X_novos)

    # Previsão dos níveis para os novos tópicos
    y_novos = modelo.predict(X_novos)

    # Mapeamento dos rótulos de volta para os níveis originais
    niveis_previstos = pd.Series(y_novos).map({0: 'Intermediário', 1: 'Avançado'})

    # Criação da resposta com os cursos gerados
    cursos_gerados = [{"topico": topico, "nivel_predito": nivel} for topico, nivel in zip(topicos, niveis_previstos)]

    # Limitar o número de cursos conforme solicitado pelo usuário
    cursos_gerados = cursos_gerados[:numero_cursos]

    return jsonify({"cursos": cursos_gerados})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
