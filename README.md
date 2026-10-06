# Agentic Chatbot Evaluator

An agentic platform for automatically testing and evaluating conversational AI systems.

## Objective

The system takes an evaluation objective and:

1. Generates test scenarios
2. Simulates users
3. Interacts with a target chatbot
4. Evaluates chatbot responses
5. Evaluates complete scenarios
6. Aggregates results
7. Generates an evaluation report

## Architecture

React
    ↓
FastAPI
    ↓
LangGraph
    ↓
Planner / Simulator / Evaluator
    ↓
Target Chatbot

## Tech Stack

### Backend

- Python
- FastAPI
- LangGraph
- Pydantic

### Frontend

- React
- TypeScript
- Vite

### AI

- Gemini
- LangChain
- LLM-as-a-Judge

## Development

### Backend

```bash
cd backend

# Activate environment
.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload