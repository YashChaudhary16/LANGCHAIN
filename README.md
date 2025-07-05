# LangChain AI Assistant Suite

A comprehensive AI assistant suite featuring multiple interfaces and models including Claude 3.5 Haiku, local Ollama models, and a REST API server.

## Features

- 🤖 **Multiple AI Models**: Claude 3.5 Haiku (cloud) and Gemma3 (local via Ollama)
- 💬 **Chat-like Interface**: Clean, modern UI similar to ChatGPT
- 🧠 **Conversation Memory**: Remembers context from previous messages
- ⚙️ **Adjustable Settings**: Control temperature and max tokens
- 📱 **Responsive Design**: Works on desktop and mobile
- 🎨 **Beautiful UI**: Custom styling with modern design
- 🌐 **REST API Server**: FastAPI-based server for programmatic access
- 🖥️ **Local LLM Support**: Run models locally with Ollama

## Project Structure

```
LANGCHAIN/
├── chatbot/
│   ├── app.py              # Claude 3.5 Haiku Streamlit app
│   ├── locallama.py        # Local Ollama Streamlit app
│   ├── .env                # Environment variables
│   └── requirements.txt    # Python dependencies
├── API/
│   ├── app.py              # FastAPI server with multiple endpoints
│   ├── client.py           # Streamlit client for API testing
│   └── .env                # API environment variables
├── requirements.txt        # Main project dependencies
└── README.md              # This file
```

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Environment Variables

#### For Chatbot Applications
Create `.env` files in both `chatbot/` and `API/` directories:

**chatbot/.env:**
```env
LANGSMITH_API_KEY="your_langsmith_api_key"
LANGSMITH_PROJECT="Langchain_Tutorial_1"
ANTHROPIC_API_KEY="your_anthropic_api_key"
```

**API/.env:**
```env
ANTHROPIC_API_KEY="your_anthropic_api_key"
```

### 3. Install Ollama (for Local Models)

#### Windows
1. Download Ollama from [ollama.ai](https://ollama.ai)
2. Run the installer and follow the setup wizard
3. Open PowerShell and run:
```bash
ollama pull gemma3
```

#### macOS
```bash
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull gemma3
```

#### Linux
```bash
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull gemma3
```

### 4. Start Ollama Service
```bash
ollama serve
```

## Running the Applications

### Option 1: Claude 3.5 Haiku Chatbot
```bash
cd chatbot
python -m streamlit run app.py
```
Access at: `http://localhost:8501`

### Option 2: Local Ollama Chatbot
```bash
cd chatbot
python -m streamlit run locallama.py
```
Access at: `http://localhost:8501`

### Option 3: API Server + Client
1. **Start the API server:**
```bash
cd API
python app.py
```
Server runs at: `http://localhost:8000`

2. **Start the API client:**
```bash
cd API
python -m streamlit run client.py
```
Access at: `http://localhost:8501`

## API Endpoints

The FastAPI server provides the following endpoints:

- `POST /anthropic` - Direct Claude 3.5 Haiku access
- `POST /paid` - Claude 3.5 Haiku with topic explanation prompt
- `POST /free` - Local Gemma3 with poetry prompt
- `GET /docs` - Interactive API documentation

### Example API Usage
```bash
# Get paid response (Claude)
curl -X POST "http://localhost:8000/paid/invoke" \
     -H "Content-Type: application/json" \
     -d '{"input": {"topic": "artificial intelligence"}}'

# Get free response (Gemma3)
curl -X POST "http://localhost:8000/free/invoke" \
     -H "Content-Type: application/json" \
     -d '{"input": {"topic": "nature"}}'
```

## Usage

### Claude Chatbot (app.py)
1. **Start a Conversation**: Type your message in the input box
2. **Adjust Settings**: Use the sidebar to modify temperature and max tokens
3. **Clear History**: Click the "Clear Chat History" button to start fresh

### Local LLM Chatbot (locallama.py)
1. **Simple Interface**: Type your question and get responses from local Gemma3 model
2. **No API Keys Required**: Works completely offline once Ollama is set up
3. **Fast Responses**: Local processing for quick interactions

### API Client (client.py)
1. **Test API Endpoints**: Use the web interface to test both paid and free endpoints
2. **Topic Input**: Enter any topic to get AI-generated responses
3. **Real-time Testing**: See API responses immediately

## Configuration

### Temperature
- **Lower values (0.0-0.3)**: More focused, deterministic responses
- **Higher values (0.7-1.0)**: More creative, varied responses

### Max Tokens
- Controls the maximum length of AI responses
- Range: 100-2000 tokens

### Ollama Models
- **gemma3**: Fast, efficient local model
- **Other models**: Pull additional models with `ollama pull <model-name>`

## Troubleshooting

### Common Issues

1. **API Key Error**: Make sure your `ANTHROPIC_API_KEY` is correctly set in the `.env` files
2. **Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
3. **Port Issues**: If ports are busy, applications will automatically use the next available port
4. **Ollama Not Found**: Make sure Ollama is installed and running (`ollama serve`)
5. **Model Not Found**: Pull the required model with `ollama pull gemma3`

### Streamlit Command Issues (Windows)
If `streamlit` command is not recognized, use:
```bash
python -m streamlit run <filename>
```

### Getting API Keys

- **Anthropic API Key**: Sign up at [console.anthropic.com](https://console.anthropic.com)
- **LangSmith API Key**: Sign up at [smith.langsmith.com](https://smith.langsmith.com)

### Ollama Troubleshooting

1. **Service Not Running**: Start with `ollama serve`
2. **Model Download Issues**: Check internet connection and try `ollama pull gemma3` again
3. **Permission Issues**: Run as administrator (Windows) or use `sudo` (Linux/macOS)

## Technologies Used

- **Streamlit**: Web application framework
- **FastAPI**: High-performance API framework
- **LangChain**: LLM framework and conversation management
- **Anthropic Claude**: Cloud-based large language model
- **Ollama**: Local LLM framework
- **Python-dotenv**: Environment variable management
- **Uvicorn**: ASGI server for FastAPI

## License

This project is open source and available under the MIT License. 