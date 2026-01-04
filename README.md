# 🤖 AI Chat Assistant with RAG

<div align="center">

![AI Chat](https://img.shields.io/badge/AI-Chat%20Assistant-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?style=for-the-badge&logo=flask)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD700?style=for-the-badge&logo=huggingface&logoColor=white)

**An intelligent conversational AI powered by Retrieval-Augmented Generation (RAG)**

*Ask questions and get accurate answers with contextual understanding*

[Features](#-features) • [Quick Start](#-quick-start) • [API Reference](#-api-reference)

</div>

---

## 📋 Overview

AI Chat Assistant is a lightweight yet powerful chatbot application that leverages HuggingFace's multilingual E5 model for semantic search and text processing. It implements a RAG (Retrieval-Augmented Generation) system to provide contextually relevant responses based on pre-processed text chunks stored in ChromaDB.

### ✨ Key Features

- 🌍 **Multilingual Support** - Powered by intfloat/multilingual-e5-base model
- 🔍 **Semantic Search** - Efficient vector similarity search with ChromaDB
- 📝 **Text Processing** - Processes plain text documents from documents.txt
- ⚡ **Fast & Lightweight** - Optimized for performance with minimal dependencies

---

## 🏗️ Architecture

```
┌─────────────┐     ┌─────────────┐
│   User      │     │   Web UI    │
│   Interface │◄───►│   (HTML/JS) │
└─────────────┘     └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐     ┌──────────────┐
                    │   Flask     │     │   ChromaDB   │
                    │   Server    │◄───►│   Vector     │
                    └──────┬──────┘     │   Store      │
                           │            └──────────────┘
                           ▼
                    ┌─────────────┐
                    │ GitHub Models│
                    │ via Azure AI │
                    │  (gpt-4.1)   │
                    └─────────────┘
```

---

## 🛠️ Tech Stack

### Backend
- **Flask** - Lightweight web framework
- **HuggingFace Transformers** - For text embeddings using multilingual-e5-base
- **ChromaDB** - Vector database for efficient similarity search
- **Python-dotenv** - Environment variable management
- **sentence-transformers** - For efficient text embeddings

### Frontend
- **HTML5 / JavaScript** - Simple and responsive interface
- **Basic Styling** - Clean and minimal design

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- ChromaDB (local or remote instance)
- HuggingFace account (for model access)

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd RAG-PgVectorScale-Backend-main
```

2. **Create virtual environment**
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Prepare your documents**

Place your text content in `services/documents.txt`. Each line should be a separate document chunk.

5. **Set up ChromaDB**

The application will automatically create a ChromaDB instance in the `./chroma_db` directory when you first run it.

6. **Start the server**

```bash
python server.py
```

The application will be available at `http://localhost:5000`

---

## 📁 Project Structure

```
RAG-PgVectorScale-Backend/
├── agents/                      # AI agent implementation
│   ├── __init__.py
│   ├── index.py                # Main RAG implementation
│   ├── prompt.py               # System prompts
│   └── embeddings.py           # Embedding utilities
├── controllers/                # Request handlers
│   └── agents.py               # API endpoints
├── routes/                     # API routes
│   └── agents.py               # Route definitions
├── services/                   # Core services
│   ├── chunks.py               # Text processing
│   └── rag_creation.py         # RAG setup and initialization
├── static/                     # Static files
├── views/                      # Frontend templates
│   └── index.html              # Chat interface
├── server.py                   # Flask application entry point
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables
└── README.md                   # This file
```

---

## 🌐 API Reference

### POST /conversation

Send a message to the chat and get a response. The system will find the most relevant text chunks from your documents and use them to generate a response.

**Request Body:**
```json
{
    "query": "Your question here"
}
```

**Response:**
```json
{
    "response": "The AI's response based on the most relevant document chunks"
}
```

---

## 🔧 Configuration

The application can be configured using the following:

1. **Environment Variables**:
   - `FLASK_ENV`: Set to 'development' for debug mode (default: 'production')

2. **Model Configuration** (in `agents/embeddings.py`):
   - `model_name`: Currently set to "intfloat/multilingual-e5-base"
   - `encode_kwargs`: Normalization settings for embeddings

3. **Text Processing** (in `services/chunks.py`):
   - Chunk size and overlap settings
   - Text cleaning and preprocessing

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services/) for the powerful AI capabilities
- [ChromaDB](https://www.trychroma.com/) for the vector database
- [Flask](https://flask.palletsprojects.com/) for the web framework

## ⚙️ Configuration

### Chunk Size Optimization

The default configuration uses:
- **Chunk size**: 400 characters
- **Chunk overlap**: 50 characters

Adjust in `services/chunks.py`:
```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,      # Increase for longer context
    chunk_overlap=50,    # Increase for more context continuity
)
```

### Embedding Model

Default: `text-embedding-3-small` (1536 dimensions)

To change, update in `services/rag_creation.py`:
```python
model = "text-embedding-3-large"  # Higher quality, more expensive
```

### Chat Model

Default: `gpt-4o-mini`

To change, update in `agents/index.py`:
```python
model = "gpt-4o"  # More capable, higher cost
```

---

## 🔌 API Reference

### POST `/api/agents/conversation`

Send a message to the AI assistant.

**Request:**
```json
{
  "query": "What is artificial intelligence?"
}
```

**Response:**
```json
{
  "response": "Artificial intelligence (AI) is...",
  "status": "success",
  "code": 200
}
```

**Error Response:**
```json
{
  "error": "Error message",
  "status": "error",
  "code": 500
}
```

---

## 🎨 UI Features

### Design System
- **Color Scheme**: Black and Stone (inspired by shadcn/ui)
- **Typography**: System fonts with optimized readability
- **Animations**: Smooth transitions and loading states
- **Responsive**: Works on desktop, tablet, and mobile

### User Experience
- ✅ Real-time typing indicators
- ✅ Smooth message animations
- ✅ Auto-scrolling to latest message
- ✅ Error handling with user-friendly messages
- ✅ Keyboard shortcuts (Enter to send)
- ✅ Disabled state during API calls

---

## 📊 How RAG Works

1. **Document Ingestion**
   - PDFs are converted to images
   - Gemini Vision extracts text via OCR
   - Text is split into semantic chunks

2. **Embedding Generation**
   - Each chunk is embedded using OpenAI's embedding model
   - Embeddings (vectors) are stored in PostgreSQL with metadata

3. **Query Processing**
   - User query is embedded using the same model
   - Vector similarity search finds top-k relevant chunks
   - Retrieved context is added to the conversation

4. **Response Generation**
   - GPT model receives: system prompt + conversation history + retrieved context
   - Generates contextually accurate response
   - Response is stored in conversation history

---

## 🔧 Troubleshooting

### Common Issues

**1. "Extension vectorscale is not available"**
- Solution: Use pgvector instead of TimescaleDB vectorscale
- Run: `CREATE EXTENSION IF NOT EXISTS vector;` in your database

**2. "No module named 'pdf2image'"**
- Solution: Install Poppler (see installation steps)

**3. "API key not found"**
- Solution: Ensure `.env` file exists with correct keys

**4. "Connection refused to database"**
- Solution: Check `TIMESCALE_SERVICE_URL` in `.env`

**5. Slow response times**
- Solution: Reduce chunk_size or limit the number of retrieved embeddings

---

## 🚢 Deployment

### Railway

1. Connect your GitHub repository to Railway
2. Add environment variables in Railway dashboard
3. Deploy automatically on push

### Docker (Optional)

```dockerfile
FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8080

CMD ["python", "server.py"]
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services/) for the powerful AI capabilities
- [ChromaDB](https://www.trychroma.com/) for the vector database
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [LangChain](https://langchain.com/) for document processing utilities
- [TimescaleDB](https://www.timescale.com/) / [pgvector](https://github.com/pgvector/pgvector) for vector storage

---

## 📧 Contact & Support

For questions, issues, or suggestions:
- 🐛 Report bugs via [Issues](../../issues)
- 💡 Request features via [Discussions](../../discussions)
- 📧 Email: your-email@example.com

---

<div align="center">

**Built with ❤️ using Python, Flask, and OpenAI**

⭐ Star this repo if you find it helpful!

</div>

#   R A G - c h r o m a _ d b - B a c k e n d - m a i n  
 