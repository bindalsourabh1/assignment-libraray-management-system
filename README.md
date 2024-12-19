# Library Management System API

---

## Overview

This project is a Flask-based REST API for a Library Management System. It provides endpoints for managing books and includes features such as:  
1. **CRUD Operations**: Create, Read, Update, and Delete books.  
2. **Search Functionality**: Search for books by title or author.  
3. **Pagination**: Efficiently fetch books in chunks with offset and limit parameters.  
4. **Token-Based Authentication**: Secure API endpoints with a custom token mechanism.

---

## How to Run the Project

### Prerequisites
1. Python 3.10+ installed on your system.
2. Basic understanding of command-line tools.

### Steps to Set Up
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/bindalsourabh1/assignment-libraray-management-system.git
   cd assignment-libraray-management-system

## Getting Started

Set up your development environment:

```bash
# Create a virtual environment
python -m venv .venv

# Activate it (choose based on your OS)
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize DB
python database.py
```

Start the server:
```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000`

## Authentication 

Generate an authentication token before accessing the API:

```http
POST /auth/token
```
Request body:
```json
{
    "user": "your_username"
}
```

The returned token is required for all subsequent API calls.

## API Endpoints

### Create Book
```http
POST /books
```

Request body:
```json
{
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "published_date": "1937-09-21"
}
```

### List Books
```http
GET /books
```

Available query parameters:
- `search`: Filter books by title or author
- `offset`: Pagination offset (default: 0)
- `limit`: Results per page (default: 10)

### Update Book
```http
PUT /books/<book_id>
```

Request body:
```json
{
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "published_date": "1937-09-21",
    "is_available": true
}
```

### Delete Book
```http
DELETE /books/<book_id>
```

## Design Choices

### Framework
Flask was chosen for its simplicity and suitability for small-scale RESTful APIs.

### Database
SQLite was selected for its ease of use in development and testing environments.

### Authentication
A lightweight token-based authentication mechanism was implemented using simple string tokens for user verification.

### Pagination
Offset and limit parameters were added to ensure scalability for large datasets.

### Modular Structure
The project is divided into distinct modules:
- `app.py`: Contains the main Flask application
- `models.py`: Handles database models and operations
- `auth.py`: Manages authentication logic

## Assumptions and Limitations

### Assumptions
- Users must generate a token before accessing authenticated endpoints
- The token mechanism is basic and suited for demonstration purposes
- Search functionality only looks for exact matches in book titles or authors

### Limitations
- **Security**: Tokens are basic and unencrypted. We can use JWT for secure production environments.
- **Concurrency**: SQLite is ideal for development but unsuitable for high-concurrency production use.
- **HTTPS**: The API lacks SSL; deploy behind a secure server for encrypted communication.