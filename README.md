# User Information Fetcher

This application fetches user information from the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/users) in a production-ready, modular, and testable manner using Python and clean architecture principles.

## Features

- Fetches and parses all user data from the public JSONPlaceholder API
- Clean, layered architecture (controller → service → repository → domain)
- Environment-based configuration management
- Graceful error handling and logging
- Easily extensible and testable
- **Exports all user data to a CSV file, with all fields (including nested) flattened for compatibility with spreadsheet software**

## Folder Structure

```
app/
  ├── config/           # Configuration loader
  ├── controller/       # Entrypoint/controller
  ├── domain/           # Domain models
  ├── repository/       # API communication and CSV persistence
  ├── service/          # Business logic
tests/                  # Unit tests
.env                    # Environment variables
requirements.txt        # Python dependencies
.gitignore              # Git ignore rules
```

## Setup & Run Instructions

1. **Clone the repository**

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Edit the `.env` file if you need to change the API base URL or CSV output path (defaults are set).

5. **Run the application:**
   ```bash
   python app/controller/main.py
   ```
   - This will fetch all users from the API and export them to a CSV file at the path specified by `USER_CSV_PATH` in your `.env` (default: `output/users.csv`).

6. **Run tests:**
   ```bash
   pytest
   ```

## Environment Variables

- `JSONPLACEHOLDER_BASE_URL` (default: `https://jsonplaceholder.typicode.com`)
- `USER_CSV_PATH` (default: `output/users.csv`)

## Output

- The CSV file will contain all user fields, including nested fields (e.g., `address.street`, `address.geo.lat`, `company.name`), as columns.
- The CSV is compatible with Microsoft Excel, Google Sheets, and other spreadsheet software.

## Notes

- No authentication is required for the API.
- All configuration is managed via `.env` and environment variables.
- The application handles network errors and invalid responses gracefully.
- The codebase follows PEP8 and clean architecture best practices.

## License

MIT