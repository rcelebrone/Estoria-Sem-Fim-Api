from flask import Flask, jsonify, request
from uuid import uuid4

app = Flask(__name__)
books = {}

@app.route('/books', methods=['POST'])
def create_book():
    book_id = str(uuid4())
    name = request.json.get('name')
    if not name:
        return 'Nome do livro é obrigatório', 400
    books[book_id] = {'id': book_id, 'name': name, 'paragraphs': []}
    return jsonify({'book_id': book_id}), 201

@app.route('/books/<book_id>/paragraphs', methods=['POST'])
def create_paragraph(book_id):
    book = books.get(book_id)
    if not book:
        return 'Livro não encontrado', 404
    
    paragraph_id = str(uuid4())
    text = request.json.get('text')
    if not text or len(text) > 300:
        return 'Texto inválido', 400
    
    position = request.json.get('position')
    if not position:
        return 'Posição é obrigatória', 400
    
    paragraph = {'id': paragraph_id, 'text': text, 'votes': 0, 'position': position}
    book['paragraphs'].append(paragraph)
    return jsonify({'paragraph_id': paragraph_id}), 201

@app.route('/paragraphs/<paragraph_id>/votes', methods=['POST'])
def vote(paragraph_id):
    for book in books.values():
        for paragraph in book['paragraphs']:
            if paragraph['id'] == paragraph_id:
                paragraph['votes'] += 1
                return jsonify({'votes': paragraph['votes']}), 200
    return 'Parágrafo não encontrado', 404

@app.route('/books/<book_id>', methods=['GET'])
def list_book(book_id):
    book = books.get(book_id)
    if not book:
        return 'Livro não encontrado', 404
    
    result = {}
    for p in book['paragraphs']:
        if p['position'] not in result:
            result[p['position']] = p
        else:
            if p['votes'] > result[p['position']]['votes']:
                result[p['position']] = p
    
    filtered_paragraphs = [result[key] for key in sorted(result.keys())]
    
    return jsonify({'name': book['name'], 'paragraphs': filtered_paragraphs})