<!-- # Naive-RAG: Implementation of Different RAG Approaches 🧠📚

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Last Commit](https://img.shields.io/github/last-commit/Shoshinmai/Naive-RAG)

A modular implementation of basic Retrieval-Augmented Generation (RAG) systems for educational purposes and experimentation.

![RAG Architecture Diagram](https://via.placeholder.com/800x400.png?text=RAG+Architecture+Diagram)

## Features ✨
- **Document Ingestion Pipeline** 📥
- **ChromaDB Persistent Storage** 🗄️
- **Basic Retrieval Mechanisms** 🔍
- **Language Model Integration** 🤖
- **News Article Processing** 📰
- **Modular Architecture** 🧩

## Quick Start 🚀

### Prerequisites
- Python 3.8+
- [Poetry](https://python-poetry.org/) (recommended)
- OpenAI API key

### Installation
```bash
git clone https://github.com/Shoshinmai/Naive-RAG.git
cd Naive-RAG

# Using poetry
poetry install

# Alternative using pip
pip install -r requirement.txt
```

### Configuration
Create `.env` file:
```ini
OPENAI_API_KEY=your-api-key-here
CHROMA_PERSIST_DIR=./chroma_persistent_storage
```

### Usage
```python
from app import NaiveRAG

# Initialize RAG system
rag = NaiveRAG()

# Ingest documents
rag.ingest_documents("./news_articles/")

# Query the system
response = rag.query("What's the latest technology news?")
print(response)
```

## Project Structure 🗂️
```
.
├── chroma_persistent_storage/   # Vector database storage
├── news_articles/               # Sample news articles
├── app.py                       # Main application logic
├── requirement.txt              # Dependencies
├── .gitignore
└── 1.5.2                        # Version-specific configurations
```

## Key Components 🔧
1. **Document Processing**:
   - Text extraction and chunking
   - Basic cleaning and normalization
   - Metadata tagging

2. **Vector Storage**:
   - ChromaDB persistent storage
   - Sentence embedding transformations
   - Metadata-aware indexing

3. **Retrieval System**:
   - Basic similarity search
   - Keyword-based filtering
   - Hybrid search strategies

## Dependencies 📦
| Package | Version | Purpose |
|---------|---------|---------|
| chromadb | 0.4.15 | Vector storage |
| langchain | 0.1.5 | Pipeline orchestration |
| openai | 1.5.2 | LLM integration |
| python-dotenv | 0.21.0 | Environment management |

## Roadmap 🗺️
- [ ] Add advanced retrieval strategies
- [ ] Implement evaluation metrics
- [ ] Support for multiple LLM providers
- [ ] Web interface integration

## Contributing 🤝
We welcome contributions! Please see our [Contribution Guidelines](CONTRIBUTING.md) for details.

## License 📄
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Maintainer**: [Shoshinmai](https://github.com/Shoshinmai)  
**Documentation**: [View Docs](https://github.com/Shoshinmai/Naive-RAG/wiki)
