# User Directory Application

This project provides a production-ready, clean-architecture implementation for browsing user data in a table format. It consists of a Python Flask backend and a React TypeScript frontend.

---

## Folder Structure

- `app/` - Backend (Flask, Clean Architecture)
- `frontend/` - Frontend (React, TypeScript, Clean Structure)
- `.env` - Backend environment variables
- `frontend/.env` - Frontend environment variables

---

## Prerequisites

- Python 3.8+
- Node.js 18+ and npm 9+
- (Recommended) Use a Python virtual environment

---

## Backend Setup

1. **Install dependencies:**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

2. **Configure environment:**
   - Edit `.env` for backend settings (API base URL, CSV path, port, CORS origin).

3. **Run the backend server:**
   ```bash
   python -m app.api.server
   ```
   The backend will start on the port specified in `.env` (default: 5001).

---

## Frontend Setup

1. **Install dependencies:**
   ```bash
   npm install --prefix frontend
   ```

2. **Configure environment:**
   - Edit `frontend/.env` to set the backend API URL (must match backend port and CORS origin).

3. **Run the frontend:**
   ```bash
   npm start --prefix frontend
   ```
   The frontend will start on [http://localhost:3000](http://localhost:3000) by default.

---

## Environment Variables

### Backend (`.env`)
- `JSONPLACEHOLDER_BASE_URL` - Upstream API base URL
- `USER_CSV_PATH` - Path for CSV export
- `BACKEND_PORT` - Backend server port (default: 5001)
- `FRONTEND_ORIGIN` - Allowed frontend origin for CORS

### Frontend (`frontend/.env`)
- `REACT_APP_API_URL` - Backend API URL (e.g., `http://localhost:5001`)

---

## Usage

- Open [http://localhost:3000](http://localhost:3000) in your browser.
- The UI displays all user data in a table, with columns for all required fields.
- The backend fetches user data from JSONPlaceholder and exposes it at `/users`.

---

## Linting & Style

- Python: [PEP8](https://pep8.org/) (use `flake8` for linting)
- TypeScript/React: [Airbnb React/JSX Style Guide](https://github.com/airbnb/javascript/tree/master/react) (use `eslint`)

---

## Notes

- All configuration is managed via `.env` files.
- No sensitive data is committed.
- CORS is configured for local development.
- All dependencies are up to date as of project setup.

---

## Troubleshooting

- If you see CORS or network errors, ensure both backend and frontend are running and the ports/origins match in `.env` files.
- For dependency issues, run `pip install --upgrade -r requirements.txt` and `npm install --prefix frontend`.

---

## Test & Export

- Backend includes test scripts in `tests/`.
- User data can be exported to CSV via the backend.

---

## Clean Architecture

- Backend: Controller → Service → Domain → Repository
- Frontend: Components are modular and reusable.

---

## License

MIT License