# Healthcare AI Orchestrator: Agentic Claim Processing

An enterprise-grade AI orchestration framework designed for high-compliance healthcare environments (BCBS). This project demonstrates a **Multi-Agent system** with integrated **Human-in-the-Loop (HITL)** guardrails and persistent memory.

## 🏗️ Architecture
The system follows a **Decoupled Orchestration Pattern**:
1. **Frontend:** FastAPI handles request validation and asynchronous execution.
2. **Brain:** Gemini 2.0 (Vertex AI) performs clinical reasoning.
3. **Data:** Model Context Protocol (MCP) provides a secure bridge to BigQuery.
4. **Audit:** OpenAI (GPT-4o) acts as a secondary "Judge" to audit compliance.
5. **Memory:** Google Cloud SQL (PostgreSQL) persists state using LangGraph Checkpoints.



## 🛡️ Key Features
* **Stateful Interrupts:** High-cost claims (>$5,000) automatically trigger an `interrupt_before` node, pausing the AI for medical director review.
* **Time-Travel Debugging:** Full versioning of the agent's "Shared Brain" via Cloud SQL, allowing for 100% deterministic audit trails.
* **Secure Tooling:** MCP-based tools utilize parameterized queries to eliminate SQL injection risks.
* **State-Diffing:** A custom utility to highlight specific changes in a claim's status between AI iterations.

## 🚀 Getting Started
1. **Clone the repo:** `git clone https://github.com/jcvyt/healthcare-ai-orchestrator`
2. **Install deps:** `pip install -r requirements.txt`
3. **Set env vars:** Create a `.env` with `OPENAI_API_KEY` and `GOOGLE_APPLICATION_CREDENTIALS`.
4. **Run:** `uvicorn app.main:app --reload`

## 👨‍💻 Author
**JC** *GCP Certified Data Engineer | Multi-Agent Architect*