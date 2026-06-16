# ProposalGenie✨

## AI-Powered Freelance Proposal Generation System

ProposalGenie is an intelligent AI-driven system designed to automatically generate high-quality, personalized freelance proposals. It uses modern LLMs, RAG (Retrieval-Augmented Generation), and multi-agent architecture to craft tailored proposals based on job descriptions and user portfolio data.

---

## Core Idea

Freelancers often lose opportunities due to poorly written or generic proposals. ProposalGenie solves this by:

* Analyzing job descriptions
* Understanding user skills & portfolio
* Retrieving relevant past experience (RAG + FAISS)
* Generating personalized, client-ready proposals using LLM agents

---

## Key Features

*  **Job Analysis Agent** – Extracts requirements from job posts
*  **Portfolio Intelligence (RAG)** – Matches user experience with job needs
*  **Proposal Generator Agent** – Creates tailored proposals using LLMs
*  **Reviewer Agent** – Improves tone, grammar, and impact
*  **FAISS Vector Search** – Fast semantic retrieval of portfolio data
*  **Google Gemini Integration** – High-quality text generation
*  **Multi-Agent Workflow** – Modular AI pipeline for better reasoning

---

##  Architecture

```
Job Post → Analyzer Agent → RAG (FAISS Vector DB)
                     ↓
        Portfolio Matching & Context Building
                     ↓
        Generator Agent (LLM - Gemini)
                     ↓
        Reviewer Agent (Refinement)
                     ↓
           Final Proposal Output
```

---

## Tech Stack

* Python 
* FastAPI (Backend API)
* Google Gemini / Generative AI
* FAISS (Vector Database)
* LangChain (optional orchestration layer)
* Pydantic (Data validation)
* Async SQLAlchemy (Database layer)
* dotenv (.env configuration)

---

## Project Structure (High Level)

```
proposal_agent/
│
├── agents/              # AI agents (Analyzer, Generator, Reviewer)
├── core/                # Config and settings
├── services/           # Gemini / LLM services
├── vector_store/       # FAISS implementation
├── ingest_portfolio.py # Portfolio embedding pipeline
├── main.py             # FastAPI entry point
└── .env.example        # Environment configuration template
```

---

## Environment Variables

Create a `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
GEMINI_DEFAULT_MODEL=gemini-2.5-flash
GEMINI_ANALYZER_MODEL=gemini-2.5-flash
GEMINI_GENERATOR_MODEL=gemini-2.5-flash
GEMINI_REVIEWER_MODEL=gemini-2.5-flash
```

---

## How It Works

1. Add your portfolio data
2. Convert it into embeddings (FAISS indexing)
3. Send a job description
4. AI agents analyze + retrieve relevant context
5. System generates a customized proposal
6. Final output is reviewed and refined

---

## Use Cases

* Freelancers on Upwork / Fiverr
* Agencies automating proposal writing
* AI-based client acquisition tools
* Portfolio-based job matching systems

---

## Security Note

This project uses API keys and environment variables. Never commit `.env` files or credentials to GitHub.

---

## Future Improvements

* UI Dashboard for proposal generation
* Multi-language proposal support
* Fine-tuned proposal scoring model
* Chrome extension for Upwork/Fiverr automation
* Memory-based agent personalization

---

## If you like this project

Give it a star ⭐ and feel free to contribute or fork!
