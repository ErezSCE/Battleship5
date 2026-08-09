# Product Manager Mission Report

**Agent**: product-manager  
**Generated**: 2026-08-09T16:20:58.763Z

---

## User Stories (7)

### US-001: As a player, I want to start a new game session
- So that: I have an isolated game state for my match
- AC: POST /games returns HTTP 201 with a unique game ID; Response includes empty board state for both players; The returned game ID can be used in subsequent API calls
### US-002: As a player, I want to retrieve the current sanitized game view
- So that: I can see my board and opponent's hit/miss markers without seeing their ships
- AC: GET /games/{id} returns HTTP 200 with JSON containing my ship positions and opponent hit/miss markers; Response never includes opponent ship positions; GET with an unknown game ID returns HTTP 404
### US-003: As a Player 1, I want to place my three ships on the board
- So that: the game can start with a valid configuration
- AC: POST /games/{id}/ships with valid coordinates returns HTTP 200 and updates the game state; Invalid placements (overlap, out‑of‑bounds, wrong sizes) return HTTP 400 with a clear error message; After a successful placement the backend stores the ship locations for the player
### US-004: As a Player 1, I want to fire at a coordinate on the opponent's board
- So that: I can try to hit and eventually sink their ships
- AC: POST /games/{id}/shots returns a result field of 'hit', 'miss' or 'sunk'; Turn order is enforced – a shot made out of turn returns HTTP 409 with an appropriate message; When all opponent ships are sunk the response includes 'game_over': true
### US-005: As a player, I want to see my board and an attack view of the opponent
- So that: I understand the current game state and can decide my next move
- AC: UI displays a 6×6 grid showing my ships and any opponent hits on my board; UI displays a separate 6×6 attack grid showing markers for previous hits and misses on the opponent; Clicking a cell in the attack grid sends a shot request and updates both grids based on the backend response
### US-006: As a developer, I want the application containerised and startable with a single command
- So that: I can run the full stack locally without manual setup
- AC: Running 'docker compose up --build' starts both frontend and backend containers without errors; Frontend is reachable at http://localhost:4200 (or configured port) and can successfully call the backend at http://localhost:8000; Both containers have a restart policy of 'unless‑stopped' and recover automatically after a crash
### US-007: As a user, I want all game components (frontend UI, backend API, Docker orchestration) to be wired together
- So that: the game is playable end‑to‑end through the browser
- AC: After docker compose starts, a user can create a game, place ships, fire shots and see results reflected in the UI; No console or network errors appear during the full game flow; The win condition is detected and displayed when all opponent ships are sunk

## Tasks (23)

- **TASK-001** [frontend/Angular CLI] Initialize Angular workspace
- **TASK-002** [backend/FastAPI, Python 3.11] Initialize FastAPI backend skeleton
- **TASK-003** [backend/FastAPI] Configure CORS middleware in FastAPI
- **TASK-004** [backend/Pydantic, Python dict] Implement in‑memory game store and data models
- **TASK-005** [backend/FastAPI] Create POST /games endpoint
- **TASK-006** [backend/FastAPI] Create GET /games/{id} endpoint (sanitized view)
- **TASK-007** [backend/FastAPI, Pydantic] Create POST /games/{id}/ships endpoint
- **TASK-008** [backend/FastAPI, Python logic] Create POST /games/{id}/shots endpoint
- **TASK-009** [backend/FastAPI] Add health‑check endpoint
- **TASK-010** [backend/Python logging] Add stdout logging to backend
- **TASK-011** [testing/pytest] Write pytest unit tests for game session endpoints
- **TASK-012** [testing/pytest] Write pytest tests for ship placement validation
- **TASK-013** [testing/pytest] Write pytest tests for shooting logic
- **TASK-014** [frontend/Angular HttpClient] Create Angular service for API communication
- **TASK-015** [frontend/Angular, TypeScript] Build PlayerBoardComponent
- **TASK-016** [frontend/Angular, TypeScript] Build AttackViewComponent
- **TASK-017** [frontend/Angular, RxJS] Implement ship placement UI interactions
- **TASK-018** [testing/Jest, Karma] Write Angular unit tests for components
- **TASK-019** [infra/Docker, nginx] Write Dockerfile for Angular frontend
- **TASK-020** [infra/Docker, uvicorn] Write Dockerfile for FastAPI backend
- **TASK-021** [infra/Docker Compose v2] Create docker‑compose.yml orchestrator
- **TASK-022** [infra/GitHub Actions] Configure GitHub Actions CI workflow
- **TASK-023** [testing/Cypress] End‑to‑end integration verification script
