# Como utilizar a API

## Criar livro
```
curl -X POST -H "Content-Type: application/json" -d '{"name": "Nome do livro"}' http://localhost:5000/books

>>> export book_id=<id gerado>
```

## Criar primeiro parágrafo
```
curl -X POST -H "Content-Type: application/json" -d '{"text": "Texto do primeiro parágrafo na posição 1", "position": 1}' http://localhost:5000/books/$book_id/paragraphs

>>> export paragraph_id=<id gerado>
```

## Criar segundo parágrafo
```
curl -X POST -H "Content-Type: application/json" -d '{"text": "Texto do segundo parágrafo na posição 1", "position": 1}' http://localhost:5000/books/$book_id/paragraphs
```

## Votar no primeiro parágrafo
```
curl -X POST http://localhost:5000/paragraphs/$paragraph_id/votes
```

## Listar livro
```
curl -X GET http://localhost:5000/books/$book_id
```