from flask import Flask, jsonify, abort, request

app = Flask(__name__)

quotes = [
    {
        "id": 1,
        "quote": "I'm gonna make him an offer he can't refuse.",
        "movie": "The Godfather",
    },
    {
        "id": 2,
        "quote": "Get to the choppa!",
        "movie": "Predator",
    },
    {
        "id": 3,
        "quote": "Nobody's gonna hurt anybody. We're gonna be like three little Fonzies here.",  # noqa E501
        "movie": "Pulp Fiction",
    },
]


def _get_quote(qid):
    """Recommended helper"""
    for quote in quotes:
        if quote['id'] == qid:
            return quote


@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    return jsonify(quotes=quotes)


@app.route('/api/quotes/<int:qid>', methods=['GET'])
def get_quote(qid):
    quote = _get_quote(qid)
    if quote is None:
        abort(404)
    return jsonify(quotes=[quote])


@app.route('/api/quotes', methods=['POST'])
def create_quote():
    quote = request.get_json()
    # Check for empty data
    if quote == {}:
        abort(400)
    # Assign an id
    ids = [quote['id'] for quote in quotes]
    max_id = max(ids)
    quote['id'] = max_id + 1
    # Check for missing data
    if len(quote.keys()) != 3:
        abort(400)
    # Check if quote already exists
    cur_quotes = [q['quote'] for q in quotes]
    if quote['quote'] in cur_quotes:
        abort(400)
    # Add quote to quotes
    quotes.append(quote)

    return jsonify(quote=quote), 201


@app.route('/api/quotes/<int:qid>', methods=['PUT'])
def update_quote(qid):
    new_quote = request.get_json()
    # Check if no data
    if new_quote == {}:
        abort(400)
    # Check if quote exits
    ids = [quote['id'] for quote in quotes]
    if qid not in ids:
        abort(404)

    return jsonify(quote={
        'id': qid,
        'quote': new_quote['quote'],
        'movie': new_quote['movie']
    })


@app.route('/api/quotes/<int:qid>', methods=['DELETE'])
def delete_quote(qid):
    # Check if a quote exists to delete
    ids = [quote['id'] for quote in quotes]
    if qid not in ids:
        abort(404)
    quote_index = quotes.index(_get_quote(qid))
    del quotes[quote_index]

    return jsonify(quotes=quotes), 204
