const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 3000;

// Middleware para permitir requisições de origens diferentes (em um ambiente de produção, ajuste para segurança)
app.use(cors());

// Middleware para fazer o parsing do corpo da requisição como JSON
app.use(bodyParser.json());

// Rota para a geração de cursos
app.post('/gerar-curso', (req, res) => {
    const textoRecebido = req.body.texto;

    // Lógica para gerar o curso com base no texto recebido
    const cursoGerado = `Curso sobre ${textoRecebido}`;

    // Enviar o curso gerado como resposta
    res.json({ curso: cursoGerado });
});

// Iniciar o servidor
app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});
