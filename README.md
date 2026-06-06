# 🧠 Synthiq

> *Turn any webpage into instant knowledge.*

Synthiq is a production-grade AI knowledge extraction system that fetches any webpage, understands its content, and automatically generates high-quality question and answer pairs — transforming hours of manual work into seconds of automated intelligence.

---

## 🚀 Demo

```bash
python3 -m src.cli "https://en.wikipedia.org/wiki/Artificial_intelligence" --max-chunks 5
```

```
📥 Fetching content from: https://en.wikipedia.org/wiki/Artificial_intelligence
✅ Fetched 85,000 characters
✂️  Splitting into chunks...
✅ Created 57 chunks
🤖 Generating Q&A for 5 chunks...

=== Q&A PAIRS ===

Q1: What is Artificial Intelligence?
A1: AI is the simulation of human intelligence by machines...

Q2: Who coined the term Artificial Intelligence?
A2: John McCarthy coined the term in 1956...
```

---

## ✨ Features

- 🌐 **Web Scraper** — Fetches and cleans content from any URL
- ✂️ **Smart Chunker** — Splits large documents into digestible pieces
- 🤖 **AI Generator** — Produces meaningful Q&A pairs using LLaMA 3.1
- 💾 **JSON Export** — Save results to a file for further use
- 💻 **CLI Interface** — Simple command line tool, ready to use
- ⚡ **Fast** — Processes hundreds of pages in seconds

---

## 🏗️ Project Structure

```
synthiq/
├── src/
│   ├── __init__.py          # Package entry point
│   ├── bot.py               # Pipeline manager (orchestrates everything)
│   ├── models.py            # Data blueprints (Pydantic models)
│   ├── client.py            # AI brain (Groq/LLaMA integration)
│   ├── decoder_client.py    # Web scraper (fetches URLs)
│   ├── cli.py               # Command line interface
│   └── processors/
│       └── __init__.py      # Text chunking processor
├── .env                     # API keys (never commit this!)
├── main.py                  # Main entry point
└── requirements.txt         # Dependencies
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.10+ |
| AI Model | LLaMA 3.1 via Groq API |
| Web Scraping | BeautifulSoup4 + Requests |
| Data Validation | Pydantic |
| CLI | Typer |
| Config | python-dotenv |

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/synthiq.git
cd synthiq
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key
Get a free API key from [console.groq.com](https://console.groq.com) — no credit card needed.

```bash
cp .env.example .env
nano .env
```

Add your key:
```
GROQ_API_KEY=your_api_key_here
```

---

## 💻 Usage

### Basic usage
```bash
python3 -m src.cli "https://en.wikipedia.org/wiki/Python_(programming_language)"
```

### Control how many chunks to process
```bash
python3 -m src.cli "https://en.wikipedia.org/wiki/Machine_learning" --max-chunks 10
```

### Save results to a JSON file
```bash
python3 -m src.cli "https://en.wikipedia.org/wiki/Machine_learning" --max-chunks 5 --output-file results.json
```

### Example JSON output
```json
{
  "source": "https://en.wikipedia.org/wiki/Machine_learning",
  "status": "completed",
  "total_qa_pairs": 15,
  "qa_pairs": [
    {
      "question": "What is machine learning?",
      "answer": "Machine learning is a subset of AI that enables systems to learn from data."
    }
  ]
}
```

---

## 🎯 Use Cases

| Use Case | Description |
|----------|-------------|
| 📚 Study Tool | Feed it textbooks or articles → get instant quiz questions |
| 🏢 Chatbot Training | Feed it company docs → generate training data for support bots |
| 🎓 E-Learning | Feed it lessons → auto-generate exam questions |
| 📰 Research | Feed it papers → extract and structure key facts |
| 🔧 FAQ Generator | Feed it product docs → create FAQs automatically |

---

## 🗺️ How It Works

```
Input URL
    │
    ▼
🌐 DecoderClient      →  Fetches and cleans webpage content
    │
    ▼
✂️  TextProcessor      →  Splits content into overlapping chunks
    │
    ▼
🤖 AIClient           →  Generates Q&A pairs for each chunk
    │
    ▼
📦 Bot                →  Orchestrates the full pipeline
    │
    ▼
💾 Output (CLI/JSON)  →  Displays or saves results
```

---

## 🔧 Configuration

| Option | Default | Description |
|--------|---------|-------------|
| `--max-chunks` | 5 | Number of text chunks to process |
| `--output-file` | None | Path to save JSON results |
| `chunk_size` | 300 | Words per chunk (in processors/) |
| `overlap` | 30 | Overlapping words between chunks |

---

## 📋 Requirements

```
groq
pydantic
python-dotenv
typer
requests
beautifulsoup4
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open an issue for bugs or feature requests
- Submit a pull request with improvements
- Star the repo if you find it useful ⭐

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Built with ❤️ using Python and Groq AI.

---

## 🙏 Acknowledgements

- [Groq](https://groq.com) for the free and fast LLaMA API
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for web scraping
- [Pydantic](https://docs.pydantic.dev) for data validation
- [Typer](https://typer.tiangolo.com) for the CLI interface
