# AI Research Agent

A Python research assistant built with LangChain and Google Gemini. It uses web search and Wikipedia tools to help answer research questions with structured outputs.

## Features
- Google Gemini integration
- DuckDuckGo web search
- Wikipedia search
- Structured responses using Pydantic

## Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Google API key:

```env
GOOGLE_API_KEY=your_api_key
```

## Run

```bash
python main.py
```
