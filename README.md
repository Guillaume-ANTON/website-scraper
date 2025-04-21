# 📰 Website Scraper API

A modern, asynchronous Python API that scrapes [Hacker News](https://news.ycombinator.com), stores article titles in a SQLite database, and exposes them through a REST API built with FastAPI.  
Includes testing with `pytest`, automation with a custom `run.sh` script, and clean project structure ready for CI and containerization.

---

## 🚀 Features

- ⚡️ Asynchronous web scraping using `aiohttp` + `BeautifulSoup`
- 🔌 REST API with FastAPI & Pydantic
- 📓 SQLite database via SQLAlchemy
- 🔀 Automatic scraping on server startup
- 🧲 Unit-tested with `pytest` and `httpx`
- 🔧 Shell script to activate venv and launch the app easily
- 🧱 Modular architecture (scraper, routes, models, database)

---

## 📁 Project Structure

```
website-scraper/
├── app/
│   ├── main.py            # FastAPI entrypoint
│   ├── scraper.py         # Async scraper
│   ├── routes.py          # API routes
│   ├── models.py          # SQLAlchemy models
│   ├── schemas.py         # Pydantic schemas
│   ├── database.py        # DB setup
│   └── __init__.py
├── tests/
│   └── test_api.py        # Unit tests for the API
├── run.sh                 # Script to activate venv and start API
├── test.sh                # Script to run tests with PYTHONPATH
├── requirements.txt       # Dependencies
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Guillaume-ANTON/website-scraper.git
cd website-scraper
```

### 2. Create & activate the virtual environment (Python 3.11 recommended)

```bash
/opt/homebrew/bin/python3.11 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the server

```bash
./run.sh
```

Server runs at: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
Swagger docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧲 Running Tests

```bash
PYTHONPATH=. pytest
```

Or use the optional `test.sh` if created.

---

## 📬 API Endpoints

| Method | Endpoint        | Description               |
|--------|-----------------|---------------------------|
| GET    | `/articles`     | List all scraped articles |
| POST   | `/articles`     | Add a new article manually|

---

## ✅ Example Response

```json
[
  {
    "id": 1,
    "title": "Stripe launches new API for global payments"
  },
  {
    "id": 2,
    "title": "GitHub Copilot gets real-time code explanation feature"
  }
]
```

---

## 💡 To Improve

- [ ] Add authentication
- [ ] Switch to PostgreSQL with Docker
- [ ] Deploy with Render or Railway
- [ ] Add GitHub Actions CI
- [ ] Add export endpoints (.csv, .json)

---

## 📄 License

MIT — Feel free to use and modify.

---

> Built with ❤️ by [Guillaume Anton](https://github.com/Guillaume-ANTON)
