from flask import Flask, request, jsonify
from models import Book
from auth import Auth

app = Flask(__name__)

# Token Authentication Decorator
def require_token(func):
    def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or not Auth.verify_token(token):
            return jsonify({"message": "Unauthorized"}), 401
        return func(*args, **kwargs)
    decorated_function.__name__ = func.__name__  # Preserve the original function name for Flask
    return decorated_function

# Health Check Endpoint
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Library Management System API is running."})

# Generate Token Endpoint
@app.route("/auth/token", methods=["POST"])
def get_token():
    user = request.json.get("user")
    if not user:
        return jsonify({"message": "User is required"}), 400
    token = Auth.generate_token(user)
    return jsonify({"token": token})

# Create Book Endpoint
@app.route("/books", methods=["POST"])
@require_token
def create_book():
    data = request.json
    if not data or not data.get("title") or not data.get("author"):
        return jsonify({"message": "Title and author are required."}), 400
    book_id = Book.create_book(data)
    return jsonify({"message": "Book created.", "book_id": book_id}), 201

# Get Books with Pagination and Search
@app.route("/books", methods=["GET"])
@require_token
def get_books():
    search = request.args.get("search")
    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", 10))
    books = Book.get_books(offset=offset, limit=limit, search=search)
    return jsonify(books)

# Update Book Endpoint
@app.route("/books/<int:book_id>", methods=["PUT"])
@require_token
def update_book(book_id):
    data = request.json
    if not data:
        return jsonify({"message": "No data provided to update."}), 400
    success = Book.update_book(book_id, data)
    if success:
        return jsonify({"message": "Book updated."})
    return jsonify({"message": "Book not found."}), 404

# Delete Book Endpoint
@app.route("/books/<int:book_id>", methods=["DELETE"])
@require_token
def delete_book(book_id):
    success = Book.delete_book(book_id)
    if success:
        return jsonify({"message": "Book deleted."})
    return jsonify({"message": "Book not found."}), 404

if __name__ == "__main__":
    app.run(debug=True)
