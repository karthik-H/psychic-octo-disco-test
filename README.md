# User Directory Application

This project provides a production-ready, full-stack solution for viewing user data in a table format. It consists of a Python backend and a React TypeScript frontend, following clean architecture and industry best practices.

---

## Features

- **Backend**: Python (Flask), clean architecture, fetches users from JSONPlaceholder, exposes `/users` API, CORS enabled, config via `.env`.
- **Frontend**: React + TypeScript, modular, displays all user fields in a readable table, error/loading handling, config via `.env`.

---

## Prerequisites

- Python 3.8+
- Node.js 18+
- npm 9+
- (Recommended) Use a virtual environment for Python

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repo-url>
cd <repo-directory>
```

### 2. Backend Setup

```bash
# Create and activate a virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env  # or edit .env as needed

# Start the backend server
python -m app.api.server
```

The backend will run on `http://localhost:5000` by default.

### 3. Frontend Setup

```bash
cd frontend
npm install
cp .env.example .env  # or edit .env as needed
npm start
```

The frontend will run on `http://localhost:3000` by default.

---

## Configuration

- All environment variables are managed in `.env` files for both backend and frontend.
- Update `FRONTEND_ORIGIN` in the backend `.env` to match your frontend URL for CORS.
- Update `REACT_APP_API_URL` in the frontend `.env` to match your backend API URL.

---

## Usage

- Open your browser at `http://localhost:3000`
- The UI will display all users in a table with the following fields:
  - id, name, username, email, phone, website, address, company

---

## Folder Structure

```
.
├── app/
│   ├── api/
│   │   └── server.py
│   ├── config/
│   ├── controller/
│   ├── domain/
│   ├── repository/
│   └── service/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── UserTable.tsx
│   │   │   └── LoadingError.tsx
│   │   └── App.tsx
│   └── .env
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Notes

- Do **not** commit `.env` files with secrets.
- All dependencies are up to date as of project creation.
- For production, use a proper WSGI server (e.g., gunicorn) and a production-ready Node build.

---

## Troubleshooting

- If you encounter CORS issues, ensure the backend `.env` `FRONTEND_ORIGIN` matches your frontend URL.
- If ports are in use, update the `.env` files accordingly.

---

## License

MIT