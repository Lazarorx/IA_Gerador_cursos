
# Sistema de Cursos Online

## Introdução

Este é um projeto em andamento para um Sistema de Cursos Online, onde os usuários podem inserir tópicos de cursos e receber previsões sobre os níveis de dificuldade desses cursos. O projeto utiliza técnicas de Processamento de Linguagem Natural (PLN) e aprendizado de máquina para realizar as previsões.

## Funcionalidades Atuais

- **Página Inicial**: Uma página inicial simples com um formulário para inserir os tópicos dos cursos.
- **Preprocessamento de Texto**: Um módulo (`processamento.py`) que realiza o preprocessamento de texto, removendo stopwords, caracteres especiais e números.
- **Vetorização de Texto**: O texto é vetorizado usando a técnica TF-IDF para ser usado como entrada para o modelo de aprendizado de máquina.

## Como Executar

1. Instale as dependências listadas no arquivo `requirements.txt`.
2. Execute o arquivo `app.py` para iniciar o servidor Flask.
3. Abra um navegador e vá para `http://localhost:3000` para acessar a interface do usuário.

## Próximos Passos

O projeto está em constante evolução, e os próximos passos incluem:

- **Treinamento do Modelo**: Criarei um novo conjunto de dados de treinamento e treine o modelo novamente.
- **Novos Algoritmos de Aprendizado de Máquina**: Experimentarei diferentes algoritmos de aprendizado de máquina para melhorar a precisão das previsões.
- **Melhorias na Interface do Usuário**: Aprimorarei a experiência do usuário na página inicial.

Fique atento para atualizações e melhorias contínuas!

