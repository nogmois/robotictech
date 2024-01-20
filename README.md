
# API de Anotações de Imagem

## Descrição
Esta API permite aos usuários adicionar, visualizar, atualizar, sinalizar e deletar anotações em imagens.

## Endpoints

### POST /anotacoes
- **Descrição:** Adiciona uma nova anotação.
- **Corpo da Requisição:**
  ```json
  {
    "classe": "String",
    "confianca": Float,
    "centro_x": Integer,
    "centro_y": Integer,
    "largura": Integer,
    "altura": Integer
  }
  ```
- **Resposta de Sucesso:** `{ "mensagem": "Anotação adicionada com sucesso!" }`

### GET /anotacoes
- **Descrição:** Retorna todas as anotações.
- **Resposta de Sucesso:** Lista de anotações.

### GET /anotacoes/<int:id>
- **Descrição:** Retorna uma anotação específica.
- **Resposta de Sucesso:** Detalhes da anotação.

### PUT /anotacoes/<int:id>
- **Descrição:** Atualiza uma anotação existente.
- **Corpo da Requisição:** Dados da anotação para atualizar.
- **Resposta de Sucesso:** `{ "mensagem": "Anotação atualizada com sucesso!" }`

### DELETE /anotacoes/<int:id>
- **Descrição:** Deleta uma anotação específica.
- **Resposta de Sucesso:** `{ "mensagem": "Anotação deletada com sucesso!" }`

### PUT /anotacoes/sinalizar/<int:id>
- **Descrição:** Sinaliza uma anotação como errada.
- **Resposta de Sucesso:** `{ "mensagem": "Anotação sinalizada como errada." }`

### GET /anotacoes/alteradas
- **Descrição:** Retorna anotações que foram alteradas.
- **Resposta de Sucesso:** Lista de anotações alteradas.

### GET /anotacoes/sinalizadas
- **Descrição:** Retorna anotações que foram sinalizadas como erradas.
- **Resposta de Sucesso:** Lista de anotações sinalizadas.

## Como Executar

Para executar a aplicação localmente, siga os passos abaixo:

1. Clone o repositório para o seu ambiente local.

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git

- Certifique-se de ter o Python instalado em seu sistema.
2. Instale as dependências do projeto executando o seguinte comando no terminal:

  ```bash
  pip install -r requirements.txt

3. Rode a aplicação com o seguinte comando
  ```bash
  python app.py 

- Acesse o link: http://127.0.0.1:5000/anotacoes

## Testes
Para executar os testes automatizados, siga os passos abaixo:

1. Certifique-se de ter todas as dependências instaladas conforme mencionado acima.

2. Execute o seguinte comando no terminal para rodar os testes:
  ```bash
  python test_app.py

Isso executará os testes automatizados e fornecerá os resultados no terminal. Certifique-se de que todos os testes passem com sucesso antes de prosseguir com o desenvolvimento ou implantação da aplicação.

## Autor
## Murilo Nogueira