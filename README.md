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

## Technical Details

### Framework
Flask was chosen for its minimalist approach and suitability for RESTful APIs.

### Database
SQLite is used for its:
- Simple setup process
- Zero-configuration nature
- Suitability for development and testing
- Self-contained database file

### Project Structure
- `app.py`: Main application logic and route handlers
- `models.py`: Database models and operations
- `auth.py`: Authentication implementation

## Limitations and Considerations

### Development Configuration
- Basic token-based authentication
- SQLite database (suitable for development)
- No SSL/TLS configuration

### Production Recommendations
- Implement proper JWT authentication
- Consider PostgreSQL for better concurrency
- Add SSL/TLS support
- Implement request rate limiting
- Add proper logging

## Future Development

Planned features:
- Advanced search capabilities
- Batch operations
- Data export/import functionality
- User roles and permissions
