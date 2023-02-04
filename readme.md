# API Livros
API simples para gerenciar livros e seus parágrafos, permitindo que os usuários votem em seus parágrafos favoritos.

## Dependências
- Flask==1.0.2
- uuid==1.30

## Instalação
+ Clone o repositório: git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
+ Entre na pasta do projeto: cd SEU_REPOSITORIO
+ Instale as dependências: pip install -r requirements.txt
+ Inicie o servidor: flask run

## Rotas disponíveis
- POST /books: cria um novo livro
- POST /books/<book_id>/paragraphs: adiciona um novo parágrafo a um livro existente
- POST /paragraphs/<paragraph_id>/votes: adiciona um voto a um parágrafo existente
- GET /books/<book_id>: lista um livro específico, incluindo seus parágrafos e quantidade de votos.

## Licença
Este projeto está licenciado sob a https://opensource.org/licenses/MIT, que permite que outras pessoas copiem, distribuam e modifiquem o projeto, mas não para fins comerciais.