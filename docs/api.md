
# Documentação da API

### Criar um livro
- Endpoint: `/books`
- Método: `POST`
- Request Body:
  - name (obrigatório, string): Nome do livro.
- Resposta:
  - book_id (string): ID do livro criado.
  - status code: 201 (criado)

### Criar um parágrafo
- Endpoint: `/books/<book_id>/paragraphs`
- Método: `POST`
- Request Body:
  - text (obrigatório, string, tamanho máximo 300 caracteres): Texto do parágrafo.
  - position (obrigatório, inteiro): Posição do parágrafo.
- Resposta:
  - paragraph_id (string): ID do parágrafo criado.
  - status code: 201 (criado)

### Votar em um parágrafo
- Endpoint: `/paragraphs/<paragraph_id>/votes`
- Método: `POST`
- Resposta:
  - votes (inteiro): Número de votos no parágrafo.
  - status code: 200 (OK)

### Recuperar livro com seus parágrafos
- Endpoint: `/books/<book_id>`
- Método: `GET`
- Resposta:
  - name (string): Nome do livro.
  - paragraphs (lista de objetos): Lista de parágrafos com suas informações (id, text, votes, position). A lista está ordenada pela posição do parágrafo e, caso existam mais de um parágrafo na mesma posição, o parágrafo com mais votos será retornado.
  - status code: 200 (OK)
