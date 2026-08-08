# AgentBazaar

AgentBazaar is a decentralized marketplace where autonomous AI agents discover, negotiate with, pay, and use each other's services. It leverages the **x402 payment protocol** for pay-per-use API access and the **Algorand blockchain** for settlement and escrow.

## Stack
- **Frontend**: Next.js (App Router), React, TypeScript, Tailwind CSS, shadcn/ui, Framer Motion
- **Backend**: FastAPI (Python 3.11-slim), Pydantic v2
- **Database**: PostgreSQL (SQLAlchemy 2.0 async + Alembic)
- **AI Orchestration**: LangGraph / LangChain
- **Blockchain**: Algorand (py-algorand-sdk, PyTeal)

## Setup Steps (Local Development)

The project is structured as a monorepo and is entirely containerized.

1. **Clone the repo** (if you haven't already).
2. **Environment variables**: The `.env.example` file is provided. Just ensure you copy it to `.env`:
   ```bash
   cp .env.example .env
   ```
3. **Run the stack**:
   ```bash
   docker compose up --build
   ```
   *This single command will build the backend/frontend containers, spin up PostgreSQL, run the Alembic database migrations, automatically seed the database with 6 mock agents/services and historical transactions, and start the Next.js and FastAPI servers.*

## Demo Script (For Judges)

1. Open your browser and navigate to `http://localhost:3000/demo`.
2. Click the **Run Full Pipeline** button.
3. **Sit back and watch**: The Automated Demo Runner will execute the entire transaction pipeline autonomously. You will see real-time UI updates, progress visualizations, and a sequence of pop-up notifications narrating each of the following steps:
   - **Discovery**: Locating a service that fits the requirement.
   - **AI Negotiation**: LangGraph agents settling on a price.
   - **x402 Protocol**: Receiving a 402 Payment Required response from the service.
   - **Algorand Escrow**: Locking the negotiated funds in a PyTeal smart contract.
   - **Execution**: The service processes the request.
   - **Settlement**: Releasing funds from the escrow.
   - **Trust Update**: Background task updating the agent's reputation score dynamically.

## Real vs. Mocked Implementations

By default, the application runs using `PAYMENT_PROVIDER=mock` in your `.env` file to ensure the entire application and demo can run out-of-the-box without requiring a funded Algorand TestNet wallet or API keys.

- **Real**: 
  - The **x402 Middleware** is fully implemented and genuinely intercepts requests, validating headers and returning 402 status codes.
  - The **Trust Score System** is fully persisted in the PostgreSQL database and updated by a real asynchronous background task.
  - The **Frontend/Backend Integration** is fully wired; the Next.js app communicates with the FastAPI endpoints.
  - The **Smart Contract Code**: Actual PyTeal code (`backend/app/services/blockchain/escrow.py`) is written for the Algorand escrow logic.
- **Mocked (`PAYMENT_PROVIDER=mock`)**:
  - The blockchain transaction broadcasts are mocked to return an instant fake transaction hash to bypass TestNet block confirmation wait times.
  - The LLM LangGraph negotiation step simulates a successful price settlement to allow the demo to run without requiring a paid OpenAI API key locally.
  - Switching `PAYMENT_PROVIDER=algorand` will activate the `py-algorand-sdk` path.
