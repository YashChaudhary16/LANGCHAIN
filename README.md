# Claude Chat Assistant

A simple Streamlit dashboard with a ChatGPT-like interface using LangChain and Claude 3.5 Haiku model.

## Features

- 🤖 **Claude 3.5 Haiku Integration**: Powered by Anthropic's latest model
- 💬 **Chat-like Interface**: Clean, modern UI similar to ChatGPT
- 🧠 **Conversation Memory**: Remembers context from previous messages
- ⚙️ **Adjustable Settings**: Control temperature and max tokens
- 📱 **Responsive Design**: Works on desktop and mobile
- 🎨 **Beautiful UI**: Custom styling with modern design

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Environment Variables

Make sure your `.env` file contains the following variables:

```env
LANGSMITH_API_KEY="your_langsmith_api_key"
LANGSMITH_PROJECT="Langchain_Tutorial_1"
ANTHROPIC_API_KEY="your_anthropic_api_key"
```

### 3. Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## Usage

1. **Start a Conversation**: Type your message in the input box and press Enter or click Send
2. **Adjust Settings**: Use the sidebar to modify temperature and max tokens
3. **Clear History**: Click the "Clear Chat History" button to start fresh
4. **View Information**: Check the sidebar for model information and instructions

## Configuration

### Temperature
- **Lower values (0.0-0.3)**: More focused, deterministic responses
- **Higher values (0.7-1.0)**: More creative, varied responses

### Max Tokens
- Controls the maximum length of Claude's responses
- Range: 100-2000 tokens

## Troubleshooting

### Common Issues

1. **API Key Error**: Make sure your `ANTHROPIC_API_KEY` is correctly set in the `.env` file
2. **Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
3. **Port Issues**: If port 8501 is busy, Streamlit will automatically use the next available port

### Getting API Keys

- **Anthropic API Key**: Sign up at [console.anthropic.com](https://console.anthropic.com)
- **LangSmith API Key**: Sign up at [smith.langchain.com](https://smith.langchain.com)

## File Structure

```
chatbot/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not in repo)
└── README.md          # This file
```

## Technologies Used

- **Streamlit**: Web application framework
- **LangChain**: LLM framework and conversation management
- **Anthropic Claude**: Large language model
- **Python-dotenv**: Environment variable management

## License

This project is open source and available under the MIT License. 